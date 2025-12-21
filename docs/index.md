---
layout: default
title: Electricity Price Forecast SE3
---

<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">

<style>
    body { 
        font-family: 'Inter', sans-serif; 
        background-color: #020617; /* Very Dark Slate */
        color: #e2e8f0; 
    }
    .dark-panel { 
        background: #1e293b; /* Slate 800 */
        border: 1px solid #334155; 
        border-radius: 1rem; 
        overflow: hidden; 
    }
    .accent { color: #38bdf8; }
</style>

<div class="min-h-screen pb-12">

    <header class="border-b border-slate-800 bg-slate-900 py-10 mb-8">
        <div class="max-w-7xl mx-auto px-6 text-center">
            <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-2 text-white">
                ⚡ Electricity Price <span class="accent">Forecast</span>
            </h1>
            <p class="text-slate-400">Stockholm Region (SE3) • AI-Powered</p>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="dark-panel p-6 flex items-center justify-between">
                <div>
                    <p class="text-xs text-slate-400 font-bold uppercase">System Status</p>
                    <p class="text-xl font-bold text-emerald-400 mt-1">● Operational</p>
                </div>
            </div>
            <div class="dark-panel p-6 flex items-center justify-between">
                <div>
                    <p class="text-xs text-slate-400 font-bold uppercase">Region</p>
                    <p class="text-xl font-bold text-white mt-1">SE3 Stockholm</p>
                </div>
                <div class="text-2xl">📍</div>
            </div>
            <div class="dark-panel p-6 flex items-center justify-between">
                <div>
                    <p class="text-xs text-slate-400 font-bold uppercase">Model</p>
                    <p class="text-xl font-bold text-white mt-1">XGBoost</p>
                </div>
                <div class="text-2xl">🤖</div>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">

            <div class="lg:col-span-8 space-y-8">
                
                <div class="dark-panel">
                    <div class="p-5 border-b border-slate-700 bg-slate-800 flex justify-between items-center">
                        <h2 class="text-lg font-bold text-white">🔌 Smart Charging Guide</h2>
                        <span class="bg-emerald-500/10 text-emerald-400 text-xs font-bold px-2 py-1 rounded">Recommendation</span>
                    </div>
                    <div class="p-5">
                        <img src="PricesDashboard/assets/img/electricity_price_signal.png" class="w-full h-auto rounded border border-slate-700" alt="Charging Signal">
                        <p class="mt-4 text-emerald-200 text-sm bg-emerald-900/20 p-3 rounded border border-emerald-500/20">
                            <strong>Tip:</strong> Aim for the <span class="text-emerald-400 font-bold">Green bars</span>. These hours are cheaper than the daily average.
                        </p>
                    </div>
                </div>

                <div class="dark-panel">
                     <div class="p-5 border-b border-slate-700 bg-slate-800">
                        <h2 class="text-lg font-bold text-white">📈 Price Trend & Forecast</h2>
                    </div>
                    <div class="p-5">
                        <img src="PricesDashboard/assets/img/price_trend.png" class="w-full h-auto rounded border border-slate-700" alt="Price Trend">
                    </div>
                </div>

            </div>

            <div class="lg:col-span-4 space-y-8">
                
                <div class="dark-panel">
                    <div class="p-5 border-b border-slate-700 bg-slate-800">
                        <h2 class="text-lg font-bold text-white">🔍 Key Drivers</h2>
                    </div>
                    <div class="p-5">
                        <img src="PricesDashboard/assets/img/feature_importance.png" class="w-full h-auto rounded border border-slate-700 mb-4" alt="Feature Importance">
                        <p class="text-slate-400 text-xs">
                            The graph above shows which factors (weather, lags) currently influence the electricity price the most.
                        </p>
                    </div>
                </div>
                
                <div class="text-center text-slate-500 text-sm">
                    <p>&copy; 2025 Scalable Machine Learning.</p>
                    <a href="https://github.com/Jeppcode/Project" class="text-blue-500 hover:underline">View on GitHub</a>
                </div>

            </div>
        </div>

    </main>
</div>