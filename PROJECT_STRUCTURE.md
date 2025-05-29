🗂️ Přehled adresářů a souborů
gpt2-embeddings-explorer/
│
├── 📚 Dokumentace/
│   ├── README.md                    # Hlavní dokumentace projektu
│   ├── UNDERSTANDING_768_NUMBERS.md # Vysvětlení 768 embeddingů
│   ├── TEACHER_GUIDE.md            # Průvodce pro vyučující
│   ├── STUDENT_WORKSHEET.md        # Pracovní list pro studenty
│   ├── FAQ.md                      # Často kladené otázky
│   └── QUICKSTART.md               # Rychlý start (3 minuty)
│
├── 🐍 Zdrojový kód/
│   ├── src/
│   │   ├── __init__.py            # Package inicializace
│   │   └── gpt2_embeddings.py     # Hlavní modul (třída GPT2EmbeddingsExplorer)
│   │
│   └── examples/
│       ├── __init__.py            # Package inicializace
│       └── example_usage.py       # 5 vzdělávacích ukázek
│
├── 🧪 Testy/
│   └── tests/
│       └── __init__.py            # Připraveno pro budoucí testy
│
├── 📦 Konfigurace a závislosti/
│   ├── requirements.txt           # Minimální závislosti
│   ├── requirements-freeze.txt    # Přesné verze pro reprodukovatelnost
│   ├── setup.py                   # Instalační skript
│  
│
├── ⚙️ Git a projekt/
│   ├── .gitignore                 # Ignorované soubory (venv, cache, atd.)
│   └── LICENSE                    # MIT licence
│
└── 🚫 Lokální (není v gitu)/
    └── venv/                      # Virtuální prostředí Pythonu







    
📄 Detailní popis souborů
Hlavní kód (src/)
gpt2_embeddings.py

Třída: GPT2EmbeddingsExplorer
Metody:

tokenize_text() - Rozdělení textu na tokeny
get_token_embeddings() - Získání embeddingů
analyze_text() - Kompletní analýza s výpisem všech 768 hodnot
get_learned_positional_embeddings() - Poziční embeddingy



Příklady (examples/)
example_usage.py
Obsahuje 5 interaktivních ukázek:

Tokenizace - Jak se text dělí
Embeddingy - Co jsou ta čísla
Podobnost slov - Měření vzdálenosti
Poziční embeddingy - Význam pořadí
Experimentální prostor - Vlastní pokusy

Dokumentace
Pro studenty:

README.md - Úvod a experimenty
UNDERSTANDING_768_NUMBERS.md - Proč tolik čísel?
FAQ.md - Odpovědi na časté otázky
QUICKSTART.md - Začít za 3 minuty

Pro učitele:

TEACHER_GUIDE.md - Jak používat ve výuce
STUDENT_WORKSHEET.md - Úkoly k vypracování