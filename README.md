## Notebooks

Nedan är vår struktur för notebooks. Under varje notebook finns:
- **Syfte**: vad notebooken är till för.
- **Att göra / status**: checklista som vi uppdaterar löpande.
- **Kommentarer**: fri text där vi skriver vad som är gjort och vad nästa person behöver veta.

---

### Notebook 1 – Backfill

**Syfte**  
Körs bara en gång för att hämta historisk data via API och skapa feature groups i Hopsworks.

- Skapa feature groups:
  - `electricity_prices`
  - `weather`
- Feature engineering:
  - Lägg till veckodag/helg (antingen exakt veckodag eller bara "helg/inte helg").
  - Få in helgdagar/högtider.

**Att göra / status**

- [X] Hämta historisk elprisd data och skriva till `electricity_prices` feature group.
- [X] Hämta historisk väderdata och skriva till `weather` feature group.
- [X] Implementera logik för veckodag/helg.
- [X] Implementera logik för helgdagar/högtider.
- [X] Implementera lagged features. 
- [X] Verifiera att feature groups ser korrekta ut i Hopsworks.

**Kommentarer**
- 


---

### Notebook 2 – Daglig uppdatering av data

**Syfte**  
Hålla databasen uppdaterad med korrekt och sann data.

- Lägg till gårdagens faktiska elpris.
- Lägg till faktiskt väderutfall från igår.

**Att göra / status**

- [X] Skapa jobb för att hämta gårdagens elpris.
- [X] Skapa jobb för att hämta gårdagens väder.
- [X] Uppdatera respektive feature group i Hopsworks.
- [ ] Säkerställa att notebooken kan köras schemalagt (eller manuellt dagligen).
- [ ] Logga om uppdateringen lyckades eller inte.

**Kommentarer**

Har lagt till så att notebook 2 ska köras dagligen, första körning blir 12/12. Vi får se om det fungerar.

---

### Notebook 3 – Första basmodellen

**Syfte**  
Skapa första basmodellen. Körs initialt för att ta fram en första modell.

- Hämta features från Hopsworks (sann data).
- Skapa och träna en första modell.
- Göra prediction och utvärdering.

**Att göra / status**

- [X] Definiera vilka features som ska ingå.
- [X] Hämta träningsdata från feature store.
- [X] Träna första modellen.
- [X] Utvärdera modellen (valfri metrik, t.ex. MAE/MSE).
- [X] Logga modellversion och resultat i valfritt system (Hopsworks, MLflow, fil osv).
- [X] Spara modellen så att den kan laddas i Notebook 4.

**Kommentarer**

- Skriv här:
  - Vilken modelltyp vi använder (t.ex. XGBoost, RandomForest, LSTM).
  - Vilka hyperparametrar som testats.
  - Kort kommentar om modellens prestanda.
  - Vad nästa person kan testa härnäst.

---

### Notebook 4 – Predictions och visualisering

**Syfte**  
Göra prediktioner med hjälp av modellen och forecast för väder.

- Hämta väderprognos för minst en dag framåt (kan utökas senare).
- Förutspå elpriser för kommande tidsperiod.
- Skapa feature group om det behövs: `electricity_prices_predictions` med `get_or_create(...)`.
- Skapa plots:
  - Timvis prediktion för elpris.
  - Plot som jämför tidigare prediktioner mot faktiskt utfall.
  - Spara plots i docs/pricesDashboard/assets/img
- Spara bilder i en mapp i repot (t.ex. `plots/`) som används av dashboarden.

**Att göra / status**

- [ ] Ladda senaste modellversionen.
- [ ] Hämta väderprognos från API.
- [ ] Generera features för framtida tidssteg.
- [ ] Göra prediktioner för elpriser.
- [ ] Skapa och spara plots i lokala repot (t.ex. `plots/`).
- [ ] Säkerställa att dashboarden pekar på rätt bildfiler.
- [ ] Eventuellt skriva prediktioner till Hopsworks feature group.

**Kommentarer**

- Skriv här:
  - Var bilder sparas och filnamnsstruktur.
  - Om något måste uppdateras när modellversion ändras.
  - Hur ofta vi tänker köra notebooken.

---

### Notebook 5 – Regelbunden reträning

Vi implenterar att notebook 3 körs regelbundet så kan vi skippa notebook 5 helt. Skillnaden blir att vi alltid ersätter den befingliga modellen med den nya. 

**Syfte**  
Träna om modellen regelbundet, till exempel en gång i veckan.

- Träna om modellen på ny data.
- Jämför nya modellen mot den gamla.
- Om nya modellen är bättre: skriv över den gamla och uppdatera produktion.

**Att göra / status**

- [ ] Bestäm träningsfrekvens (t.ex. varje vecka).
- [ ] Hämta data upp till "nu" från Hopsworks.
- [ ] Träna ny modell.
- [ ] Utvärdera ny modell mot valideringsdata.
- [ ] Jämför med nuvarande produktionsmodell.
- [ ] Om bättre: uppdatera sparad modellversion.
- [ ] Logga resultat och beslut (behöll/uppdaterade modellen).

**Kommentarer**

- Skriv här:
  - Hur jämförelsen görs (vilka metriker, vilka fönster).
  - Eventuella trösklar för när modellen får bytas ut.
  - Datum för senaste reträning.

---

## Dashboard

Dashboarden läser in sparade bilder från notebookarna (t.ex. från `plots/`) och uppdateras när nya plots skrivs.

Beskriv kort här hur dashboarden funkar tekniskt (om det är Streamlit, webbapp, Jupyter osv).

---

## Miljö och installation

### Skapa conda eller virtuell miljö

```bash
conda create -n book
conda activate book


# Install 'uv' and 'invoke'
pip install invoke dotenv

# 'invoke install' installs python dependencies using uv and requirements.txt
invoke install


## PyInvoke

    invoke aq-backfill
    invoke aq-features
    invoke aq-train
    invoke aq-inference
    invoke aq-clean

## Feldera


pip install feldera ipython-secrets
sudo apt-get install python3-secretstorage
sudo apt-get install gnome-keyring 

mkdir -p /tmp/c.app.hopsworks.ai
ln -s  /tmp/c.app.hopsworks.ai ~/hopsworks
docker run -p 8080:8080 \
  -v ~/hopsworks:/tmp/c.app.hopsworks.ai \
  --tty --rm -it ghcr.io/feldera/pipeline-manager:latest





# Old daily run
name: run-notebook-2
on:
  schedule:
    - cron: "0 8 * * *"
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    env:
      HOPSWORKS_PROJECT: ${{ secrets.HOPSWORKS_PROJECT }}
      HOPSWORKS_HOST: ${{ secrets.HOPSWORKS_HOST }}
      ELPRICE_BASE_URL: ${{ secrets.ELPRICE_BASE_URL }}
      ELPRICE_AREA: ${{ secrets.ELPRICE_AREA }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: |
          pip install -r requirements.txt
          pip install papermill
      - name: Run notebook 2
        env:
          HOPSWORKS_API_KEY: ${{ secrets.HOPSWORKS_API_KEY }}
        run: python -m papermill NotebooksElectricity/2_electricity_prices_feature_pipeline.ipynb /tmp/out.ipynb