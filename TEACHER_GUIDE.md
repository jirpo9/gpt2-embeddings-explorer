# 👨‍🏫 Průvodce pro vyučující

## Jak používat tento projekt ve výuce

### 📋 Přehled
- **Cílová skupina**: Studenti informatiky, AI/ML
- **Úroveň**: Středně pokročilí (základy programování v Pythonu)
- **Časová náročnost**: 2-4 vyučovací hodiny
- **Prerekvizity**: Základy Pythonu, základní lineární algebra (vektory)

### 🎯 Vzdělávací cíle

Po absolvování tohoto cvičení studenti:
1. **Pochopí** koncept embeddingů a jejich roli v NLP
2. **Dokáží vysvětlit** tokenizaci a její důležitost
3. **Experimentálně ověří** podobnost slov pomocí embeddingů
4. **Porozumí** pozičnímu kódování v transformerech
5. **Získají intuici** o fungování jazykových modelů

### 📚 Doporučená struktura výuky

#### **1. hodina: Teorie a základy (45 min)**

**Úvod (15 min)**
- Co jsou jazykové modely?
- Problém reprezentace textu pro počítače
- One-hot encoding vs. embeddingy

**Tokenizace (15 min)**
- Proč ne písmena? Proč ne celá slova?
- Byte-Pair Encoding (zjednodušeně)
- Ukázka na projektu (Ukázka 1)

**Embeddingy (15 min)**
- Vektorová reprezentace
- Proč 768 dimenzí?
- Ukázka na projektu (Ukázka 2)

#### **2. hodina: Praktické cvičení (45 min)**

**Hands-on experimenty (30 min)**
- Studenti spustí projekt
- Provádějí experimenty z ukázek 1-4
- Zapisují pozorování

**Diskuze výsledků (15 min)**
- Co studenty překvapilo?
- Jaké vzory objevili?
- Otázky a odpovědi

#### **3. hodina: Projekty a rozšíření (45 min)**

**Mini-projekty pro studenty:**

1. **Detektiv synonym** (jednoduchý)
   - Najít 5 párů synonym
   - Změřit jejich podobnost
   - Vytvořit "škálu podobnosti"

2. **Jazykový průzkumník** (střední)
   - Porovnat tokenizaci 5 jazyků
   - Který jazyk je "nejdražší" (nejvíce tokenů)?
   - Hypotéza proč

3. **Embedding analyzátor** (pokročilý)
   - Implementovat PCA vizualizaci
   - Zobrazit skupiny slov ve 2D
   - Interpretovat výsledky

### 🔧 Praktické tipy

#### Proč zobrazujeme VŠECH 768 hodnot?

**Pedagogický důvod**: Studenti potřebují vidět skutečnou složitost:
- **Vizuální šok** - 768 čísel na obrazovce vytvoří "aha moment"  
- **Žádná magie** - není tam žádné speciální číslo pro "sloveso" nebo "pozitivní"
- **Distributed representation** - význam je v kombinaci VŠECH čísel
- **Scale AI** - pomáhá pochopit, proč AI potřebuje tolik výpočetního výkonu

**Tip pro výuku**: 
1. Nechte studenty nejdřív hádat, kolik čísel bude
2. Ukažte jim výstup - budou šokováni
3. Diskutujte, co to znamená pro výpočetní nároky

#### Instalace v učebně
```bash
# Předem stáhnout model (ušetří čas)
python -c "from transformers import GPT2Model; GPT2Model.from_pretrained('gpt2')"
```

#### Časté problémy studentů

**"Proč některá slova začínají Ġ?"**
- Ġ = mezera před slovem
- Součást Byte-Pair Encoding

**"Můžu změnit embedding a dostat jiné slovo?"**
- Ne přímo - embeddingy → slova není 1:1
- Model generuje pravděpodobnosti

**"Proč má 'bank' stejný embedding?"**
- Tento model nemá kontext
- BERT a novější modely to řeší

### 📊 Hodnocení

#### Možné úkoly k odevzdání:

1. **Report z experimentů** (60%)
   - Minimálně 5 různých experimentů
   - Hypotéza → test → závěr
   - Screenshoty a interpretace

2. **Vlastní rozšíření** (40%)
   - Nová funkce v kódu
   - Vizualizace
   - Zajímavý experiment

#### Hodnotící kritéria:
- Pochopení konceptů
- Kvalita experimentů
- Originalita přístupu
- Technické provedení

### 💡 Nápady na rozšíření

1. **Sentiment analýza**
   - Průměr embeddingů pozitivních/negativních slov
   - Jednoduchý klasifikátor

2. **Cross-lingual embeddingy**
   - Porovnání stejných konceptů napříč jazyky
   - Který jazyk je modelu "nejbližší"?

3. **Historická analýza**
   - Jak se liší embeddingy archaických slov?
   - Co model "neví"?

4. **Vizualizace**
   - t-SNE nebo PCA
   - Interaktivní web aplikace (Streamlit)
   - Clustering slov

### 📖 Doporučená literatura

**Pro studenty:**
- [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/)
- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

**Pro hlubší pochopení:**
- Původní GPT-2 paper
- "Attention Is All You Need"
- Blog posts od Jay Alammar

### ⚠️ Upozornění

1. **Výpočetní náročnost**: První spuštění stáhne ~500MB
2. **Paměťové nároky**: Minimálně 4GB RAM
3. **Časová náročnost**: Některé experimenty mohou trvat déle

### 🎓 Návazující témata

Po tomto cvičení mohou následovat:
- Fine-tuning jazykových modelů
- Attention mechanismus
- BERT a kontextové embeddingy
- Prompt engineering
- Etické aspekty LLM

### 📧 Zpětná vazba

Sdílejte své zkušenosti s použitím tohoto projektu ve výuce:
- Co fungovalo dobře?
- Co studenty bavilo nejvíce?
- Jaká rozšíření jste implementovali?

---

**Tip**: Projekt je navržen tak, aby byl co nejvíce hands-on. Nechte studenty experimentovat a objevovat!