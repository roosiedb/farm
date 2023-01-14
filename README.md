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

GitHub Actions
--------------


Bash Script
-----------

Bijzondere resultaten
=====================
Toen de CD Pipeline eindelijk werkte kreeg ik tijdens een van de tests een lege webpagina in beeld en kon ik eerst niet bedenken wat de oorzaak was. Toen ik via "Paginabron weergeven" ontdekte dat de nieuwste HTML file goed was uitgerold, en dus dat het CD proces zelf zijn werk had gedaan, moest de fout ergens anders zitten. Na wat puzzelwerk bleek ik een aanhalingsteken te zijn vergeten. Een belangrijke voetnoot is daarom dat de technische staat van een applicatie prima in orde kan zijn terwijl er praktisch toch nog problemen kunnen optreden als gevolg van niet-geteste onderdelen. Zelfs bij een automatisch CD proces blijft dus een handmatige check (openen/verversen webpagina) essentieel.
