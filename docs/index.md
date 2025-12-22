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
        <div class="max-w-7xl mx-auto px-6 text-center">
            <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-4 text-white">
                ⚡ Electricity Price <span class="accent-text">Forecast</span>
            </h1>
            <p class="text-slate-400 text-xl max-w-2xl mx-auto">
                AI-powered predictions for the Stockholm Region (SE3).
                <br>Optimized for smart energy usage.
            </p>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
            <div class="dark-card p-6 flex items-center justify-between hover:border-blue-500 transition-colors duration-300">
                <div>
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-wider">System Status</p>
                    <p class="text-2xl font-bold text-emerald-400 flex items-center gap-2 mt-1">
                        <span class="relative flex h-3 w-3">
                          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                          <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
                        </span>
                        Operational
                    </p>
                </div>
            </div>
            
            <div class="dark-card p-6 flex items-center justify-between hover:border-blue-500 transition-colors duration-300">
                <div>
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-wider">Region</p>
                    <p class="text-2xl font-bold text-white mt-1">SE3 Stockholm</p>
                </div>
                <div class="text-3xl opacity-50">📍</div>
            </div>

            <div class="dark-card p-6 flex items-center justify-between hover:border-blue-500 transition-colors duration-300">
                <div>
                    <p class="text-xs text-slate-400 font-bold uppercase tracking-wider">Model Type</p>
                    <p class="text-2xl font-bold text-white mt-1">XGBoost Regressor</p>
                </div>
                <div class="text-3xl opacity-50">🤖</div>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">

            <div class="lg:col-span-8 space-y-8">
                
                <div class="dark-card">
                    <div class="p-6 border-b border-slate-700 flex justify-between items-center bg-slate-800/50">
                        <h2 class="text-xl font-bold text-white flex items-center gap-2">
                            🔌 Smart Charging Guide
                        </h2>
                        <span class="bg-emerald-900/30 text-emerald-400 border border-emerald-500/30 text-xs font-bold px-3 py-1 rounded-full">
                            Actionable Insight
                        </span>
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
                        <h2 class="text-xl font-bold text-white">📈 Price Trend & Performance</h2>
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
                        <h2 class="text-xl font-bold text-white">🔍 Key Drivers (Feature Importance)</h2>
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

            </div>

            <div class="lg:col-span-4 space-y-8">
                
                <div class="dark-card bg-gradient-to-br from-slate-800 to-slate-900 p-6 border-blue-500/30 border sticky top-6">
                    <h3 class="font-bold text-lg text-white mb-4">About the Project</h3>
                    <p class="text-slate-400 text-sm mb-6 leading-relaxed">
                        This is a serverless Machine Learning pipeline built with <strong>Hopsworks</strong> Feature Store & <strong>GitHub Actions</strong>.
                    </p>
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
        </div>
        
        <footer class="mt-16 text-center text-slate-500 text-sm pb-8">
            &copy; 2025 Scalable Machine Learning Project.
        </footer>

    </main>
</div>