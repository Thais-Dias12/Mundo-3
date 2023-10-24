# Defina a tupla com as palavras
palavras = ("python", 
            "programaçao", 
            "Linguagem", 
            "computador", 
            "algoritmo")

# Função para encontrar e mostrar as vogais de uma palavra
def encontrar_vogais(palavras):
    vogais = [letras for letras in palavras if letras in "aeiou"]
    return vogais

# Itere sobre as palavras na tupla e mostre suas vogais
for p in palavras:
    vogais = encontrar_vogais(p)
    print(f"Palavra: {p} temos as Vogais: {', '.join(vogais)}")