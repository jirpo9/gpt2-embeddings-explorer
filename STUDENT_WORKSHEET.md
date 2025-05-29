# 📝 Pracovní list - GPT-2 Embeddings Explorer

**Jméno:** _________________________ **Datum:** _____________

## 🎯 Cíl: Pochopit, jak jazykové modely "vidí" text

### Část 1: Tokenizace (10 bodů)

Spusťte program a vyzkoušejte následující texty. Zapište, na kolik tokenů se rozdělí:

| Text | Počet tokenů | Zajímavé pozorování |
|------|--------------|---------------------|
| "Hello" | _____ | |
| "Hello!" | _____ | |
| "Hello world" | _____ | |
| "Ahoj světe" | _____ | |
| "123456789" | _____ | |
| "AI is cool" | _____ | |

**Otázka 1.1:** Proč má česká věta více tokenů než anglická? (2 body)

_Vaše odpověď:_
```
_______________________________________________
_______________________________________________
_______________________________________________
```

**Otázka 1.2:** Co znamená symbol Ġ před některými tokeny? (2 body)

_Vaše odpověď:_
```
_______________________________________________
```

### Část 2: Embeddingy (15 bodů)

**Experiment 2.1:** Vyberte 3 libovolná slova a zapište jejich embedding statistiky:

| Slovo | Norma vektoru | Min hodnota | Max hodnota |
|-------|---------------|-------------|-------------|
| ____________ | _______ | _______ | _______ |
| ____________ | _______ | _______ | _______ |
| ____________ | _______ | _______ | _______ |

**Otázka 2.2:** Kolik čísel (dimenzí) má každý embedding v GPT-2? (1 bod)

_Odpověď:_ __________

**Otázka 2.3:** Navrhněte, proč model používá tolik dimenzí: (4 body)

_Vaše odpověď:_
```
_______________________________________________
_______________________________________________
_______________________________________________
```

### Část 3: Podobnost slov (20 bodů)

**Experiment 3.1:** Změřte podobnost mezi následujícími páry slov:

| Slovo 1 | Slovo 2 | Kosinová podobnost |
|---------|---------|-------------------|
| cat | dog | _______ |
| cat | car | _______ |
| happy | sad | _______ |
| happy | joyful | _______ |
| one | two | _______ |
| one | 1 | _______ |

**Otázka 3.2:** Které dva páry měly nejvyšší podobnost? Proč? (5 bodů)

_Vaše odpověď:_
```
_______________________________________________
_______________________________________________
```

**Experiment 3.3:** Najděte vlastní trojici slov, kde dvě jsou velmi podobná a jedno velmi odlišné: (5 bodů)

Slovo 1: __________ Slovo 2: __________ Slovo 3: __________

Podobnosti: 1↔2: _____ 1↔3: _____ 2↔3: _____

### Část 4: Poziční embeddingy (15 bodů)

**Experiment 4.1:** Analyzujte tyto dvě věty:

1. "The cat chased the mouse"
2. "The mouse chased the cat"

Tokeny věty 1: _________________________________________________

Tokeny věty 2: _________________________________________________

**Otázka 4.2:** Jsou tokenové embeddingy pro "cat" stejné v obou větách? (2 body)

_Odpověď:_ ☐ ANO ☐ NE

**Otázka 4.3:** Co způsobuje, že model ví o rozdílu mezi větami? (5 bodů)

_Vaše odpověď:_
```
_______________________________________________
_______________________________________________
_______________________________________________
```

### Část 5: Vlastní experiment (20 bodů)

**Navrhněte a proveďte vlastní experiment, který demonstruje něco zajímavého o embeddingech:**

**Hypotéza:** 
```
_______________________________________________
_______________________________________________
```

**Postup:**
```
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________
```

**Výsledky:**
```
_______________________________________________
_______________________________________________
_______________________________________________
```

**Závěr:**
```
_______________________________________________
_______________________________________________
```

### Část 6: Kritické myšlení (20 bodů)

**Otázka 6.1:** Jaké jsou limity této reprezentace textu? Uveďte alespoň 2: (10 bodů)

```
1. ___________________________________________
   ___________________________________________

2. ___________________________________________
   ___________________________________________
```

**Otázka 6.2:** Jak byste vylepšili tento model pro lepší porozumění kontextu? (10 bodů)

_Vaše návrh:_
```
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
```

### Bonusová část: Vizualizace (10 bodů navíc)

Nakreslete nebo popište, jak by vypadala 2D vizualizace embeddingů pro slova:
"cat", "dog", "car", "bicycle", "happy", "sad"

_Váš náčrt / popis:_

```
[Místo pro náčrt nebo popis rozložení slov ve 2D prostoru]




```

---

**Celkový počet bodů: _____ / 100**

**Známka:** _____

**Komentář vyučujícího:**
```
_______________________________________________
_______________________________________________
_______________________________________________
```