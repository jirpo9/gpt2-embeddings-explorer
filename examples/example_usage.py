"""
🎓 Vzdělávací příklady pro pochopení embeddingů v GPT-2

Tyto příklady jsou navrženy tak, aby studentům pomohly pochopit:
- Jak fungují embeddingy
- Co je tokenizace  
- Jak model "vidí" text
- Proč jsou některá slova podobná
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gpt2_embeddings import GPT2EmbeddingsExplorer
import torch


def ukazka_1_tokenizace():
    """
    UKÁZKA 1: Pochopení tokenizace
    
    Studenti uvidí:
    - Jak se text rozděluje na tokeny
    - Že tokeny nejsou vždy celá slova
    - Jak různé jazyky vyžadují různý počet tokenů
    """
    print("\n" + "="*60)
    print("🎓 UKÁZKA 1: JAK FUNGUJE TOKENIZACE")
    print("="*60)
    print("\nTokenizace = rozdělení textu na menší části (tokeny)")
    print("GPT-2 nevidí písmena ani slova, ale TOKENY!\n")
    
    explorer = GPT2EmbeddingsExplorer()
    
    # Různé příklady pro demonstraci
    texty = [
        "Hello",
        "Hello world",  
        "Hello, world!",
        "Ahoj světe",  # Čeština
        "Künstliche Intelligenz",  # Němčina
        "👋🌍",  # Emoji
        "https://www.example.com",  # URL
        "3.14159265359"  # Čísla
    ]
    
    print("Podívejme se, jak model rozděluje různé texty:\n")
    
    for text in texty:
        _, tokens = explorer.tokenize_text(text)
        print(f"Text: '{text}'")
        print(f"  → Tokeny: {tokens}")
        print(f"  → Počet tokenů: {len(tokens)}")
        print()
    
    print("💡 CO SI VŠIMNOUT:")
    print("- Mezera je součástí tokenu (Ġ = mezera před slovem)")
    print("- Čeština potřebuje více tokenů (model trénován hlavně na angličtině)")
    print("- Interpunkce může být samostatný token")
    print("- URL a čísla se často dělí na mnoho tokenů")


def ukazka_2_embeddingy():
    """
    UKÁZKA 2: Co jsou embeddingy
    
    Studenti pochopí:
    - Že každý token má svůj vektor (seznam čísel)
    - Že podobná slova mají podobné vektory
    - Jak velké jsou tyto vektory
    """
    print("\n" + "="*60)
    print("🎓 UKÁZKA 2: CO JSOU EMBEDDINGY")
    print("="*60)
    print("\nEmbedding = reprezentace slova pomocí čísel (vektor)")
    print("GPT-2 používá 768 čísel pro každé slovo!\n")
    
    explorer = GPT2EmbeddingsExplorer()
    
    # Analyzujeme jedno slovo
    word = "cat"
    results = explorer.analyze_text(word, show_details=False)
    
    embedding = results["token_embeddings"][0]
    
    print(f"Slovo '{word}' jako embedding:")
    print(f"- Je to vektor o velikosti: {len(embedding)} čísel")
    print(f"- Rozsah hodnot: od {embedding.min().item():.3f} do {embedding.max().item():.3f}")
    print(f"- Průměrná hodnota: {embedding.mean().item():.3f}")
    print(f"- 'Velikost' vektoru (norma): {embedding.norm().item():.3f}")
    
    # ZOBRAZÍME VŠECH 768 HODNOT
    print(f"\n📊 VŠECH {len(embedding)} HODNOT EMBEDDINGU:")
    print("(Ano, je jich opravdu tolik! Každé číslo přispívá k významu.)")
    print("-" * 70)
    
    for i in range(0, len(embedding), 8):
        values = embedding[i:i+8].tolist()
        formatted = [f"{v:6.3f}" for v in values]
        print(f"[{i:3d}-{min(i+7, len(embedding)-1):3d}]: " + " ".join(formatted))
    
    print("\n💡 K ZAMYŠLENÍ:")
    print("- Dokážete najít nějaký vzor v číslech? (Nedokážete - není tam!)")
    print("- Proč zrovna 768 čísel? (Design rozhodnutí - víc = lepší, ale pomalejší)")
    print("- Co jednotlivá čísla znamenají? (Nic konkrétního - význam je v kombinaci)")
    print("- Představte si, že model pracuje s tisíci takových vektorů najednou!")


def ukazka_3_podobnost_slov():
    """
    UKÁZKA 3: Podobnost slov podle modelu
    
    Studenti uvidí:
    - Že podobná slova mají podobné embeddingy
    - Jak se měří podobnost (kosinová podobnost)
    - Že model "chápe" významy
    """
    print("\n" + "="*60)
    print("🎓 UKÁZKA 3: KTERÁ SLOVA JSOU SI PODOBNÁ?")
    print("="*60)
    print("\nModel dává podobným slovům podobné vektory.")
    print("Podobnost měříme pomocí 'kosinové podobnosti' (0 = různé, 1 = stejné)\n")
    
    explorer = GPT2EmbeddingsExplorer()
    
    # Skupiny slov k porovnání
    skupiny = [
        ("Zvířata", ["cat", "dog", "mouse", "elephant"]),
        ("Barvy", ["red", "blue", "green", "yellow"]),
        ("Čísla", ["one", "two", "three", "four"]),
        ("Pocity", ["happy", "sad", "angry", "excited"])
    ]
    
    for nazev_skupiny, slova in skupiny:
        print(f"\n{nazev_skupiny}:")
        embeddings = []
        
        # Získat embeddingy
        for slovo in slova:
            results = explorer.analyze_text(slovo, show_details=False)
            embeddings.append(results["average_embedding"])
        
        # Porovnat všechny páry
        for i in range(len(slova)):
            for j in range(i + 1, len(slova)):
                sim = torch.nn.functional.cosine_similarity(
                    embeddings[i].unsqueeze(0),
                    embeddings[j].unsqueeze(0)
                ).item()
                print(f"  '{slova[i]}' ← → '{slova[j]}': {sim:.3f}")
    
    print("\n💡 POZOROVÁNÍ:")
    print("- Slova ze stejné kategorie mají vyšší podobnost")
    print("- Model se naučil skupiny slov z trénovacích dat")
    print("- Toto je základ pro 'porozumění' jazyka")


def ukazka_4_pozicni_embeddingy():
    """
    UKÁZKA 4: Proč záleží na pořadí slov
    
    Studenti pochopí:
    - Že pořadí slov je důležité
    - Jak model kóduje pozice
    - Rozdíl mezi stejnými slovy na různých pozicích
    """
    print("\n" + "="*60)
    print("🎓 UKÁZKA 4: POZIČNÍ EMBEDDINGY - POŘADÍ SLOV")
    print("="*60)
    print("\nModel musí vědět, které slovo je první, druhé, třetí...")
    print("Každá pozice má svůj vlastní embedding!\n")
    
    explorer = GPT2EmbeddingsExplorer()
    
    # Věty s různým pořadím slov
    vety = [
        "Dog bites man",
        "Man bites dog",
        "The cat sat on the mat",
        "On the mat sat the cat"
    ]
    
    print("Stejná slova, jiné pořadí = jiný význam:\n")
    
    for veta in vety:
        print(f"Věta: '{veta}'")
        inputs, tokens = explorer.tokenize_text(veta)
        
        # Najít opakující se tokeny
        token_positions = {}
        for idx, token in enumerate(tokens):
            if token in token_positions:
                token_positions[token].append(idx)
            else:
                token_positions[token] = [idx]
        
        # Ukázat tokeny s jejich pozicemi
        print(f"  Tokeny s pozicemi:")
        for idx, token in enumerate(tokens):
            print(f"    Pozice {idx}: '{token}'")
        
        print()
    
    # Demonstrace pozičních embeddingů
    print("\nJak vypadají poziční embeddingy pro první 4 pozice:")
    pos_embeddings = explorer.get_learned_positional_embeddings(4)
    
    for i in range(4):
        emb = pos_embeddings[0, i]
        print(f"Pozice {i}: prvních 5 hodnot = {emb[:5].tolist()}")
    
    print("\n💡 DŮLEŽITÉ:")
    print("- Každá pozice má unikátní embedding")
    print("- Model kombinuje význam slova + jeho pozici")
    print("- Proto 'Dog bites man' ≠ 'Man bites dog'")


def ukazka_5_experimentalni_prostor():
    """
    UKÁZKA 5: Prostor pro experimenty
    
    Studenti mohou experimentovat s vlastními texty
    """
    print("\n" + "="*60)
    print("🎓 UKÁZKA 5: PROSTOR PRO VAŠE EXPERIMENTY")
    print("="*60)
    print("\nNávrhy experimentů pro studenty:\n")
    
    print("1. SYNONYMA:")
    print("   - Porovnejte: 'car' vs 'automobile' vs 'vehicle'")
    print("   - Jsou si opravdu podobná?\n")
    
    print("2. ANTONYMA:")
    print("   - Porovnejte: 'hot' vs 'cold', 'big' vs 'small'")
    print("   - Jak moc jsou rozdílná?\n")
    
    print("3. RŮZNÉ JAZYKY:")
    print("   - Zkuste stejné slovo v různých jazycích")
    print("   - Kolik tokenů každý jazyk potřebuje?\n")
    
    print("4. KONTEXT:")
    print("   - Slovo 'bank' (banka/břeh)")
    print("   - Změní se embedding podle kontextu?\n")
    
    print("5. VLASTNÍ EXPERIMENT:")
    print("   - Co vás zajímá?")
    print("   - Navrhněte a otestujte vlastní hypotézu!")
    
    # Zde může student přidat vlastní kód
    explorer = GPT2EmbeddingsExplorer()
    
    # Příklad: TODO - studenti doplní vlastní experiment
    # moje_slova = ["láska", "love", "amour", "Liebe"]
    # for slovo in moje_slova:
    #     results = explorer.analyze_text(slovo)
    #     ...


def souhrn_pro_studenty():
    """
    Shrnutí hlavních konceptů
    """
    print("\n" + "="*60)
    print("📚 SHRNUTÍ: CO JSME SE NAUČILI")
    print("="*60)
    
    print("\n1. TOKENIZACE:")
    print("   - Text → Tokeny (ne písmena, ne vždy celá slova)")
    print("   - Různé jazyky = různý počet tokenů")
    
    print("\n2. EMBEDDINGY:")
    print("   - Každý token = vektor 768 čísel")
    print("   - Podobná slova = podobné vektory")
    
    print("\n3. POZIČNÍ KÓDOVÁNÍ:")
    print("   - Model ví o pořadí slov")
    print("   - Každá pozice má svůj embedding")
    
    print("\n4. JAK MODEL 'CHÁPE' TEXT:")
    print("   - Kombinuje význam (token embedding) + pozici")
    print("   - Naučil se vztahy mezi slovy z dat")
    
    print("\n🎯 ÚKOL PRO VÁS:")
    print("Navrhněte experiment, který by ukázal něco zajímavého")
    print("o tom, jak model 'rozumí' jazyku!")


if __name__ == "__main__":
    print("🎓 VZDĚLÁVACÍ UKÁZKY - GPT-2 EMBEDDINGS")
    print("Tyto ukázky vám pomohou pochopit, jak fungují jazykové modely\n")
    
    # Menu pro výběr ukázky
    while True:
        print("\nVyberte ukázku:")
        print("1 - Tokenizace (jak se dělí text)")
        print("2 - Embeddingy (čísla reprezentující slova)")
        print("3 - Podobnost slov")
        print("4 - Poziční embeddingy (pořadí slov)")
        print("5 - Prostor pro experimenty")
        print("6 - Spustit všechny ukázky")
        print("S - Shrnutí konceptů")
        print("Q - Konec")
        
        volba = input("\nVaše volba: ").upper()
        
        if volba == "1":
            ukazka_1_tokenizace()
        elif volba == "2":
            ukazka_2_embeddingy()
        elif volba == "3":
            ukazka_3_podobnost_slov()
        elif volba == "4":
            ukazka_4_pozicni_embeddingy()
        elif volba == "5":
            ukazka_5_experimentalni_prostor()
        elif volba == "6":
            ukazka_1_tokenizace()
            ukazka_2_embeddingy()
            ukazka_3_podobnost_slov()
            ukazka_4_pozicni_embeddingy()
            souhrn_pro_studenty()
        elif volba == "S":
            souhrn_pro_studenty()
        elif volba == "Q":
            print("\nDěkujeme za použití! Hodně štěstí při studiu NLP! 🎓")
            break
        else:
            print("Neplatná volba, zkuste znovu.")