# ❓ Často kladené otázky (FAQ)

## 🎓 Pro studenty

### Základní otázky

**Q: Co je to vlastně embedding?**
> A: Embedding je způsob, jak reprezentovat slova pomocí čísel. Představte si to jako "souřadnice" slova v mnohorozměrném prostoru. Podobná slova mají podobné souřadnice.

**Q: Proč program zobrazuje VŠECH 768 čísel? To je přece nečitelné!**
> A: Právě to je pointa! Chceme, abyste viděli:
> - Jak obrovské množství informací model používá pro jediné slovo
> - Že neexistuje "jedno číslo = jeden význam"  
> - Složitost toho, jak AI "myslí"
> - Že lidský mozek nedokáže tato čísla interpretovat přímo

**Q: Proč 768 dimenzí? Proč ne jen 3 jako v běžném prostoru?**
> A: Jazyk je složitý! Potřebujeme mnoho dimenzí, abychom zachytili všechny nuance významu. 768 je kompromis mezi výkonem a přesností. Větší modely (GPT-3) používají ještě více dimenzí.

**Q: Co znamená ten divný symbol Ġ?**
> A: Ġ znamená, že před tokenem je mezera. Je to způsob, jak model rozlišuje "Hello" na začátku věty od " Hello" uprostřed věty.

### Technické otázky

**Q: Můžu z embeddingu získat zpět původní slovo?**
> A: Ne přímo. Embedding → slovo není jednoznačné. Model při generování textu používá embeddingy k výpočtu pravděpodobností všech možných slov.

**Q: Jak model ví, že "bank" může znamenat "banka" i "břeh"?**
> A: GPT-2 to neví! Používá stejný embedding. Novější modely (BERT, GPT-3) používají kontextové embeddingy, které se mění podle okolních slov.

**Q: Proč některá slova mají záporné hodnoty v embeddingu?**
> A: Čísla v embeddingu nemají přímý význam. Důležité jsou vztahy mezi nimi. Záporné hodnoty jsou normální - jde o relativní pozice v prostoru.

### Praktické otázky

**Q: Proč první spuštění trvá tak dlouho?**
> A: Stahuje se model (~500 MB). Při dalších spuštěních už bude rychlé.

**Q: Můžu použít jiný model než GPT-2?**
> A: Ano! Zkuste změnit `model_name = "gpt2"` na `"gpt2-medium"` nebo `"gpt2-large"` (pozor, jsou větší).

**Q: Jak vizualizovat embeddingy?**
> A: Embeddingy mají 768 dimenzí, což nejde zobrazit. Můžete použít PCA nebo t-SNE k redukci na 2D/3D. Viz bonusové úkoly.

### Konceptuální otázky

**Q: Je embedding slova vždy stejný?**
> A: V GPT-2 ano. V kontextových modelech (BERT) ne - mění se podle věty.

**Q: Jak se model naučil tyto embeddingy?**
> A: Trénováním na miliardách slov textu. Model se učil předpovídat další slovo a přitom si vytvořil užitečné reprezentace.

**Q: Můžu vytvořit vlastní embeddingy?**
> A: Ano! Můžete model dotrénovat (fine-tuning) na vlastních datech. To je ale pokročilé téma.

### Častá nedorozumění

**❌ Mýtus:** "Každé číslo v embeddingu má konkrétní význam"
> ✅ **Realita:** Význam vzniká až kombinací všech čísel dohromady.

**❌ Mýtus:** "Embeddingy jsou jako slovník"
> ✅ **Realita:** Embeddingy zachycují podobnosti a vztahy, ne definice.

**❌ Mýtus:** "Model chápe, co slova znamenají"
> ✅ **Realita:** Model má statistické asociace, ne lidské porozumění.

### Troubleshooting

**Chyba: "CUDA out of memory"**
> Řešení: Model běží na CPU, pokud nemáte GPU. To je v pořádku, jen pomalejší.

**Chyba: "Token indices sequence length is longer"**
> Řešení: Váš text je moc dlouhý. GPT-2 zvládne max 1024 tokenů.

**Chyba: "ModuleNotFoundError"**
> Řešení: Nainstalujte chybějící knihovnu: `pip install transformers torch`

### Zajímavosti

**🤔 Věděli jste, že...**
- GPT-2 byl považován za "nebezpečný" a OpenAI ho nejdřív nezveřejnila?
- Největší GPT-2 má 1.5 miliardy parametrů?
- Tokenizer GPT-2 umí 50,257 různých tokenů?
- Některé jazyky (čínština) potřebují mnohem více tokenů?

### Kam dál?

**Chci se dozvědět více o:**
- **Transformerech** → "Attention Is All You Need" paper
- **BERT** → Kontextové embeddingy
- **GPT-3/4** → Velké jazykové modely
- **Fine-tuning** → Jak přizpůsobit model vlastním datům
- **Prompt engineering** → Jak efektivně komunikovat s LLM

### Otázky pro pokročilé

**Q: Jak funguje attention mechanismus?**
> A: To je nad rámec tohoto projektu, ale zjednodušeně: model se "dívá" na různá slova s různou "pozorností" při vytváření embeddingů.

**Q: Jaký je rozdíl mezi GPT a BERT?**
> A: GPT čte zleva doprava, BERT čte obousměrně. GPT je lepší na generování, BERT na porozumění.

**Q: Můžu embeddingy použít pro vlastní projekt?**
> A: Ano! Embeddingy jsou skvělé pro:
> - Vyhledávání podobných textů
> - Klasifikaci sentimentu  
> - Clustering dokumentů
> - Doporučovací systémy

---

💡 **Máte další otázku?** Zeptejte se vyučujícího nebo vytvořte issue na GitHubu!