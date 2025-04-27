# PelaajaAPI

## Tietoa
PelaajaAPI:ssa pystyy lisäämään pelaajia, etsimään pelaajia, lisätä eventtejä (eli levelien seurantaa), sekä seurata pelaajien etenemistä leveleissä.

## Ohjeet
1. Pura .zip ja avaa Visual Studio Code:ssa
2. Avaa terminaali
3. Kirjoita "python -m venv .venv"
4. Kirjoita ".venv\Scripts\activate"
5. Kirjoita "pip install -r requirements.txt"
6. Kirjoita "fastapi dev app/main.py"

## Keinoälyt
Käytin keinoälyjä apuna kun olin jumissa pitkään jossain kohdassa ja netistä en löytänyt aiheeseen sopivaa apua. Näitä kohtia olivat:
1. "POST /players/{id}/events", koska en saanut millään luotua eventtejä ja tuli kokoajan error 500. Korjasin ChatGPT:n avulla ja ongelmat oli, että en ollut käyttänyt relationship:iä ja muutenkin minun koko EventDb oli aika sekava eikä toiminut.
2. "GET /players/{id}", koska mikään ei toiminut, enkä huomannut mikä voisi olla pielessä. ChatGPT kuitenkin huomautti että return puuttuu. :D
