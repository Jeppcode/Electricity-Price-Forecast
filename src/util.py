"""
Utility functions for electricity price prediction.

This module provides functions for fetching:
- Historical and forecast weather data (hourly) from Open-Meteo
- Electricity prices from elprisetjustnu.se API
"""

import os
import datetime
from datetime import date, timedelta
import time
import requests
import pandas as pd
import numpy as np
from typing import Optional
from geopy.geocoders import Nominatim
import openmeteo_requests
import requests_cache
from retry_requests import retry
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


# =============================================================================
# Weather Variables Configuration
# =============================================================================

# Hourly weather variables relevant for electricity price prediction
# These affect power generation (wind, solar) and consumption (heating/cooling)
HOURLY_WEATHER_VARIABLES = [
    # Temperature - drives heating/cooling demand
    "temperature_2m",
    "apparent_temperature",
    
    # Precipitation - affects hydro power
    "precipitation",
    "rain",
    "snowfall",
    
    # Cloud cover - affects solar power
    "cloud_cover",
    
    # Wind - affects wind power generation
    "wind_speed_10m",
    "wind_speed_100m",      # Turbine height
    "wind_direction_10m",
    "wind_direction_100m",
    "wind_gusts_10m",
    
    # Pressure - weather patterns
    "surface_pressure",
]

# Daily weather variables (for aggregated features)
DAILY_WEATHER_VARIABLES = [
    "temperature_2m_mean",
    "temperature_2m_max",
    "temperature_2m_min",
    "apparent_temperature_mean",
    "precipitation_sum",
    "rain_sum",
    "snowfall_sum",
    "wind_speed_10m_max",
    "wind_gusts_10m_max",
    "wind_direction_10m_dominant",
    "sunshine_duration",        # Important for solar!
    "shortwave_radiation_sum",  # Solar energy
]


# =============================================================================
# Coordinate Functions
# =============================================================================

def get_city_coordinates(city_name: str) -> tuple[float, float]:
    """
    Get latitude and longitude for a city name.
    
    Args:
        city_name: Name of the city (e.g., "Stockholm")
        
    Returns:
        Tuple of (latitude, longitude) rounded to 4 decimal places
    """
    geolocator = Nominatim(user_agent="electricity_price_predictor")
    location = geolocator.geocode(city_name)
    
    if location is None:
        raise ValueError(f"Could not find coordinates for city: {city_name}")
    
    return round(location.latitude, 4), round(location.longitude, 4)


# =============================================================================
# Weather Data Functions
# =============================================================================

def get_hourly_historical_weather(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str,
    city: str = "Stockholm"
) -> pd.DataFrame:
    """
    Fetch hourly historical weather data from Open-Meteo Archive API.
    
    Args:
        latitude: Location latitude
        longitude: Location longitude
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        city: City name for labeling
        
    Returns:
        DataFrame with hourly weather data
    """
    # Setup the Open-Meteo API client with cache and retry
    cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": HOURLY_WEATHER_VARIABLES,
        "timezone": "Europe/Stockholm"
    }
    
    print(f"Fetching historical weather for {city} ({latitude}, {longitude})...")
    print(f"Date range: {start_date} to {end_date}")
    
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    
    # Process hourly data
    hourly = response.Hourly()
    
    hourly_data = {
        "timestamp": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        )
    }
    
    # Extract all variables in order
    for i, var_name in enumerate(HOURLY_WEATHER_VARIABLES):
        hourly_data[var_name] = hourly.Variables(i).ValuesAsNumpy()
    
    df = pd.DataFrame(data=hourly_data)
    
    # Add metadata columns
    df['city'] = city
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    
    # Convert to float32 for efficiency
    numeric_cols = [c for c in df.columns if c not in ['timestamp', 'city', 'date', 'hour']]
    for col in numeric_cols:
        df[col] = df[col].astype('float32')
    
    df['hour'] = df['hour'].astype('int16')
    
    print(f"Fetched {len(df)} hourly weather records")
    
    return df


def get_hourly_weather_forecast(
    latitude: float,
    longitude: float,
    city: str = "Stockholm",
    forecast_days: int = 7
) -> pd.DataFrame:
    """
    Fetch hourly weather forecast from Open-Meteo Forecast API.
    
    This is used for predicting future electricity prices.
    
    Args:
        latitude: Location latitude
        longitude: Location longitude
        city: City name for labeling
        forecast_days: Number of days to forecast (default 7)
        
    Returns:
        DataFrame with hourly weather forecast
    """
    # Setup the Open-Meteo API client with cache (1 hour expiry for forecasts)
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": HOURLY_WEATHER_VARIABLES,
        "forecast_days": forecast_days,
        "timezone": "Europe/Stockholm"
    }
    
    print(f"Fetching weather forecast for {city} ({latitude}, {longitude})...")
    
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    
    # Process hourly data
    hourly = response.Hourly()
    
    hourly_data = {
        "timestamp": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        )
    }
    
    # Extract all variables in order
    for i, var_name in enumerate(HOURLY_WEATHER_VARIABLES):
        hourly_data[var_name] = hourly.Variables(i).ValuesAsNumpy()
    
    df = pd.DataFrame(data=hourly_data)
    
    # Add metadata columns
    df['city'] = city
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    
    # Convert to float32 for efficiency
    numeric_cols = [c for c in df.columns if c not in ['timestamp', 'city', 'date', 'hour']]
    for col in numeric_cols:
        df[col] = df[col].astype('float32')
    
    df['hour'] = df['hour'].astype('int16')
    
    print(f"Fetched {len(df)} hourly forecast records")
    
    return df


def get_daily_historical_weather(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str,
    city: str = "Stockholm"
) -> pd.DataFrame:
    """
    Fetch daily aggregated historical weather data from Open-Meteo Archive API.
    
    Useful for daily summary features like sunshine duration.
    
    Args:
        latitude: Location latitude
        longitude: Location longitude
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        city: City name for labeling
        
    Returns:
        DataFrame with daily weather data
    """
    cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": DAILY_WEATHER_VARIABLES,
        "timezone": "Europe/Stockholm"
    }
    
    print(f"Fetching daily historical weather for {city}...")
    
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    
    daily = response.Daily()
    
    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s"),
            end=pd.to_datetime(daily.TimeEnd(), unit="s"),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )
    }
    
    for i, var_name in enumerate(DAILY_WEATHER_VARIABLES):
        daily_data[var_name] = daily.Variables(i).ValuesAsNumpy()
    
    df = pd.DataFrame(data=daily_data)
    df['city'] = city
    
    # Convert to float32
    numeric_cols = [c for c in df.columns if c not in ['date', 'city']]
    for col in numeric_cols:
        df[col] = df[col].astype('float32')
    
    df = df.dropna()
    
    print(f"Fetched {len(df)} daily weather records")
    
    return df


def get_yesterday_hourly_weather(
    latitude: float,
    longitude: float,
    city: str = "Stockholm"
) -> pd.DataFrame:
    """
    Convenience helper: hämta gårdagens timvisa väder för givna koordinater.
    
    Args:
        latitude: Latitud
        longitude: Longitud
        city: Stadens namn (endast metadata)
    
    Returns:
        DataFrame med timvisa vädervärden för gårdagen.
    """
    yesterday = date.today() - timedelta(days=1)
    iso_date = yesterday.isoformat()
    
    df = get_hourly_historical_weather(
        latitude=latitude,
        longitude=longitude,
        start_date=iso_date,
        end_date=iso_date,
        city=city,
    )
    
    # Säkerställ att endast gårdagens data returneras om API:t ger marginalt spann
    df = df[df["date"] == yesterday]
    return df


# =============================================================================
# Electricity Price Functions
# =============================================================================

# Earliest date with historical data according to elprisetjustnu.se docs
ELPRICE_EARLIEST_DATE = date(2022, 11, 1)

# Use .env if available, otherwise fall back to sane defaults
DEFAULT_PRICE_AREA = os.getenv("ELPRICE_AREA", "SE3")
ELPRICE_BASE_URL = os.getenv(
    "ELPRICE_BASE_URL",
    "https://www.elprisetjustnu.se/api/v1/prices"
)
ELPRICE_PROXY_BASE_URL = "https://api.elpris.eu/api/v1/prices"


def _build_elprisetjustnu_url(target_date: date, price_area: str) -> str:
    year = target_date.year
    month = f"{target_date.month:02d}"
    day = f"{target_date.day:02d}"
    return f"{ELPRICE_BASE_URL}/{year}/{month}-{day}_{price_area}.json"


def _build_proxy_legacy_url(target_date: date, price_area: str) -> str:
    """
    Elpris Proxy API in legacy=1 mode.
    Always returns 24 hourly prices (aggregated from 15 min if needed).
    """
    year = target_date.year
    month = f"{target_date.month:02d}"
    day = f"{target_date.day:02d}"
    return f"{ELPRICE_PROXY_BASE_URL}/{year}/{month}-{day}_{price_area}.json?legacy=1"


def fetch_electricity_prices_for_date(
    target_date: date,
    price_area: str = DEFAULT_PRICE_AREA,
    session: Optional[requests.Session] = None
) -> list:
    """
    Fetch electricity prices for a specific date and price area.
    
    Primary source: Elpris Proxy API (mirrors elprisetjustnu.se) with legacy=1,
    which should return 24 hourly values (aggregated from 15-min if needed).
    Fallback: the original elprisetjustnu.se endpoint.
    
    Returns:
        List of dict records for that day (may be empty if no data).
    """
    urls = [
        _build_proxy_legacy_url(target_date, price_area),
        _build_elprisetjustnu_url(target_date, price_area),
    ]
    
    client = session if session is not None else requests
    
    for url in urls:
        for attempt in range(3):
            try:
                resp = client.get(url, timeout=10)
            except requests.RequestException:
                # Connection or other transport error, backoff and retry
                time.sleep(0.2 * (attempt + 1))
                continue
            
            # No data for this date at this source
            if resp.status_code == 404:
                break
            
            # Rate limited, backoff and retry same URL
            if resp.status_code == 429:
                time.sleep(0.5 * (attempt + 1))
                continue
            
            # Other non-success codes, backoff and retry
            if resp.status_code != 200:
                time.sleep(0.2 * (attempt + 1))
                continue
            
            # Status 200, try to parse JSON
            try:
                data = resp.json()
            except ValueError:
                data = []
            
            if data:
                return data
            
            # Empty response, no point in retrying this URL again
            break
    
    return []


def fetch_electricity_prices(
    start_date: date,
    end_date: date,
    price_area: str = DEFAULT_PRICE_AREA,
    show_progress: bool = True,
    request_pause: float = 0.5,
) -> pd.DataFrame:
    """
    Fetch electricity prices for a date range.
    
    Uses Elpris Proxy API (legacy=1) when possible to always get 24 hourly
    values per day, and falls back to the original elprisetjustnu.se API.
    
    The start_date is automatically clamped to the earliest available date
    (2022-11-01) to avoid unnecessary requests.
    
    Args:
        start_date: Start date (inclusive)
        end_date: End date (inclusive)
        price_area: Swedish price area (SE1, SE2, SE3, SE4)
        show_progress: Whether to show progress bar
        request_pause: Seconds to pause between day-requests to avoid rate limits
        
    Returns:
        DataFrame with hourly electricity prices
    """
    from tqdm import tqdm
    
    # Accept strings for convenience
    if isinstance(start_date, str):
        start_date = date.fromisoformat(start_date)
    if isinstance(end_date, str):
        end_date = date.fromisoformat(end_date)
    
    # Clamp to earliest available date
    if start_date < ELPRICE_EARLIEST_DATE:
        print(
            f"Start date {start_date} is before earliest available "
            f"{ELPRICE_EARLIEST_DATE}. Adjusting."
        )
        start_date = ELPRICE_EARLIEST_DATE
    
    if end_date < start_date:
        raise ValueError("end_date cannot be earlier than start_date")
    
    all_records: list[dict] = []
    current_date = start_date
    total_days = (end_date - start_date).days + 1
    
    print(f"Fetching electricity prices from {start_date} to {end_date} for {price_area}...")
    
    iterator = range(total_days)
    if show_progress:
        iterator = tqdm(iterator, desc="Fetching prices")
    
    missing_dates: list[date] = []
    bad_length_dates: list[tuple[date, int]] = []
    success_days = 0
    
    session = requests.Session()
    
    for i in iterator:
        records = fetch_electricity_prices_for_date(
            current_date, price_area=price_area, session=session
        )
        if records:
            all_records.extend(records)
            success_days += 1
            # For proxy legacy we expect 24 values, so track deviations
            if len(records) != 24:
                bad_length_dates.append((current_date, len(records)))
        else:
            missing_dates.append(current_date)
        
        current_date += timedelta(days=1)
        
        # Rate-limit: pause between requests
        if request_pause:
            time.sleep(request_pause)
        # Additional small delay every 100 requests to be nice to the API
        if i > 0 and i % 100 == 0:
            time.sleep(0.5)
    
    if not all_records:
        print("No electricity price data found!")
        return pd.DataFrame()
    
    # Create DataFrame
    df = pd.DataFrame(all_records)
    
    if missing_dates:
        preview = ", ".join(str(d) for d in missing_dates[:3])
        print(f"Warning: missing price data for {len(missing_dates)} day(s). First missing: {preview}")
    
    # Parse timestamps
    if 'time_start' in df.columns:
        df['timestamp'] = pd.to_datetime(df['time_start'], utc=True)
    elif 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
    else:
        raise ValueError("Price response missing time_start/timestamp fields")

    if 'time_end' in df.columns:
        df['time_end'] = pd.to_datetime(df['time_end'], utc=True)
    else:
        # For legacy proxy data we only have time_start and hourly values
        df['time_end'] = df['timestamp'] + pd.Timedelta(hours=1)
    
    # Extract time features
    df['date'] = pd.to_datetime(df['timestamp'].dt.date)
    df['hour'] = df['timestamp'].dt.hour.astype('int16')
    
    # Rename and select columns
    df = df.rename(columns={
        'SEK_per_kWh': 'price_sek',
        'EUR_per_kWh': 'price_eur',
        'EXR': 'exchange_rate'
    })
    
    df['price_area'] = price_area
    
    # Convert to float32
    if 'price_sek' in df.columns:
        df['price_sek'] = df['price_sek'].astype('float32')
    if 'price_eur' in df.columns:
        df['price_eur'] = df['price_eur'].astype('float32')
    if 'exchange_rate' in df.columns:
        df['exchange_rate'] = df['exchange_rate'].astype('float32')
    
    # Select final columns (allow for missing eur/exchange if proxy format changes)
    final_cols = ['timestamp', 'date', 'hour', 'price_area']
    for col in ['price_sek', 'price_eur', 'exchange_rate']:
        if col in df.columns:
            final_cols.append(col)
    
    df = df[final_cols]
    
    # Sort and clean
    df = df.sort_values('timestamp').reset_index(drop=True)
    df = df.dropna(subset=['price_sek'])
    
    print(f"Fetched {len(df)} hourly price records across {success_days} day(s)")
    if missing_dates:
        preview = ", ".join(str(d) for d in missing_dates[:3])
        print(f"Warning: missing price data for {len(missing_dates)} day(s). First missing: {preview}")
    if bad_length_dates:
        preview_bad = ", ".join(f"{d} (len={l})" for d, l in bad_length_dates[:3])
        print(f"Warning: unexpected record count for {len(bad_length_dates)} day(s). First: {preview_bad}")
    
    return df


def _strip_timezone(series: pd.Series) -> pd.Series:
    """Drop timezone information if present to produce a naive datetime series."""
    if pd.api.types.is_datetime64tz_dtype(series):
        return series.dt.tz_convert(None)
    return series


def align_electricity_price_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Align electricity price DataFrame to feature store schema:
    - timestamp/date as naive datetime64[us]
    - hour as int32
    """
    df = df.copy()
    if "timestamp" in df.columns:
        df["timestamp"] = _strip_timezone(pd.to_datetime(df["timestamp"]))
        df["timestamp"] = df["timestamp"].astype("datetime64[us]")
    if "date" in df.columns:
        df["date"] = _strip_timezone(pd.to_datetime(df["date"]))
        df["date"] = df["date"].astype("datetime64[us]")
    if "hour" in df.columns:
        df["hour"] = df["hour"].astype("int32")
    return df


def get_today_electricity_prices(price_area: str = DEFAULT_PRICE_AREA) -> pd.DataFrame:
    """
    Get today's electricity prices.
    
    Args:
        price_area: Swedish price area
        
    Returns:
        DataFrame with today's hourly prices
    """
    today = date.today()
    df = fetch_electricity_prices(today, today, price_area, show_progress=False)
    return align_electricity_price_schema(df)


def get_tomorrow_electricity_prices(price_area: str = DEFAULT_PRICE_AREA) -> pd.DataFrame:
    """
    Get tomorrow's electricity prices (available after ~13:00 today).
    
    Args:
        price_area: Swedish price area
        
    Returns:
        DataFrame with tomorrow's hourly prices, or empty if not yet available
    """
    tomorrow = date.today() + timedelta(days=1)
    df = fetch_electricity_prices(tomorrow, tomorrow, price_area, show_progress=False)
    return align_electricity_price_schema(df)


# =============================================================================
# Feature Engineering Helpers
# =============================================================================

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add time-based features useful for electricity price prediction.
    
    Args:
        df: DataFrame with 'timestamp' column
        
    Returns:
        DataFrame with additional time features
    """
    df = df.copy()
    
    # Basic time features
    df['day_of_week'] = df['timestamp'].dt.dayofweek.astype('int16')  # 0=Monday
    df['is_weekend'] = (df['day_of_week'] >= 5).astype('int16')
    df['month'] = df['timestamp'].dt.month.astype('int16')
    
    # Cyclical encoding for hour (for neural networks)
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24).astype('float32')
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24).astype('float32')
    
    # Cyclical encoding for day of week
    df['dow_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7).astype('float32')
    df['dow_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7).astype('float32')
    
    return df


def add_price_lag_features(
    df: pd.DataFrame,
    lags: list[int] = [1, 24, 168]
) -> pd.DataFrame:
    """
    Add lagged price features for time series prediction.
    
    Args:
        df: DataFrame with 'price_sek' column, sorted by timestamp
        lags: List of lag periods (hours). Default: 1h, 24h (1 day), 168h (1 week)
        
    Returns:
        DataFrame with lag features
    """
    df = df.copy()
    df = df.sort_values('timestamp')
    
    for lag in lags:
        df[f'price_lag_{lag}h'] = df['price_sek'].shift(lag).astype('float32')
    
    return df


# =============================================================================
# Plotting Helpers
# =============================================================================

def plot_electricity_price_forecast(
    price_area: str,
    df: pd.DataFrame,
    file_path: str,
    hindcast: bool = False,
    window_days: int | None = 21,
) -> plt.Figure:
    """
    Plot predicted electricity prices (and actuals if hindcast).

    Args:
        price_area: Price area label, e.g. "SE3"
        df: DataFrame with columns:
            - date
            - predicted_price_sek
            - actual price column (electricity_prices_price_sek or price_sek) if hindcast
        file_path: Path to save the figure
        hindcast: If True, also plot actuals and set x-limits to recent period
    """
    # If hindcast, optionally limit to recent window for readability
    if hindcast and window_days is not None and "date" in df.columns:
        try:
            df = df.copy()
            df["date"] = pd.to_datetime(df["date"])
            cutoff = df["date"].max() - pd.Timedelta(days=window_days)
            df = df[df["date"] >= cutoff]
        except Exception:
            pass

    fig, ax = plt.subplots(figsize=(12, 6))

    day = pd.to_datetime(df["date"])
    ax.plot(
        day,
        df["predicted_price_sek"],
        label="Predicted price (SEK/kWh)",
        color="red",
        linewidth=2,
        marker="o",
        markersize=4,
        markerfacecolor="white",
    )

    actual_col = "electricity_prices_price_sek" if "electricity_prices_price_sek" in df.columns else "price_sek"
    if hindcast and actual_col in df.columns:
        ax.plot(
            day,
            df[actual_col],
            label="Actual price (SEK/kWh)",
            color="black",
            linewidth=2,
            marker="^",
            markersize=4,
            markerfacecolor="grey",
        )

    ax.set_xlabel("Date")
    ax.set_ylabel("SEK / kWh")
    ax.set_title(f"Electricity price hindcast for {price_area}")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
    plt.xticks(rotation=45)

    # Keep y-axis reasonable
    try:
        y_min = min(df["predicted_price_sek"].min(), df[actual_col].min() if hindcast and actual_col in df.columns else np.inf)
        y_max = max(df["predicted_price_sek"].max(), df[actual_col].max() if hindcast and actual_col in df.columns else -np.inf)
        if np.isfinite(y_min) and np.isfinite(y_max):
            pad = (y_max - y_min) * 0.1 if y_max > y_min else 0.1
            ax.set_ylim(bottom=y_min - pad, top=y_max + pad)
    except Exception:
        pass

    if hindcast:
        try:
            x_left = pd.Timestamp(df["date"].min()) - pd.Timedelta(days=2)
            x_right = pd.Timestamp(df["date"].max()) + pd.Timedelta(days=2)
            ax.set_xlim(left=x_left, right=x_right)
        except Exception:
            pass

    ax.legend(loc="best")
    plt.tight_layout()
    plt.savefig(file_path)
    return fig


def plot_next_day_price_forecast(
    forecast_df: pd.DataFrame,
    price_area: str,
    file_path: str | None = None,
) -> plt.Figure:
    """
    Plot next-day hourly price forecast and highlight cheapest/expensive hours.

    Args:
        forecast_df: DataFrame with columns ['date','hour','predicted_price_sek']
        price_area: Price area label
        file_path: Optional path to save figure
    """
    df = forecast_df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['date', 'hour'])

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(df['hour'], df['predicted_price_sek'], color="#1f77b4", alpha=0.8, label="Predicted price")

    # Highlight cheapest / 2nd cheapest and most / 2nd most expensive
    idx_min = df['predicted_price_sek'].idxmin()
    idx_second_min = df.nsmallest(2, 'predicted_price_sek').index[-1] if len(df) > 1 else idx_min
    idx_max = df['predicted_price_sek'].idxmax()
    idx_second_max = df.nlargest(2, 'predicted_price_sek').index[-1] if len(df) > 1 else idx_max

    ax.bar(df.loc[idx_min, 'hour'], df.loc[idx_min, 'predicted_price_sek'], color="green", alpha=0.9, label="Cheapest")
    if idx_second_min != idx_min:
        ax.bar(df.loc[idx_second_min, 'hour'], df.loc[idx_second_min, 'predicted_price_sek'], color="#90ee90", alpha=0.9, label="2nd cheapest")

    ax.bar(df.loc[idx_max, 'hour'], df.loc[idx_max, 'predicted_price_sek'], color="red", alpha=0.9, label="Most expensive")
    if idx_second_max != idx_max:
        ax.bar(df.loc[idx_second_max, 'hour'], df.loc[idx_second_max, 'predicted_price_sek'], color="#ffa500", alpha=0.9, label="2nd most expensive")

    # Annotate primary extremes
    ax.annotate(
        f"Min {df.loc[idx_min, 'predicted_price_sek']:.3f} SEK",
        xy=(df.loc[idx_min, 'hour'], df.loc[idx_min, 'predicted_price_sek']),
        xytext=(0, 12),
        textcoords="offset points",
        ha="center",
        color="green",
        fontsize=9,
        fontweight="bold",
    )
    ax.annotate(
        f"Max {df.loc[idx_max, 'predicted_price_sek']:.3f} SEK",
        xy=(df.loc[idx_max, 'hour'], df.loc[idx_max, 'predicted_price_sek']),
        xytext=(0, -14),
        textcoords="offset points",
        ha="center",
        color="red",
        fontsize=9,
        fontweight="bold",
    )

    ax.set_xlabel("Hour (0-23)")
    ax.set_ylabel("Predicted price (SEK/kWh)")
    ax.set_title(f"Next-day hourly electricity price forecast – {price_area}")
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.legend(loc="best")
    plt.tight_layout()

    if file_path:
        plt.savefig(file_path)
    return fig