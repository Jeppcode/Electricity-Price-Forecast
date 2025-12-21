---
layout: default
title: Elprisprognos
---

<script src="https://cdn.tailwindcss.com"></script>

<style>
    /* Döljer standard-headern i många Jekyll-teman (Minima, Just the Docs etc) */
    .site-header, .site-title, header[role="banner"], .wrapper > header {
        display: none !important;
    }
    /* Tar bort default margins från temat så vår design fyller ut */
    body, .main-content {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        background-color: #0f172a !important; /* Matchar slate-900 */
    }
</style>

<div class="bg-slate-900 min-h-screen text-gray-100 font-sans">
    
    <div class="bg-blue-700 py-8 mb-8 shadow-xl border-b border-blue-800">
        <div class="max-w-6xl mx-auto px-6">
            <h1 class="text-4xl font-extrabold text-white tracking-tight">Electricity Price Dashboard</h1>
            <p class="text-blue-200 mt-2 text-lg">Prediktioner för Stockholm (SE3)</p>
        </div>
    </div>

    <main class="max-w-6xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-3 gap-8 pb-12">
        
        <div class="lg:col-span-2 bg-slate-800 rounded-2xl shadow-2xl border border-slate-700 overflow-hidden">
            <div class="p-6 border-b border-slate-700">
                <h2 class="text-2xl font-bold text-white">Prisprognos (SEK/kWh)</h2>
                <p class="text-slate-400 text-sm mt-1">Historisk data + Prognos för nästa dygn</p>
            </div>
            <div class="p-6 bg-white"> <img src="assets/img/electricity_price_forecast_se3.png" class="w-full h-auto rounded" alt="Grafen kunde inte laddas. Kontrollera att Github Actions har kört.">
            </div>
            <div class="p-4 bg-slate-800 text-center">
                <p class="text-xs text-slate-500">Uppdateras automatiskt kl 08:00</p>
            </div>
        </div>

        <div class="space-y-8">
            
            <div class="bg-slate-800 p-6 rounded-2xl shadow-xl border border-slate-700">
                <h2 class="text-xl font-bold text-white mb-4 border-b border-slate-600 pb-2">SYSTEMSTATUS</h2>
                <ul class="space-y-4">
                    <li class="flex items-center justify-between">
                        <span class="text-slate-300">Pipeline</span>
                        <span class="px-3 py-1 bg-green-900 text-green-300 text-xs font-bold rounded-full border border-green-700">ONLINE</span>
                    </li>
                    <li class="flex items-center justify-between">
                        <span class="text-slate-300">Feature Store</span>
                        <span class="px-3 py-1 bg-blue-900 text-blue-300 text-xs font-bold rounded-full border border-blue-700">HOPSWORKS</span>
                    </li>
                    <li class="flex items-center justify-between">
                        <span class="text-slate-300">Modell</span>
                        <span class="text-sm font-mono text-purple-400">XGBoost</span>
                    </li>
                </ul>
            </div>

            <div class="bg-slate-800 p-6 rounded-2xl shadow-xl border border-slate-700">
                <h2 class="text-xl font-bold text-white mb-4 border-b border-slate-600 pb-2">TRÄFFSÄKERHET</h2>
                <div class="bg-white rounded p-2">
                    <img src="assets/img/model_performance.png" class="w-full h-auto" alt="Prestandagraf saknas">
                </div>
            </div>

        </div>
    </main>
</div>