from datetime import datetime, timedelta
import re

# Räkna dos - ett program som hjälper dig att räkna ut hur länge ett recept räcker.
# Av Felix Rosén


def räkna_dos():
    print("\n---WISEMED / FELIX ROSÉN---")
    # ---- INPUT FRÅN ANVÄNDAREN ----
    # Datum för första dos
    while True:
        datum = input("\nNär ska första dosen tas? (ÅÅÅÅMMDD)\n")
        try:
            datum = datetime.strptime(datum, "%Y%m%d")
            break
        except:
            print(f"Oiltigt datum. Försök igen.")
            continue

    # Totalt antal doser i receptet
    while True:
        antal_doser = input("\nHur många doser ingår i receptet?\n")
        try:
            antal_doser = float(antal_doser)
            break
        except:
            print(
                f"Oiltigt antal doser. Försök igen.\nOBS! Använd vid behov punkt som decimaltecken, t ex 1.5."
            )
            continue

    # Maximal dygnsdos
    while True:
        maxdos_dag = input("\nVad är maximal dygnsdos?\n")
        try:
            maxdos_dag = float(maxdos_dag)
            break
        except:
            print(
                f"Oiltig dosmängd. Försök igen.\nOBS! Använd vid behov punkt som decimaltecken, t ex 1.5."
            )
            continue

    # ---- BERÄKNINGAR ----
    # Antalet dagar receptet kan tas enligt ordination.
    antal_dosdagar = int(antal_doser / maxdos_dag)

    # Sista datumet som receptet kan tas enligt ordination.
    dosdagar = timedelta((antal_doser / maxdos_dag) - 1)
    sista_dosdag = datum + dosdagar
    sista_dosdag = str(sista_dosdag)[:10]

    # Antalet doser som blir över efter sista dosdatum.
    doser_kvar = antal_doser % maxdos_dag
    if doser_kvar % 1 == 0.0:
        doser_kvar = int(doser_kvar)
    else:
        doser_kvar = round(doser_kvar, 1)

    # Beräkna snittkonsumtion, om receptet är slut idag.
    dagar_första_dosdag_till_idag = datetime.now() - datum + timedelta(1)
    pattern = re.compile(r"\d+")
    match = re.search(pattern, str(dagar_första_dosdag_till_idag))
    dagar_första_dosdag_till_idag = int(match.group())
    snittkonsumtion = antal_doser / dagar_första_dosdag_till_idag
    if snittkonsumtion % 1 == 0.0:
        snittkonsumtion = int(snittkonsumtion)
    else:
        snittkonsumtion = round(snittkonsumtion, 1)

    # ---- OUTPUT ----
    print(
        f"\nReceptet borde räcka i {antal_dosdagar} hela dagar, till och med {sista_dosdag}."
    )
    print(f"Snittkonsumtion {snittkonsumtion} per dag, om receptet är slut redan idag.")
    print(f"Efter {sista_dosdag} återstår {doser_kvar} doser.")
    print("\n---WISEMED / FELIX ROSÉN---")


räkna_dos()
