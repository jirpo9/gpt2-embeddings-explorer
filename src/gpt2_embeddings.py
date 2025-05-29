"""
🎓 GPT-2 Embeddings Explorer - Vzdělávací nástroj

Tento program pomáhá studentům pochopit:
1. Co jsou embeddingy - jak počítač "chápe" slova pomocí čísel
2. Jak funguje tokenizace - rozdělení textu na menší části
3. Jak model ví o pořadí slov - poziční embeddingy
4. Jak jazykové modely interně reprezentují text

Autor: jirpo9
Účel: Výuka základů NLP a jazykových modelů
"""

import math
from typing import List, Tuple, Optional
import torch
from transformers import GPT2Tokenizer, GPT2Model


class GPT2EmbeddingsExplorer:
    """Třída pro exploraci embeddingů v GPT-2 modelu."""
    
    def __init__(self, model_name: str = "gpt2"):
        """
        Inicializace exploreru.
        
        Args:
            model_name: Název modelu z Hugging Face (default: "gpt2")
        """
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
            self.model = GPT2Model.from_pretrained(model_name)
            self.model.eval()
            self.model_name = model_name
            self.embedding_dim = self.model.config.hidden_size
            self.max_length = self.model.config.max_position_embeddings
            self.vocab_size = len(self.tokenizer.get_vocab())
        except Exception as e:
            raise RuntimeError(f"Chyba při načítání modelu: {e}")
    
    def get_model_info(self) -> dict:
        """Vrátí informace o modelu."""
        return {
            "model_name": self.model_name,
            "vocab_size": self.vocab_size,
            "embedding_dim": self.embedding_dim,
            "max_sequence_length": self.max_length
        }
    
    def tokenize_text(self, text: str) -> Tuple[torch.Tensor, List[str]]:
        """
        Tokenizuje vstupní text.
        
        Args:
            text: Vstupní text
            
        Returns:
            Tuple obsahující token IDs a seznam tokenů
        """
        if len(text.split()) > self.max_length:
            print(f"Varování: Text bude oříznut na {self.max_length} tokenů.")
        
        inputs = self.tokenizer(text, return_tensors="pt", 
                               truncation=True, max_length=self.max_length)
        tokens = self.tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
        
        return inputs, tokens
    
    def get_token_embeddings(self, inputs: dict) -> torch.Tensor:
        """
        Získá tokenové embeddingy z modelu.
        
        Args:
            inputs: Tokenizovaný vstup
            
        Returns:
            Tensor s embeddingy
        """
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state
    
    def get_learned_positional_embeddings(self, length: int) -> torch.Tensor:
        """
        Získá naučené poziční embeddingy z GPT-2.
        
        Args:
            length: Délka sekvence
            
        Returns:
            Tensor s pozičními embeddingy
        """
        position_ids = torch.arange(length).unsqueeze(0)
        return self.model.wpe(position_ids)
    
    def compute_sinusoidal_positional_embedding(self, position: int, 
                                                dim: int, max_length: int = 10000) -> torch.Tensor:
        """
        Vypočítá sinusoidální poziční embedding (pro srovnání).
        
        Args:
            position: Pozice v sekvenci
            dim: Dimenze embeddingu
            max_length: Maximální délka pro škálování
            
        Returns:
            Poziční embedding
        """
        embedding = torch.zeros(dim)
        for i in range(0, dim, 2):
            if i + 1 < dim:
                embedding[i] = math.sin(position / (max_length ** (i / dim)))
                embedding[i + 1] = math.cos(position / (max_length ** ((i + 1) / dim)))
        return embedding
    
    def analyze_text(self, text: str, show_details: bool = True) -> dict:
        """
        Analyzuje embeddingy pro zadaný text.
        
        Args:
            text: Vstupní text
            show_details: Zda zobrazit detaily pro každý token
            
        Returns:
            Slovník s výsledky analýzy
        """
        # Tokenizace
        inputs, tokens = self.tokenize_text(text)
        
        # Získání embeddingů
        token_embeddings = self.get_token_embeddings(inputs)
        learned_pos_embeddings = self.get_learned_positional_embeddings(len(tokens))
        
        results = {
            "tokens": tokens,
            "token_count": len(tokens),
            "token_embeddings": [],
            "positional_embeddings": [],
            "combined_embeddings": [],
            "average_embedding": None
        }
        
        if show_details:
            print(f"\nTokeny v zadaném textu: {tokens}")
            print("\nAnalýza jednotlivých tokenů:")
            print("-" * 50)
        
        all_combined_embeddings = []
        
        for idx, token in enumerate(tokens):
            # Tokenový embedding
            token_emb = token_embeddings[0, idx]
            
            # Poziční embeddingy (naučené z GPT-2)
            pos_emb = learned_pos_embeddings[0, idx]
            
            # Kombinované embeddingy (jak je GPT-2 skutečně používá)
            # GPT-2 sčítá tokenové a poziční embeddingy
            combined_emb = token_emb  # V GPT-2 už jsou poziční embeddingy zahrnuty
            
            results["token_embeddings"].append(token_emb)
            results["positional_embeddings"].append(pos_emb)
            results["combined_embeddings"].append(combined_emb)
            all_combined_embeddings.append(combined_emb)
            
            if show_details:
                print(f"\nToken #{idx}: '{token}'")
                print(f"  Norma tokenového emb.: {token_emb.norm().item():.4f}")
                print(f"  Norma pozičního emb.: {pos_emb.norm().item():.4f}")
                
                # VZDĚLÁVACÍ ÚČEL: Zobrazíme VŠECH 768 hodnot, aby studenti viděli složitost
                print(f"\n  📊 KOMPLETNÍ TOKENOVÝ EMBEDDING ({len(token_emb)} hodnot):")
                print("  " + "-" * 70)
                # Formátované zobrazení po 8 hodnotách na řádek
                for i in range(0, len(token_emb), 8):
                    values = token_emb[i:i+8].tolist()
                    formatted = [f"{v:7.4f}" for v in values]
                    print(f"  [{i:3d}-{min(i+7, len(token_emb)-1):3d}]: " + " ".join(formatted))
                
                print(f"\n  📊 KOMPLETNÍ POZIČNÍ EMBEDDING ({len(pos_emb)} hodnot):")
                print("  " + "-" * 70)
                for i in range(0, len(pos_emb), 8):
                    values = pos_emb[i:i+8].tolist()
                    formatted = [f"{v:7.4f}" for v in values]
                    print(f"  [{i:3d}-{min(i+7, len(pos_emb)-1):3d}]: " + " ".join(formatted))
        
        # Výpočet průměrného embeddingu (běžnější než součet)
        if all_combined_embeddings:
            results["average_embedding"] = torch.stack(all_combined_embeddings).mean(dim=0)
            
            if show_details:
                print("\n" + "=" * 50)
                print("SOUHRN:")
                print(f"Celkový počet tokenů: {len(tokens)}")
                print(f"Dimenze embeddingů: {self.embedding_dim}")
                print(f"\n🎓 DŮLEŽITÉ PRO STUDENTY:")
                print("Každý token je reprezentován 768 čísly!")
                print("Tato čísla nemají jednotlivý význam - význam vzniká jejich kombinací.")
                print("\nPrůměrný embedding celého textu (všech 768 hodnot):")
                print("-" * 70)
                
                # Zobrazit VŠECHNY hodnoty průměrného embeddingu
                avg_emb = results['average_embedding']
                for i in range(0, len(avg_emb), 8):
                    values = avg_emb[i:i+8].tolist()
                    formatted = [f"{v:7.4f}" for v in values]
                    print(f"[{i:3d}-{min(i+7, len(avg_emb)-1):3d}]: " + " ".join(formatted))
                
                print(f"\nNorma průměrného embeddingu: {avg_emb.norm().item():.4f}")
                print("\n💡 Co vidíte?")
                print("- Hodnoty jsou mezi cca -3 a +3")
                print("- Některé jsou blízko 0, jiné ne")
                print("- Žádná hodnota nemá 'speciální význam'")
                print("- Model používá VŠECH 768 hodnot pro reprezentaci významu!")
        
        return results


def main():
    """Hlavní funkce pro interaktivní použití."""
    print("GPT-2 Embeddings Explorer")
    print("=" * 50)
    print("\n⚠️  POZNÁMKA: Program zobrazuje VŠECH 768 hodnot embeddingů!")
    print("   Cílem je ukázat skutečnou složitost reprezentace textu v AI.")
    print("   Připravte se na HODNĚ čísel! 🔢\n")
    
    # Inicializace
    try:
        explorer = GPT2EmbeddingsExplorer()
        info = explorer.get_model_info()
        print(f"\nNačten model: {info['model_name']}")
        print(f"Velikost slovníku: {info['vocab_size']:,}")
        print(f"Dimenze embeddingů: {info['embedding_dim']}")
        print(f"Max. délka sekvence: {info['max_sequence_length']}")
    except Exception as e:
        print(f"Chyba při inicializaci: {e}")
        return
    
    # Interaktivní smyčka
    while True:
        print("\n" + "-" * 50)
        user_input = input("\nZadejte text k analýze (nebo 'q' pro ukončení): ")
        
        if user_input.lower() == 'q':
            print("Ukončuji program.")
            break
        
        if not user_input.strip():
            print("Prázdný vstup, zkuste znovu.")
            continue
        
        try:
            explorer.analyze_text(user_input, show_details=True)
        except Exception as e:
            print(f"Chyba při analýze: {e}")


if __name__ == "__main__":
    main()