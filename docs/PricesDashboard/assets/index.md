# Electricity Price Dashboard

<link rel="stylesheet" href="./assets/css/air-quality.css">

<div class="aq-header" style="text-align:left;">
  <h2 style="margin-bottom:4px;">Next-day electricity price forecast (SE3)</h2>
  <p style="margin:4px 0 10px 0; font-size: 15px;">
    Final project for ID2223 – Scalable Machine Learning, KTH.<br/>
    Contributors: <strong>Jesper Malmgren</strong>, <strong>Niklas Dahlbom</strong>.
  </p>
  <p style="margin:0; font-size: 15px;">
    The pipeline fetches hourly electricity prices (elprisetjustnu.se / proxy) and hourly weather (Open-Meteo), 
    stores them in Hopsworks Feature Store, engineers calendar/holiday/lag features, trains an XGBoost model, 
    and serves a next-day price forecast for SE3. Daily feature updates (Notebook 2), periodic training (Notebook 3), 
    and batch inference (Notebook 4) keep this forecast fresh.
  </p>
</div>

<div class="aq-dashboard">
  <div class="aq-card">
    <h3>SE3 – Next-day forecast</h3>
    <img src="./assets/img/electricity_price_forecast_se3.png" alt="Electricity price forecast Stockholm"/>
  </div>
</div>
