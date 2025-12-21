---
layout: default
title: Elprisprognos SE3
---

<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">

<style>
    body { font-family: 'Inter', sans-serif; background-color: #f3f4f6; }
    .glass-panel { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); }
</style>

<div class="min-h-screen pb-12">
    
    <header class="bg-slate-900 text-white py-12 shadow-xl border-b-4 border-blue-500">
        <div class="max-w-6xl mx-auto px-4 text-center">
            <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-2">⚡ Elprisprognos <span class="text-blue-400">SE3</span></h1>
            <p class="text-slate-400 text-lg max-w-2xl mx-auto">AI-driven prediktion för Stockholms elområde baserat på realtidsväder och historiska data.</p>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 -mt-8 relative z-10">
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="glass-panel p-6 rounded-xl shadow-lg border border-slate-200 flex flex-col items-center justify-center text-center">
                <span class="text-slate-500 text-sm uppercase tracking-wider font-semibold">Pipeline Status</span>
                <div class="flex items-center mt-2">
                    <span class="w-3 h-3 bg-green-500 rounded-full animate-pulse mr-2"></span>
                    <span class="text-xl font-bold text-slate-800">Operational</span>
                </div>
                <p class="text-xs text-slate-400 mt-2">Uppdateras dagligen 08:00</p>
            </div>
            
            <div class="glass-panel p-6 rounded-xl shadow-lg border border-slate-200 flex flex-col items-center justify-center text-center">
                <span class="text-slate-500 text-sm uppercase tracking-wider font-semibold">Modelltyp</span>
                <div class="text-xl font-bold text-slate-800 mt-2">XGBoost Regressor</div>
                <p class="text-xs text-slate-400 mt-2">Tränad på historisk data & väder</p>
            </div>

             <div class="glass-panel p-6 rounded-xl shadow-lg border border-slate-200 flex flex-col items-center justify-center text-center">
                <span class="text-slate-500 text-sm uppercase tracking-wider font-semibold">Elområde</span>
                <div class="text-xl font-bold text-slate-800 mt-2">SE3 (Stockholm)</div>
                <p class="text-xs text-slate-400 mt-2">Påverkas av vind, temp & nederbörd</p>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            
            <div class="bg-white p-6 rounded-2xl shadow-md border border-slate-100">
                <h2 class="text-2xl font-bold text-slate-800 mb-4 flex items-center">
                    <svg class="w-6 h-6 mr-2 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"></path></svg>
                    Prisprognos (Nästa 24h)
                </h2>
                <div class="overflow-hidden rounded-lg bg-slate-50 p-1 border border-slate-100">
                    <img src="./PricesDashboard/assets/img/electricity_price_forecast_se3.png" class="w-full h-auto transform hover:scale-[1.02] transition-transform duration-300" alt="Prisprognos">
                </div>
                <p class="mt-4 text-sm text-slate-500 leading-relaxed">
                    Grafen ovan visar vår modells prediktion (orange) jämfört med faktiskt utfall (blå, om tillgängligt) för de senaste timmarna samt prognos framåt.
                </p>
            </div>

            <div class="bg-white p-6 rounded-2xl shadow-md border border-slate-100">
                <h2 class="text-2xl font-bold text-slate-800 mb-4 flex items-center">
                    <svg class="w-6 h-6 mr-2 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Ladda Smart
                </h2>
                <div class="overflow-hidden rounded-lg bg-slate-50 p-1 border border-slate-100">
                    <img src="./PricesDashboard/assets/img/electricity_price_signal.png" onerror="this.src='https://placehold.co/600x400?text=Graf+kommer+snart...'" class="w-full h-auto transform hover:scale-[1.02] transition-transform duration-300" alt="Ladda smart signal">
                </div>
                <p class="mt-4 text-sm text-slate-500 leading-relaxed">
                    Gröna staplar indikerar timmar där priset förväntas vara lägre än dygnsmedlet. Planera din energianvändning (tvättmaskin, elbilsladdning) till dessa timmar.
                </p>
            </div>

        </div>

        <div class="mt-12 text-center text-slate-400 text-sm">
            <p>Projektet är en del av kursen i Scalable Machine Learning.</p>
            <p class="mt-2">Byggt med <a href="https://hopsworks.ai" class="underline hover:text-blue-500">Hopsworks</a>, <a href="https://github.com/features/actions" class="underline hover:text-blue-500">GitHub Actions</a> & Python.</p>
        </div>

    </main>
</div>