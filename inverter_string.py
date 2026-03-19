def inverter_string(palavra):
    pilha = []
    
    # Passo 1: Empilhar cada caractere
    for caractere in palavra:
        pilha.append(caractere)
    
    palavra_invertida = ""
    
    # Passo 2: Desempilhar até a pilha esvaziar
    while len(pilha) > 0:
        palavra_invertida += pilha.pop()
        
    return palavra_invertida

# Teste
entrada = "ALGORITMO"
saida = inverter_string(entrada)
print(f"Entrada: {entrada}")
print(f"Saída Esperada: {saida}")