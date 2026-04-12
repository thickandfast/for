# Prisoppdatering for abosjekk

## Hvordan du får rapporten

Den ukentlige jobben kjører i GitHub Actions.

1. Gå til GitHub-repoet.
2. Åpne fanen **Actions**.
3. Velg workflowen **Sjekk prisdata**.
4. Åpne siste kjøring.
5. Last ned artifacten **prisrapport**.

Rapporten heter `price-report.md`. Den er en sjekkliste og statusrapport, ikke en automatisk fasit.

## Filosofi

- Kun faste listepriser.
- Ikke bruk kampanjer, introduksjonstilbud eller rabatter.
- Sjekk direkte hos leverandørene.
- Oppdater `_meta.oppdatert` i `abosjekk/priser.json` ved hver revisjon.
- Publiser aldri automatisk uten manuell godkjenning.

## Anbefalt rytme

- Ukentlig: kjør rapporten og se om prisdataen bør sjekkes.
- Kvartalsvis: gjør full manuell revisjon i januar, april, juli og oktober.
- Ekstraordinært: oppdater tidligere hvis leverandører endrer faste listepriser.

## Mobilpriser

Sjekk faste månedspriser, datamengde, nettoperatør og bindingstid hos:

- Happybytes: https://happybytes.no/mobilabonnement
- Chilimobil: https://www.chilimobil.no/
- OneCall: https://onecall.no/mobilabonnement
- PlussMobil: https://plussmobil.no/
- Ice: https://www.ice.no/mobilabonnement/
- Talkmore: https://talkmore.no/

Dataterskler i JSON:

`1, 3, 5, 10, 12, 20, 30, 50, 999`

## Bredbåndspriser

Sjekk faste listepriser, hastighet, teknologi, bindingstid og etableringsgebyr hos:

- Bahnhof: https://www.bahnhof.no/
- GlobalConnect: https://www.globalconnect.no/privat/
- Ice 5G Hjemme: https://www.ice.no/hjemmeinternet/
- Altibox: https://www.altibox.no/bredband/
- Telenor: https://www.telenor.no/internett/
- Telia: https://www.telia.no/bredband/

Hastighetsnivåer i JSON:

`50, 100, 200, 250, 500, 1000`
