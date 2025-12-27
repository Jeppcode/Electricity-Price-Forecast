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

        <!--
          1) VALUE + CONTEXT
          2) DECISIONS (cheapest/expensive hours + best window + savings)
          3) TOMORROW HOURLY PREDICTIONS (main plot)
          4) RELIABILITY (predicted vs actual)
          5) EXPLANATION (feature importance)
          6) ABOUT (sources + pipelines + stack)
        -->

        <div class="dark-card p-6 mb-10 border border-slate-700">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                <div>
                    <p class="text-sm text-slate-300 font-bold uppercase tracking-wider">Next-day forecast</p>
                    <h2 class="text-2xl font-bold text-white mt-1">Tomorrow’s electricity price predictions (early access)</h2>
                    <p class="text-slate-400 text-sm mt-2">
                        Official day-ahead prices are typically published around <strong>13:00</strong>. This dashboard provides an earlier forecast so you can plan flexible consumption (EV charging, laundry, dishwasher) before the official release.
                        After 13:00, use official prices as the source of truth.
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
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-wider">Cheapest 4-hour window (charging)</p>
                    <div id="bestWindow" class="mt-2 text-white font-semibold">—</div>
                    <p class="text-slate-400 text-sm mt-2">
                        The lowest average price across <strong>4 consecutive hours</strong> tomorrow.
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
                        The slider only affects the savings estimate (it scales with how many kWh you can shift).
                    </p>
                </div>
            </div>
        </div>

        <div class="space-y-8">

                <!-- TOMORROW HOURLY PREDICTIONS -->
                <div class="dark-card">
                    <div class="p-6 border-b border-slate-700 bg-slate-800/50">
                        <h2 class="text-xl font-bold text-white">Tomorrow: hourly predictions</h2>
                    </div>
                    <div class="p-6 bg-white/5">
                        <div class="rounded-lg overflow-hidden border border-slate-600">
                            <img src="PricesDashboard/assets/img/electricity_price_signal.png" class="w-full h-auto" alt="Tomorrow hourly predictions">
                        </div>
                        <div class="mt-4 p-4 rounded-lg bg-slate-900/30 border border-slate-600/50">
                            <p class="text-slate-200 text-sm leading-relaxed">
                                <strong>How to use:</strong> Use the green/amber/red bars as a quick guide for flexible consumption.
                                Combine this with the “Cheapest hours” and “Cheapest 4-hour window” cards above for an actionable plan.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- RELIABILITY -->
                <div class="dark-card">
                     <div class="p-6 border-b border-slate-700 bg-slate-800/50">
                        <h2 class="text-xl font-bold text-white">Model reliability (recent history)</h2>
                    </div>
                    <div class="p-6 bg-white/5">
                        <div class="rounded-lg overflow-hidden border border-slate-600">
                            <img src="PricesDashboard/assets/img/price_trend.png" class="w-full h-auto" alt="Price Trend">
                        </div>
                        <div class="mt-4 p-4 rounded-lg bg-slate-900/30 border border-slate-600/50">
                            <p class="text-slate-200 text-sm leading-relaxed">
                                <strong>How to read:</strong> <strong>Black</strong> is the actual price, <strong>orange dashed</strong> is the model prediction over recent days.
                                This helps validate that the model tracks price dynamics before using it for planning.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- EXPLANATION -->
                <div class="dark-card">
                    <div class="p-6 border-b border-slate-700 bg-slate-800/50">
                        <h2 class="text-xl font-bold text-white">What drives the prediction?</h2>
                    </div>
                    <div class="p-6 bg-white/5">
                        <div class="rounded-lg overflow-hidden border border-slate-600 w-full mb-4">
                            <img src="PricesDashboard/assets/img/feature_importance.png" class="w-full h-auto object-cover" alt="Feature Importance">
                        </div>
                        <div class="mt-2 p-4 rounded-lg bg-slate-900/30 border border-slate-600/50">
                            <p class="text-slate-200 text-sm leading-relaxed">
                                <strong>Understanding the graph:</strong> Higher bars mean the model relies more on that feature.
                                <em>Lag</em> features (e.g. <code class="text-slate-100">price_lag_24</code>) capture that prices often repeat daily patterns.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- ABOUT -->
                <div class="dark-card bg-gradient-to-br from-slate-800 to-slate-900 p-6 border-blue-500/30 border">
                    <h3 class="font-bold text-lg text-white mb-4">About the Project</h3>
                    <p class="text-slate-400 text-sm mb-6 leading-relaxed">
                        This project forecasts next-day hourly electricity prices for SE3 before the official day-ahead prices are published (~13:00).
                        The goal is to support morning planning for flexible consumption (EV charging, laundry, dishwasher).
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
                            Note: after 13:00, official prices should be used as the source of truth.
                        </p>
                    </div>
                    <div class="mb-6">
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-wider mb-2">Pipelines</p>
                        <p class="text-slate-400 text-sm leading-relaxed">
                            Daily ingestion updates the feature store, daily inference generates predictions and dashboard assets, and monthly training retrains the model.
                        </p>
                        <p class="text-xs text-slate-400 font-bold uppercase tracking-wider mt-4 mb-2">Technology</p>
                        <p class="text-slate-400 text-sm leading-relaxed">
                            Python, XGBoost, Hopsworks Feature Store & Model Registry, GitHub Actions, GitHub Pages.
                        </p>
                    </div>
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
    const peak = Math.max(...prices);
    const bestAvg =
      summary.best_window_hours && summary.best_window_hours.avg_price != null
        ? Number(summary.best_window_hours.avg_price)
        : Math.min(...prices);
    const delta = Math.max(0, peak - bestAvg);
    return delta * kwh;
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
        savingsEl.textContent = s == null ? "—" : `${s.toFixed(0)} SEK (peak → best 4h avg)`;
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