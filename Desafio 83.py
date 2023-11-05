def verifica_parenteses(expressao):
    pilha = [] # Usaremos uma pilha para verificar a ordem dos parênteses

    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            # Verifica se há um parêntese de fechamento sem um correspondente de abertura
            if not pilha:
                return False
            pilha.pop()

    # Se a pilha estiver vazia no final, significa que os parênteses estão corretos
    return not pilha

def main ():
    expressao = input('Digite uma exoressão com parênteses: ')
    if verifica_parenteses(expressao):
        print("Os parênteses estão corretos na expressão.")
    else:
        print("Os parênteses não estão na ordem correta na expressão.")

if __name__ == "__main__":
    main()