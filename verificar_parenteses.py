def verificar_parenteses(expressao):
    pilha = []
    
    for caractere in expressao:
        if caractere == '(':
            pilha.append('(')
        elif caractere == ')':
            if not pilha:
                return False  # Encontrou ')' sem um '(' correspondente
            pilha.pop()
            
    # Se a pilha estiver vazia, todos os parênteses foram fechados corretamente
    return len(pilha) == 0

# Testes solicitados
testes = ["((A+B) * C)", "(A+B))", "((A+B)"]

for t in testes:
    resultado = "Válido" if verificar_parenteses(t) else "Inválido"
    print(f"{t} -> {resultado}")