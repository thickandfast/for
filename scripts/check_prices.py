import json
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICE_FILE = ROOT / "abosjekk" / "priser.json"
REPORT_FILE = ROOT / "price-report.md"

SOURCES = {
    "Mobil": [
        ("Happybytes", "https://happybytes.no/mobilabonnement"),
        ("Chilimobil", "https://www.chilimobil.no/"),
        ("OneCall", "https://onecall.no/mobilabonnement"),
        ("PlussMobil", "https://plussmobil.no/"),
        ("Ice", "https://www.ice.no/mobilabonnement/"),
        ("Talkmore", "https://talkmore.no/"),
    ],
    "Bredbånd": [
        ("Bahnhof", "https://www.bahnhof.no/"),
        ("GlobalConnect", "https://www.globalconnect.no/privat/"),
        ("Ice 5G Hjemme", "https://www.ice.no/hjemmeinternet/"),
        ("Altibox", "https://www.altibox.no/bredband/"),
        ("Telenor", "https://www.telenor.no/internett/"),
        ("Telia", "https://www.telia.no/bredband/"),
    ],
}


def parse_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def count_rows(prices):
    mobile = sum(len(rows) for rows in prices["mobil"]["kategorier"].values())
    broadband = sum(len(rows) for rows in prices["bredband"]["hastigheter"].values())
    return mobile, broadband


def main():
    prices = json.loads(PRICE_FILE.read_text(encoding="utf-8"))
    updated = parse_date(prices.get("_meta", {}).get("oppdatert"))
    today = date.today()
    age_days = (today - updated).days if updated else None
    mobile_rows, broadband_rows = count_rows(prices)

    lines = [
        "# Prisrapport",
        "",
        f"Dato: {today.isoformat()}",
        f"Prisfil: `abosjekk/priser.json`",
        f"Sist oppdatert i JSON: `{updated.isoformat() if updated else 'ukjent'}`",
        f"Alder: `{age_days if age_days is not None else 'ukjent'}` dager",
        "",
        "## Status",
        "",
    ]

    if age_days is None:
        lines.append("- [ ] `_meta.oppdatert` mangler eller har feil format.")
    elif age_days > 100:
        lines.append("- [ ] Prisdata er eldre enn 100 dager. Full kvartalsvis revisjon anbefales.")
    elif age_days > 35:
        lines.append("- [ ] Prisdata er eldre enn 35 dager. Ta en rask sjekk av leverandørene.")
    else:
        lines.append("- [x] Prisdata er nylig oppdatert.")

    lines += [
        f"- [x] Mobilrader i JSON: `{mobile_rows}`",
        f"- [x] Bredbåndsrader i JSON: `{broadband_rows}`",
        "",
        "## Leverandører å sjekke manuelt",
        "",
    ]

    for category, sources in SOURCES.items():
        lines.append(f"### {category}")
        lines.append("")
        for name, url in sources:
            lines.append(f"- [ ] [{name}]({url})")
        lines.append("")

    lines += [
        "## Neste handling",
        "",
        "Oppdater `abosjekk/priser.json` manuelt hvis faste listepriser har endret seg.",
        "Ikke ta med kampanjer, introduksjonstilbud eller rabatter.",
    ]

    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
