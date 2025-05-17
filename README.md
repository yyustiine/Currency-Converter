# Currency-Converter

>[!TIP]
>Kods ir paredzēts izpildei ar **Python** un **HTML**, izmantojot **Flask** tīmekļa ietvaru.

> [!NOTE]
> Nepieciešams ielādēt šādas bibliotēkas un rīkus:
>
> flask
> requests
> matplotlib
>
> Ielādēt var ar komandu: `pip install -r requirements.txt`

---

## Projekta Autori
- Luthiena Džemre Akčinara, 3. grupa | 241RDB111
- Justīne Pavārniece, 15. grupa | 241RDC039

## Projekta Pamatmērķi un Uzdevumi

Šī projekta mērķis ir izveidot tīmekļa lietotni, kas ļauj lietotājam:

1. **Veikt valūtu konvertēšanu:** Izmantojot API, lietotājs var konvertēt jebkuru summu starp populārākajām valūtām.
2. **Apskatīt 10 populārāko valūtu kursus pasaulē:** Balstoties uz izvēlēto galveno valūtu, tiek parādīts aktuālais kurss pret pārējām.
3. **Redzēt vēsturisko kursa izmaiņu grafiku:** Tiek ģenerēts grafiks ar izvēlētās valūtas attiecību pret USD pēdējā gada laikā.

---

## Uzdevumu padziļinātais skaidrojums
`Valūtu kursu konversija`: Lietotājs ievada summu un izvēlas sākotnējo un mērķa valūtu. Izmantojot Flask izsauc FreeCurrencyAPI, tiek iegūts aktuālais kurss, aprēķināts rezultāts un izvadīts lietotājam.
`Populārāko valūtu saraksts`: Lietotājs var apskatīt 10 populārākās pasaules valūtas pēc izvēlētās galvenās valūtas. Informācija tiek attēlota sarakstā.
`Kursa izmaiņu grafiks`: Ar matplotlib palīdzību tiek uzzīmēts vēsturisks valūtas kurss pret USD, pamēnešiem (pirms 12 mēnešiem). Grafiks tiek automātiski saglabāts kā kā attēls `static/chart.png`.

---

## Izmantoto Python bibliotēku saraksts un izmantošanas skaidrojums

Šajā projektā izmantotas šadas bibliotēkas:

- `Flask`: Viegls tīmekļa ietvars, kas ļauj apkalpot HTML formas un parādīt dinamisku informāciju.
- `requests`: Nodrošina ērtu veidu, kā veikt HTTP pieprasījums API servisiem.
- `matplotlib`: Tiek izmantota grafika uzzīmēšanai - šeit tā ģenerē kursa izmaiņu līniju diagrammu.
- `os`: Palīdz pārvaldīt ceļus un dzēst iepriekšējo grafiku pirms jaunā ģenerēšanas.
- `datetime`: Lietota, lai aprēķinātu un formatētu datums kursa pieprasījumiem.

---

## Programmatūras izmantošanas metodes

Lietotni iespējams izmantot šādos veidos:

1. **Ceļotājiem:** Ātri pārrēķināt valūtas jebkurā valstī.
2. **Finanšu analītiķiem:** Pārbaudīt, kā izvēlētās valūtas kurss ir mainījies pēdējo mēnešu laikā.
3. **Studentiem un skolotājiem:** Analizēt ekonomikas un finanšu tēmas ar vizuālu atbalstu.
4. **Izglītības mērķiem:** Projekts parāda, kā savienot HTML, Python, API un datu vizualizāciju.

---

## Programmatūras konfigurēšana un palaišana
1. Klonēt GitHub repozitoriju.
2. Instalēt vajadzīgās bibliotēkas.
3. Pārliecināties, ka mape `static/` eksistē (programmatūra to izveido automātiski).
4. Palaist programmu ar komandu:
5. Atvērt pārlūkprogrammā: `http://127.0.0.1:5000/`

---

## Izmantotie avoti

1. https://freecurrecyapi.com/ - API valūtas datu iegūšanai.
2. https://matplotlib.org/ - Dokumentācija par grafiku zīmēšanu ar `matplotlib`.
3. https://flas.palletsprojekts.com/ - Flask oficiālā dokumentācija.
