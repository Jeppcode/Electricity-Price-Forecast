---
layout: default
title: Elprisprognos SE3
---

<script src="https://cdn.tailwindcss.com"></script>

<div class="bg-gray-50 min-h-screen pb-12">
    <header class="bg-blue-600 py-8 mb-8 shadow-lg">
        <div class="max-w-5xl mx-auto px-4">
            <h1 class="text-3xl font-bold text-white">Electricity Price Dashboard</h1>
            <p class="text-blue-100 mt-2">Prediktioner för Stockholm (SE3) baserat på väder och historik.</p>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <div class="md:col-span-2 bg-white p-6 rounded-xl shadow-md border border-gray-200">
            <h2 class="text-2xl font-bold mb-4 text-gray-800">Morgondagens priser (Prediktion)</h2>
            <img src="./PricesDashboard/assets/img/electricity_price_forecast_se3.png" class="w-full h-auto rounded-lg" alt="Prognosgraf">
            <p class="mt-4 text-sm text-gray-500 text-center">Grafen uppdateras dagligen kl 08:00 via GitHub Actions.</p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-md border border-gray-200">
            <h2 class="text-2xl font-bold mb-4 text-gray-800 uppercase tracking-wider">Modellens Träffsäkerhet</h2>
            <img src="./PricesDashboard/assets/img/model_performance.png" class="w-full h-auto" alt="Modellprestanda">
        </div>

        <div class="bg-white p-6 rounded-xl shadow-md border border-gray-200">
            <h2 class="text-2xl font-bold mb-4 text-gray-800 uppercase tracking-wider">Systemstatus</h2>
            <ul class="space-y-3 mt-4">
                <li class="flex items-center text-sm text-gray-600">
                    <span class="w-3 h-3 bg-green-500 rounded-full mr-2"></span> Pipeline: GitHub Actions Aktiv
                </li>
                <li class="flex items-center text-sm text-gray-600">
                    <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span> Feature Store: Hopsworks
                </li>
            </ul>
        </div>

    </main>
</div>