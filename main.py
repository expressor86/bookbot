from stats import get_num_words, count_chars
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = sys.argv[1]
    text = get_book_text(path)
 
    #Cabeçalho

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
   

    # Chama o contador de palavras
    num_words = get_num_words(text)
    
    print("----------- Word Count ----------""\n")
    print(f"Found {num_words} total words.\n")
    print("--------- Character Count -------\n")
    
    # Conta caracteres
    char_counts = count_chars(text)
    char_counts = dict(sorted(char_counts.items(), key = lambda x:x[1], reverse=True))
    for char, valor in char_counts.items():
        print(f"{char}: {valor}")
    print("=================END====================")

# Chama a função main no final do arquivo
main()
