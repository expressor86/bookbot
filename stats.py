
#conta as palavras
def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    # Inicializa um dicionário vazio
    char_counts = {}
    
    # Converte o texto para minúsculas
    text = text.lower()
    
    
    # Conta cada caractere
    for char in text:
        if char == " ":
            char_counts[char] = 0
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    char_counts = dict(sorted(char_counts.items(), key = lambda x:x[1], reverse=True))
    return char_counts