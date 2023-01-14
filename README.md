[![Test and Deploy](https://github.com/LiekeG9/farm/actions/workflows/main.yml/badge.svg)](https://github.com/LiekeG9/farm/actions/workflows/main.yml)


# farm

Inleiding
=========
De opdracht "CD" was een pittige uitdaging. Veel opgedane vaardigheden moesten worden gecombineerd met nieuwe kennis over GitHub Actions en SSH sleutels om de Continuous Deployment Pipeline te laten functioneren.
De meeste problemen heb ik kunnen oplossen door veel te experimenteren met (deel)oplossingen die ik op het Internet kon vinden.
De grootste uitdagingen voor mij bestonden uit het werkend krijgen van de autorisatie d.m.v. SSH sleutels.

Technische info
===============

VPS via Digital Ocean
---------------------
Het opzetten van een Droplet met Ubuntu 20.04 LTS via DigitalOcean.com vereist geen bijzondere vaardigheden. De wizard leidde me door het proces en zodra de VPS beschikbaar kwam werd ook direct het IP adres getoond en kon ik met 1 muisklik een Console openen.

Bash Script
-----------
Op de Droplet bij Digital Ocean moest ik een Bash script maken waarmee de applicatie vanuit GitHub kon worden gedownload. In eerste instantie heb ik hier telkens een nieuwe Clone gedraaid, maar uiteindelijk bleek het voldoende om alleen een Pull opdracht uit te voeren. Dit script kon vanuit de Console getest worden en stond daarna dus klaar om vanuit een GitHub Action gebruikte te gaan worden.

GitHub Actions
--------------
Het maken van de workflow in GitHub ging relatief soepel, behalve het onderdeel SSH. Ik heb gebruik gemaakt van 2 stappen, namelijk (1) testen en (2) deployment, en ik heb deze los van elkaar kunnen testen. GitHub ondersteunt prima mogelijkheden om onderdelen opnieuw uit te voeren en om in te zoomen op de uitgevoerde processen (inclusief foutmeldingen).

Bijzondere resultaten
=====================
Toen de CD Pipeline eindelijk werkte kreeg ik tijdens een van de tests een lege webpagina in beeld en kon ik eerst niet bedenken wat de oorzaak was. Toen ik via "Paginabron weergeven" ontdekte dat de nieuwste HTML file goed was uitgerold, en dus dat het CD proces zelf zijn werk had gedaan, moest de fout ergens anders zitten. Na wat puzzelwerk bleek ik een aanhalingsteken te zijn vergeten. Een belangrijke voetnoot is daarom dat de technische staat van een applicatie prima in orde kan zijn terwijl er praktisch toch nog problemen kunnen optreden als gevolg van niet-geteste onderdelen. Zelfs bij een automatisch CD proces blijft dus een handmatige check (openen/verversen webpagina) essentieel.

Laatste wijziging: 14-1-2023, 15:40
