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
Het opzetten van een Droplet met Ubuntu 20.04 LTS via DigitalOcean.com vereist geen bijzondere vaardigheden. De wizard leidde me door het proces en zodra de VPS beschikbaar kwam werd ook direct het IP adres getoond en kon ik met één muisklik een Console openen.

Bash Script
-----------
Op de Droplet bij Digital Ocean moest ik een Bash script maken waarmee de applicatie vanuit GitHub kon worden gedownload. In eerste instantie heb ik hier telkens een nieuwe Clone gedraaid, maar uiteindelijk bleek het voldoende om alleen een Pull opdracht uit te voeren. Dit script kon vanuit de Console getest worden en stond daarna dus klaar om vanuit een GitHub Action gebruikt te gaan worden. In het begin had ik nog wat problemen met het navigeren naar de juiste map, om vanuit die map de gewenste opdrachten te initieren. Het gebruik van 'echo' bleek erg handig omdat de output hiervan direct zichtbaar werd in de log van de workflow in GitHub.

GitHub Workflow & Actions
-------------------------
Vanuit de repository in GitHub heb ik een workflow (.yml) aangemaakt voorzien van Actions. Met deze Actions kon ik de CD Pipeline volledig automatiseren. Het maken van deze workflow ging relatief soepel. Ik heb gebruik gemaakt van 2 stappen, namelijk (1) testen en (2) deployment, en ik heb deze los van elkaar kunnen uitproberen. GitHub ondersteunt prima mogelijkheden om vastgelopen onderdelen opnieuw uit te voeren en om in te zoomen op de uitgevoerde processen (inclusief foutmeldingen).

SSH sleutels
------------
Om ervoor te zorgen dat alleen geautoriseerde gebruikers toegang hebben tot de VPS (Droplet) bij Digital Ocean en ook tot de repository van GitHub, heb ik SSH sleutels aangemaakt. De SSH key moest vervolgens geactiveerd worden, en een deel moest ook in GitHub terecht komen op een manier zodat het veilig blijft (secrets). Een van de problemen waar ik tegenaan liep was dat ik vergat om op de VPS het publieke deel aan /root/.ssh/authorized_keys toe te voegen. Dit leverde dan telkens een foutieve 'handshake' op.

Bijzondere resultaten
=====================
Toen de CD Pipeline eindelijk werkte kreeg ik tijdens een van de tests een lege webpagina in beeld en kon ik eerst niet bedenken wat de oorzaak was. Toen ik via "Paginabron weergeven" ontdekte dat de nieuwste HTML file goed was uitgerold, en dus dat het CD proces zelf zijn werk had gedaan, moest de fout ergens anders zitten. Na wat puzzelwerk bleek ik een aanhalingsteken te zijn vergeten. Een belangrijke voetnoot is daarom dat de technische staat van een applicatie prima in orde kan zijn terwijl er praktisch toch nog problemen kunnen optreden als gevolg van niet-geteste onderdelen. Zelfs bij een automatisch CD proces blijft dus een handmatige check (openen/verversen webpagina) essentieel.

Laatste wijziging: 14-1-2023, 15:40
