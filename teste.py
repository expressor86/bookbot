text = "Teste de prova @ 134.!"


char_counts = {}
    
    # Converte o texto para minúsculas
text = text.lower()
print(text)
    
    # Conta cada caractere
for char in text:
    if char in char_counts:
        char_counts[char] += 1
        
    else:
        char_counts[char] = 1
        
print(char_counts)

    

