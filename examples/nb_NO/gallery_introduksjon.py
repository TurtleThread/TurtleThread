"""
Introduksjon til TurtleThread
=============================

Nå skal vi lage vårt første skilpaddebroderi.
Det første vi må gjøre er å importere TurtleThread (pass på at det er `installert <../installation.html>`_).
"""


import turtlethread

# %%
# Så oppretter vi et skilpaddeobjekt som vi skal bruke for å tegne med

penn = turtlethread.Turtle()

# %%
# Nå har vi alt vi trenger for å begynne å lage mønster. La oss begynne med en strek.
# For å tegne en strek bruker vi ``forward`` og bestemmer hvor langt vi vil gå (f.eks 300 steg). 

penn = turtlethread.Turtle()
penn.forward(300)

# %%
# Denne koden flytter skilpadden 300 steg, men den lager ingen søm. 
# For at skilpadden skal sy mens den flytter seg må vi bruke forward kommandoen inne i en søm-blokk.
# Den enkleste søm-blokken er en som heter ``running_stitch``. I en running stitch-block så broderer vi
# en rett strek med et fast mellomrom mellom hvert sting.

penn = turtlethread.Turtle()
with penn.running_stitch(30):
    penn.forward(300)

# %%
# Her har vi lagd kode som flytter skilpadda 300 steg fremover, med en running stitch søm, hvor vi
# setter et sting for hvert trettiende steg. Dette tilsvarer at vi setter ca et sting per tredje millimeter.
# La oss se på hvordan dette ser ut. For å gjøre det kan vi bruke ``visualise``-funksjonen, som bruker
# det innebygde ``turtle``-biblioteket for å tegne broderiet vårt.

penn = turtlethread.Turtle()
with penn.running_stitch(30):
    penn.forward(300)
penn.visualise()

# %%
# .. image:: ../figures/introduction_1.png

# %%
# Nå har vi en søm som gir en rett strek fremover.
# For å skifte retning kan vi bruke ``right`` og sende inn antall grader vi vil rotere (f.eks 90 grader). 

penn = turtlethread.Turtle()
with penn.running_stitch(30):
    penn.forward(300)
    penn.right(90)
    penn.forward(300)

penn.visualise()

# %%
# .. image:: ../figures/introduction_2.png



# %%
# Med en for løkke kan vi gjenta dette fire ganger for å få en firkant:

penn = turtlethread.Turtle()
with penn.running_stitch(30):
    for side in range(4):
        penn.forward(300)
        penn.right(90)

penn.visualise()

# %%
# .. image:: ../figures/introduction_3.png

# %%
# Hvis vi bruker en ny løkke og tegner firkanten åtte ganger, så får vi en fin blomst:

penn = turtlethread.Turtle()
with penn.running_stitch(30):
    for kronblad in range(8):
        for side in range(4):
            penn.forward(300)
            penn.right(90)
        penn.right(45)

penn.visualise()

# %%
# .. image:: ../figures/introduction_4.png

# # %%
# Det kan ofte være lurt å finne de variable størrelsene i programmet, og la de være Python-variabler.
# En variabel størrelse i programmet vi akkurat lagde er hvor mange kronblader, så la oss lage en
# Python-variabel hvor vi lagrer antallet kronblader


penn = turtlethread.Turtle()
antall_kronblader = 8

with penn.running_stitch(30):
    for kronblad in range(antall_kronblader):
        for side in range(4):
            penn.forward(300)
            penn.right(90)
        penn.right(360 / antall_kronblader)

# %%
# Prøv å modifisere koden for forskjellige verdier av antall_firkanter og se hva du får

# %% 
# Nå som vi har et fint motiv kan vi for eksempel lagre det som PNG eller SVG bilder

penn = turtlethread.Turtle()
antall_kronblader = 8

with penn.running_stitch(30):
    for kronblad in range(antall_kronblader):
        for side in range(4):
            penn.forward(300)
            penn.right(90)
        penn.right(360 / antall_kronblader)

penn.save("firkantblomst.png")
penn.save("firkantblomst.svg")


# %%
# Eller vi kan lagre DST-fil for å bruke det med en broderimasking

penn = turtlethread.Turtle()
antall_kronblader = 8

with penn.running_stitch(30):
    for kronblad in range(antall_kronblader):
        for side in range(4):
            penn.forward(300)
            penn.right(90)
        penn.right(360 / antall_kronblader)

penn.save("firkantblomst.dst")

# %%
# .. image:: ../figures/firkantblomst_sydd.png