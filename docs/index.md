---
layout: default
title: Elprisprognos SE3
---

<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">

<style>
    body { font-family: 'Inter', sans-serif; background-color: #f1f5f9; }
    .glass-card { background: white; border-radius: 1rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); border: 1px solid #e2e8f0; overflow: hidden; }
    .glass-header { background: #0f172a; color: white; }
</style>

<div class="min-h-screen pb-12">

    <header class="glass-header py-10 shadow-lg mb-8 border-b-4 border-blue-500">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-2">⚡ Elprisprognos <span class="text-blue-400">SE3</span></h1>
            <p class="text-slate-400 text-lg">AI-driven analys för smartare elanvändning i Stockholm.</p>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="glass-card p-4 flex items-center justify-between">
                <div>
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-wider">Status</p>
                    <p class="text-xl font-bold text-green-600 flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span> Uppdaterad
                    </p>
                </div>
                <div class="text-3xl">✅</div>
            </div>
            <div class="glass-card p-4 flex items-center justify-between">
                <div>
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-wider">Område</p>
                    <p class="text-xl font-bold text-slate-800">SE3 (Sthlm)</p>
                </div>
                <div class="text-3xl">📍</div>
            </div>
            <div class="glass-card p-4 flex items-center justify-between">
                <div>
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-wider">AI Modell</p>
                    <p class="text-xl font-bold text-slate-800">XGBoost</p>
                </div>
                <div class="text-3xl">🤖</div>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">

            <div class="lg:col-span-8 space-y-8">
                
                <div class="glass-card">
                    <div class="p-6 border-b border-slate-100 flex justify-between items-center bg-slate-50">
                        <h2 class="text-xl font-bold text-slate-800">🔌 Ladda Smart Imorgon</h2>
                        <span class="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded">Rekommendation</span>
                    </div>
                    <div class="p-4">
                        <img src="PricesDashboard/assets/img/electricity_price_signal.png" class="w-full h-auto rounded-lg" alt="Ladda smart signal">
                        <div class="mt-4 bg-green-50 p-4 rounded-md border border-green-100 text-sm text-green-800">
                            <strong>Tips:</strong> Planera din energianvändning (tvätt, disk, laddning) till de timmar där staplarna är gröna. Då är priset lägre än dygnssnittet.
                        </div>
                    </div>
                </div>

                <div class="glass-card">
                     <div class="p-6 border-b border-slate-100 bg-slate-50">
                        <h2 class="text-xl font-bold text-slate-800">📈 Pristrend: Historik & Framtid</h2>
                    </div>
                    <div class="p-4">
                        <img src="PricesDashboard/assets/img/price_trend.png" class="w-full h-auto rounded-lg" alt="Pristrend">
                        <p class="mt-2 text-slate-500 text-sm">Grafen visar faktiskt utfall för de senaste dagarna (svart) och vår prognos framåt (orange).</p>
                    </div>
                </div>

            </div>

            <div class="lg:col-span-4 space-y-8">
                
                <div class="glass-card h-full">
                    <div class="p-6 border-b border-slate-100 bg-slate-50">
                        <h2 class="text-xl font-bold text-slate-800">🔍 Vad styr priset?</h2>
                    </div>
                    <div class="p-4 flex flex-col items-center">
                        <img src="PricesDashboard/assets/img/feature_importance.png" class="w-full h-auto rounded-lg shadow-sm mb-4" alt="Feature Importance">
                        <p class="text-slate-500 text-sm leading-relaxed">
                            Vår AI-modell analyserar hundratals datapunkter. Just nu är det dessa faktorer (ovan) som har störst påverkan på elpriset.
                            <br><br>
                            <em>Ofta ser vi att "Lags" (vad priset var igår) och vindhastighet är avgörande.</em>
                        </p>
                    </div>
                </div>

                 <div class="glass-card bg-slate-900 text-white p-6">
                    <h3 class="font-bold text-lg mb-2">Om Projektet</h3>
                    <p class="text-slate-300 text-sm mb-4">
                        Detta är ett serverless ML-system byggt med Hopsworks & GitHub Actions.
                    </p>
                    <a href="https://github.com/Jeppcode/Project" class="inline-block bg-blue-600 hover:bg-blue-700 text-white text-sm font-bold py-2 px-4 rounded transition">
                        Se koden på GitHub &rarr;
                    </a>
                </div>

            </div>
        </div>
        
        <footer class="mt-12 text-center text-slate-400 text-sm pb-8">
            &copy; 2025 Scalable Machine Learning Project.
        </footer>

    </main>
</div>