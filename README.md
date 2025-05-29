# 🎓 GPT-2 Embeddings Explorer - Učební nástroj

**Vzdělávací projekt pro pochopení fungování jazykových modelů a embeddingů**

## 🎯 O co jde?

Tento projekt je **interaktivní učební pomůcka** navržená pro studenty, kteří chtějí pochopit:
- 🧠 **Co jsou embeddingy** a jak reprezentují slova v neuronových sítích
- 🔤 **Jak funguje tokenizace** - rozdělení textu na menší části
- 📊 **Jak jazykové modely "vidí" text** - převod slov na čísla
- 🔢 **Poziční kódování** - jak model ví, které slovo je první, druhé atd.

## 📚 Co se naučíte?

### 1. **Embeddingy = Číselná reprezentace slov**
- Každé slovo/token je převedeno na vektor čísel (např. 768 čísel)
- Podobná slova mají podobné vektory
- Model "rozumí" slovům díky těmto číslům

### 2. **Tokenizace = Rozdělení textu**
- Text není zpracován po písmenech ani celých slovech
- Používají se "tokeny" - části slov optimální pro model
- Příklad: "Hello world" → ["Hello", "Ġworld"] (Ġ = mezera)

### 3. **Poziční embeddingy = Pořadí slov**
- Model potřebuje vědět, že "Pes kousl člověka" ≠ "Člověk kousl psa"
- Každá pozice má svůj vlastní vektor
- GPT-2 se tyto pozice **naučil** během trénování

## 🚀 Rychlý start pro studenty

### Krok 1: Instalace (3 minuty)
```bash
# Stáhněte projekt
git clone https://github.com/jirpo9/gpt2-embeddings-explorer.git
cd gpt2-embeddings-explorer

# Nainstalujte potřebné knihovny
pip install torch transformers
```

### Krok 2: Spuštění a experimentování
```bash
python src/gpt2_embeddings.py
```

⚠️ **POZOR**: Program zobrazuje VŠECH 768 hodnot embeddingů! Připravte se na hodně čísel!

📖 **Přečtěte si**: [UNDERSTANDING_768_NUMBERS.md](UNDERSTANDING_768_NUMBERS.md) - vysvětluje, co všechna ta čísla znamenají!

### Krok 3: Vyzkoušejte tyto experimenty

#### 🧪 Experiment 1: Základní tokenizace
Zadejte postupně:
- `Hello`
- `Hello world`
- `Hello, world!`

**Co pozorujete?** Jak interpunkce ovlivňuje tokenizaci?

#### 🧪 Experiment 2: Čeština vs. angličtina
Zadejte:
- `The cat is sleeping`
- `Kočka spí`

**Co pozorujete?** Kolik tokenů potřebuje model pro každý jazyk?

#### 🧪 Experiment 3: Poziční význam
Zadejte:
- `Dog bites man`
- `Man bites dog`

**Co pozorujete?** Jak se liší poziční embeddingy?

## 📖 Vysvětlení výstupu programu

Když zadáte text, uvidíte **VŠECH 768 HODNOT** pro každý token:

```
Token #0: 'Hello'
  Norma tokenového emb.: 12.3456
  
  📊 KOMPLETNÍ TOKENOVÝ EMBEDDING (768 hodnot):
  ----------------------------------------------------------------------
  [  0-  7]:  0.1234 -0.5678  0.9012 -0.3456  0.7890 -0.1234  0.5678 -0.9012
  [  8- 15]:  0.3456 -0.7890  0.1234 -0.5678  0.9012 -0.3456  0.7890 -0.1234
  ...
  [760-767]:  0.5678 -0.9012  0.3456 -0.7890  0.1234 -0.5678  0.9012 -0.3456
```

### 🎯 Proč zobrazujeme VŠECHNY hodnoty?

1. **Pochopení složitosti** - Vidět 768 čísel pomáhá pochopit, jak komplexní je reprezentace jediného slova
2. **Žádná magie** - Není tam žádné "speciální" číslo pro "podstatné jméno" nebo "pozitivní význam"
3. **Distributed representation** - Význam je rozložen napříč VŠEMI hodnotami
4. **Scale** - Uvědomění si, že model pracuje s tisíci takovými vektory najednou

### Co znamenají jednotlivé části:

1. **Token** = část textu, kterou model zpracovává
2. **768 čísel** = kompletní reprezentace významu tokenu
3. **Norma** = "velikost" vektoru (jak "silný" je embedding)
4. **Rozsah hodnot** = typicky -3 až +3, ale může být i větší

## 🤔 Otázky k zamyšlení

1. **Proč má "Hello" jiný embedding než "hello"?**
2. **Co se stane, když zadáte velmi dlouhý text?**
3. **Proč některá slova jsou rozdělena na více tokenů?**
4. **Jak model pozná, že "bank" (banka) a "bank" (břeh) jsou různá slova?**

## 📊 Vizualizace konceptu

```
Text: "Hello world"
         ↓
    TOKENIZACE
         ↓
Tokeny: ["Hello", "Ġworld"]
         ↓
    EMBEDDINGY
         ↓
Hello → [0.12, -0.45, 0.78, ... ] (768 čísel)
world → [0.34, 0.56, -0.12, ... ] (768 čísel)
         ↓
    + POZIČNÍ INFO
         ↓
Pozice 0 → [0.01, 0.02, -0.03, ... ]
Pozice 1 → [0.04, -0.05, 0.06, ... ]
         ↓
    MODEL ZPRACUJE
```

## 🎯 Úkoly pro hlubší pochopení

### Úkol 1: Podobnost slov
Spusťte `python examples/example_usage.py` a podívejte se na funkci `compare_texts()`. 
- Která slova jsou si podle modelu podobná?
- Překvapilo vás něco?

### Úkol 2: Vlastní experimenty
Upravte soubor `examples/example_usage.py` a přidejte:
- Porovnání synonym (např. "car" vs "automobile")
- Analýzu emocí (např. "happy" vs "sad" vs "angry")

### Úkol 3: Výzkumná otázka
- Jak by se dal embedding celé věty použít pro klasifikaci sentimentu?
- Navrhněte jednoduchý experiment

## 🛠️ Technické detaily pro zvídavé

- **Model**: GPT-2 (117M parametrů)
- **Dimenze embeddingů**: 768
- **Velikost slovníku**: 50,257 tokenů
- **Max. délka sekvence**: 1024 tokenů
- **Poziční kódování**: Naučené (ne sinusoidální jako v původním Transformeru)

## 📚 Doporučené studijní materiály

1. [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) - vizuální vysvětlení
2. [What Are Word Embeddings?](https://www.youtube.com/watch?v=viZrOnJclY0) - video tutoriál
3. [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - původní Transformer paper

## ❓ Časté dotazy studentů

**Q: Proč má každý token 768 čísel?**
A: Je to designové rozhodnutí. Větší modely (GPT-3) mají více (např. 12,288). Více dimenzí = více "prostoru" pro zachycení nuancí významu.

**Q: Jak model ví, co které číslo znamená?**
A: Neví! Během trénování na miliardách slov se model naučil, které kombinace čísel fungují nejlépe pro predikci dalšího slova.

**Q: Můžu embeddingy vizualizovat?**
A: Ano! 768 dimenzí můžete redukovat na 2D/3D pomocí PCA nebo t-SNE (pokročilé téma).

## 🤝 Příspěvky

Máte nápad na vylepšení pro studenty? Přidejte:
- Nové experimenty
- Lepší vysvětlení
- Vizualizace
- Interaktivní prvky

## 📧 Kontakt

Nejasnosti? Nápady? Vytvořte issue na GitHubu nebo se zeptejte vyučujícího!

---
⭐ **Pro učitele**: Tento projekt je vhodný pro kurzy NLP, úvod do AI nebo praktika z machine learningu. Studenti nepotřebují hluboké znalosti matematiky - důraz je na intuitivní pochopení.