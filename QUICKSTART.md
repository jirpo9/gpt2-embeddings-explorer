# 🚀 Quick Start Guide

## Rychlé spuštění za 3 minuty

### 1. Stažení projektu
```bash
git clone https://github.com/jirpo9/gpt2-embeddings-explorer.git
cd gpt2-embeddings-explorer
```

### 2. Instalace
```bash
pip install torch transformers
```

### 3. Spuštění
```bash
python src/gpt2_embeddings.py
```

## První kroky

Po spuštění uvidíte:
```
GPT-2 Embeddings Explorer
==================================================

Načten model: gpt2
Velikost slovníku: 50,257
Dimenze embeddingů: 768
Max. délka sekvence: 1024

--------------------------------------------------

Zadejte text k analýze (nebo 'q' pro ukončení): 
```

### Vyzkoušejte tyto příklady:

1. **Jednoduchý text:**
   ```
   Hello, world!
   ```

2. **Česká věta:**
   ```
   Dobrý den, jak se máte?
   ```

3. **Technický text:**
   ```
   Machine learning uses neural networks.
   ```

4. **Emoji a speciální znaky:**
   ```
   Python 🐍 is awesome! 
   ```

## Co uvidíte?

Pro každý token dostanete:
- Jak byl text rozdělen na tokeny
- Hodnoty embeddingů (prvních 5)
- Normy vektorů
- Průměrný embedding celého textu

## Další příklady

Spusťte ukázkový skript s pokročilými příklady:
```bash
python examples/example_usage.py
```

## Potřebujete pomoc?

- Otevřete issue na GitHubu
- Podívejte se do README.md pro detailní dokumentaci
- Zkontrolujte requirements.txt pro všechny závislosti

---
💡 **Tip:** Model se při prvním spuštění stahuje (~500MB), buďte trpěliví!