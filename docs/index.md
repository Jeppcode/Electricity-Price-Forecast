---
layout: default
title: Electricity Price Forecast SE3
---

<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">

<style>
    body { 
        font-family: 'Inter', sans-serif; 
        background-color: #0f172a; /* Slate 900 */
        color: #e2e8f0; /* Slate 200 */
    }
    /* Cards with glass effect */
    .dark-card { 
        background: rgba(30, 41, 59, 0.7); /* Slate 800 with opacity */
        border: 1px solid #334155; /* Slate 700 */
        backdrop-filter: blur(10px);
        border-radius: 1rem; 
        overflow: hidden; 
    }
    .accent-text { color: #38bdf8; } /* Sky 400 */
</style>

<div class="min-h-screen pb-12">

    <header class="border-b border-slate-800 bg-slate-950/50 py-12 mb-10 shadow-2xl">
        <div class="max-w-screen-2xl mx-auto px-6 text-center">
            <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-4 text-white">
                 Electricity Price <span class="accent-text">Forecast</span>
            </h1>
            <p class="text-slate-400 text-xl max-w-2xl mx-auto">
                AI-powered predictions for the Stockholm Region (SE3).
                <br>Optimized for smart energy usage.
            </p>
        </div>
    </header>

    <main class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8">

        <div class="dark-card p-6 mb-10 border border-slate-700">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                <div>
                    <p class="text-sm text-slate-300 font-bold uppercase tracking-wider">Next-day forecast</p>
                    <h2 class="text-2xl font-bold text-white mt-1">Plan before the official price release</h2>
                    <p class="text-slate-400 text-sm mt-2">
                        Official day-ahead prices are typically published around <strong>13:00</strong>. This dashboard provides an earlier forecast so you can plan flexible consumption (EV charging, laundry, dishwasher) in the morning.
                        Once official prices are published, use them as the source of truth.
                    </p>
                </div>
                <div class="text-sm text-slate-400">
                    <div>Forecast date: <span id="forecastDate" class="text-white font-semibold">—</span></div>
                    <div>Updated (UTC): <span id="forecastUpdated" class="text-white font-semibold">—</span></div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
                <div class="rounded-xl border border-slate-700 bg-white/5 p-5">
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-wider">Cheapest hours</p>
                    <div id="cheapestHours" class="mt-2 text-white font-semibold">—</div>
                    <p class="text-slate-400 text-sm mt-2">Good time for EV charging, laundry, dishwasher.</p>
                </div>
                <div class="rounded-xl border border-slate-700 bg-white/5 p-5">
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-wider">Most expensive hours</p>
                    <div id="expensiveHours" class="mt-2 text-white font-semibold">—</div>
                    <p class="text-slate-400 text-sm mt-2">Try to avoid flexible consumption in these windows.</p>
                </div>
                <div class="rounded-xl border border-slate-700 bg-white/5 p-5">
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-wider">Best 4-hour window</p>
                    <div id="bestWindow" class="mt-2 text-white font-semibold">—</div>
                    <p class="text-slate-400 text-sm mt-2">
                        The lowest-average price across any <strong>4 consecutive hours</strong> tomorrow.
                    </p>
                    <div class="mt-3 flex items-center gap-3">
                        <label for="kwh" class="text-slate-400 text-sm whitespace-nowrap">Flexible load (kWh)</label>
                        <input id="kwh" type="range" min="2" max="40" value="10" class="w-full">
                        <div class="text-white font-semibold w-14 text-right"><span id="kwhVal">10</span></div>
                    </div>
                    <p class="text-slate-400 text-sm mt-2">
                        Estimated savings: <span id="savings" class="text-emerald-300 font-semibold">—</span>
                    </p>
                    <p class="text-slate-500 text-xs mt-1">
                        Savings is a simple estimate: moving the selected kWh from the most expensive predicted hour to the cheapest predicted hour.
                    </p>
                </div>
            </div>
        </div>

        <div class="space-y-8">
                
                <div class="dark-card">
                    <div class="p-6 border-b border-slate-700 bg-slate-800/50">
                        <h2 class="text-xl font-bold text-white">
                             Smart Charging Guide
                        </h2>
                    </div>
                    <div class="p-6 bg-white/5">
                        <div class="rounded-lg overflow-hidden border border-slate-600">
                            <img src="PricesDashboard/assets/img/electricity_price_signal.png" class="w-full h-auto" alt="Charging Signal">
                        </div>
                        <div class="mt-4 p-4 rounded-lg bg-emerald-900/20 border border-emerald-500/20">
                            <p class="text-emerald-200 text-sm">
                                <strong>Tip:</strong> Plan your high-energy activities (EV charging, laundry) during the <span class="text-emerald-400 font-bold">Green bars</span>. These are hours when the price is predicted to be lower than the daily average.
                            </p>
                        </div>
                    </div>
                </div>

                <div class="dark-card">
                     <div class="p-6 border-b border-slate-700 bg-slate-800/50">
                        <h2 class="text-xl font-bold text-white"> Price Trend & Performance</h2>
                    </div>
                    <div class="p-6 bg-white/5">
                        <div class="rounded-lg overflow-hidden border border-slate-600">
                            <img src="PricesDashboard/assets/img/price_trend.png" class="w-full h-auto" alt="Price Trend">
                        </div>
                        <p class="mt-3 text-slate-400 text-sm">
                            This graph compares the <strong>Actual Price (Black)</strong> vs our <strong>Model's Prediction (Blue dashed)</strong> for the past days, followed by the future forecast.
                        </p>
                    </div>
                </div>

                <div class="dark-card">
                    <div class="p-6 border-b border-slate-700 bg-slate-800/50">
                        <h2 class="text-xl font-bold text-white"> Key Drivers (Feature Importance)</h2>
                    </div>
                    <div class="p-6 bg-white/5">
                        <div class="rounded-lg overflow-hidden border border-slate-600 w-full mb-4">
                            <img src="PricesDashboard/assets/img/feature_importance.png" class="w-full h-auto object-cover" alt="Feature Importance">
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm text-slate-400">
                            <p>
                                <strong>Understanding the graph:</strong> This chart shows which factors (features) the AI model finds most important when setting the price.
                            </p>
                            <p>
                                <em>"Lags" (e.g., price_lag_24) represent past prices, indicating that electricity prices often repeat patterns from exactly 24 or 48 hours ago.</em>
                            </p>
                        </div>
                    </div>
                </div>

                <div class="dark-card bg-gradient-to-br from-slate-800 to-slate-900 p-6 border-blue-500/30 border">
                    <h3 class="font-bold text-lg text-white mb-4">About the Project</h3>
                    <p class="text-slate-400 text-sm mb-6 leading-relaxed">
                        This is a serverless Machine Learning pipeline built with <strong>Hopsworks</strong> Feature Store & <strong>GitHub Actions</strong>.
                    </p>
                    <div class="mb-6">
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-wider mb-2">Data sources (APIs)</p>
                        <ul class="space-y-2 text-sm text-slate-400">
                            <li>
                                <strong class="text-slate-200">Electricity prices</strong>:
                                day-ahead hourly prices for Sweden price areas (SE1–SE4) from
                                <a class="underline decoration-slate-600 hover:decoration-slate-300" href="https://www.elprisetjustnu.se/">elprisetjustnu.se</a>
                                (via the proxy API at
                                <a class="underline decoration-slate-600 hover:decoration-slate-300" href="https://api.elpris.eu/">api.elpris.eu</a>
                                when available).
                            </li>
                            <li>
                                <strong class="text-slate-200">Weather</strong>:
                                hourly forecast and historical weather from
                                <a class="underline decoration-slate-600 hover:decoration-slate-300" href="https://open-meteo.com/">Open‑Meteo</a>.
                            </li>
                        </ul>
                        <p class="text-slate-500 text-xs mt-3">
                            Official day-ahead prices are typically published around 13:00; this dashboard provides an earlier forecast for planning.
                        </p>
                    </div>
                    <ul class="space-y-2 mb-6 text-sm text-slate-400">
                        <li class="flex items-center gap-2">
                            <span class="text-blue-500">✓</span> Daily Data Fetching
                        </li>
                        <li class="flex items-center gap-2">
                            <span class="text-blue-500">✓</span> XGBoost Training
                        </li>
                        <li class="flex items-center gap-2">
                            <span class="text-blue-500">✓</span> Automated Inference
                        </li>
                    </ul>
                    <a href="https://github.com/Jeppcode/Project" class="block w-full text-center bg-blue-600 hover:bg-blue-500 text-white font-semibold py-3 px-4 rounded-lg transition-all shadow-lg shadow-blue-500/20">
                        View Code on GitHub
                    </a>
                </div>
        </div>
        
        <footer class="mt-16 text-center text-slate-500 text-sm pb-8">
            &copy; 2025 Scalable Machine Learning Project.
        </footer>

    </main>
</div>

<script>
  const SUMMARY_URL = "PricesDashboard/assets/data/forecast_summary.json";

  const fmtHour = (h) => String(h).padStart(2, "0") + ":00";
  const fmtHourRange = (start, end) => `${fmtHour(start)}–${fmtHour(end)}`;

  function setText(id, text) {
    const el = document.getElementById(id);
    if (el) el.textContent = text;
  }

  function setHtml(id, html) {
    const el = document.getElementById(id);
    if (el) el.innerHTML = html;
  }

  function formatHours(list) {
    if (!Array.isArray(list) || list.length === 0) return "—";
    const sorted = [...list].sort((a, b) => a.hour_local - b.hour_local);
    return sorted
      .map((x) => `${fmtHour(x.hour_local)} (${Number(x.price).toFixed(3)} SEK/kWh)`)
      .join("<br/>");
  }

  function computeSavings(summary, kwh) {
    const prices = (summary.predicted_prices || []).map((p) => Number(p.price));
    if (prices.length === 0) return null;
    const min = Math.min(...prices);
    const max = Math.max(...prices);
    return (max - min) * kwh;
  }

  async function loadSummary() {
    try {
      const res = await fetch(SUMMARY_URL, { cache: "no-store" });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const summary = await res.json();

      setText("forecastDate", summary.date_local || "—");
      setText("forecastUpdated", summary.generated_at_utc ? String(summary.generated_at_utc).replace("T", " ").slice(0, 19) : "—");

      setHtml("cheapestHours", formatHours(summary.cheapest_hours));
      setHtml("expensiveHours", formatHours(summary.most_expensive_hours));

      if (summary.best_window_hours && summary.best_window_hours.start_hour != null) {
        const bw = summary.best_window_hours;
        setText("bestWindow", `${fmtHourRange(bw.start_hour, bw.end_hour)} (avg ${Number(bw.avg_price).toFixed(3)} SEK/kWh)`);
      } else {
        setText("bestWindow", "—");
      }

      const kwhEl = document.getElementById("kwh");
      const kwhValEl = document.getElementById("kwhVal");
      const savingsEl = document.getElementById("savings");

      const updateSavings = () => {
        const kwh = Number(kwhEl.value);
        kwhValEl.textContent = String(kwh);
        const s = computeSavings(summary, kwh);
        savingsEl.textContent = s == null ? "—" : `${s.toFixed(0)} SEK (peak → cheapest hour)`;
      };

      if (kwhEl) {
        kwhEl.addEventListener("input", updateSavings);
        updateSavings();
      }
    } catch (e) {
      setText("forecastDate", "—");
      setText("forecastUpdated", "—");
      setText("cheapestHours", "—");
      setText("expensiveHours", "—");
      setText("bestWindow", "—");
      setText("savings", "—");
    }
  }

  loadSummary();
</script>