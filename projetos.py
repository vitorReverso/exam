import time  # Importa o módulo time para usar a função sleep

# Inicializa as variáveis para contagem de acertos e erros
acertos = 0
erros = 0
passar = 3  # Define a quantidade de pontos necessários para passar
pontos = 57
bimestre = 60

# Solicita respostas do usuário para três perguntas
questao1 = int(input("Quanto é 2 + 2? "))
questao2 = int(input("Quanto é 3 + 3? "))
questao3 = int(input("Quanto é 9 + 9? "))

def prova():
    """
    Função para verificar as respostas e atualizar as variáveis de acertos e erros
    """
    global acertos, erros  # Permite modificar as variáveis globais dentro da função
    if questao1 == 4 and questao2 == 6 and questao3 == 18:
        acertos += 3  # Todos os acertos são corretos, então incrementa 3 acertos
    elif questao1 > 4 and questao2 == 6 and questao3 < 18:
        acertos += 1  # Apenas uma resposta correta
        erros += 2  # Duas respostas incorretas
    elif questao1 < 4 and questao2 > 6 and questao3 > 18:
        erros += 3  # Todas as respostas estão incorretas
    elif questao1 > 4 and questao2 < 6 and questao3 == 18:
        erros += 2  # Duas respostas incorretas
        acertos += 1  # Uma resposta correta
    elif questao1 == 4 and questao2 > 6 and questao3 == 18:
        acertos += 2  # Duas respostas corretas
        erros += 1  # Uma resposta incorreta
    elif questao1 < 4 and questao2 == 6 and questao3 == 18:
        acertos += 2  # Duas respostas corretas
        erros += 1  # Uma resposta incorreta
    else:
        print("Apenas inteiros.")  # Mensagem de erro para entradas inválidas

def verificaçoes():
    """
    Função para verificar se o número de acertos é suficiente para passar
    e determinar se o número de acertos é par ou ímpar
    """
    global acertos  # Permite modificar a variável global dentro da função
    if acertos == passar:
        print(f"Ele precisava de {passar} pontos.")
        for i in range(5):  # Loop para imprimir "..." com um intervalo de 1 segundo
            print("...\n")
            time.sleep(1)
        print("Ele passou")  # Mensagem indicando que o usuário passou
        time.sleep(5)  # Pausa de 5 segundos antes de prosseguir

    # Verifica se o número de acertos é par ou ímpar
    if acertos % 2 == 0:
        print("Par")  # Mensagem indicando que o número de acertos é par
    else:
        print("Ímpar")  # Mensagem indicando que o número de acertos é ímpar


login_senha = 1234
reprovar = erros - 60
def sistema():
    global passar
    dados = int(input("Insira a senha: "))
    if dados == login_senha:
        nome = input("Selecione o nome do aluno: ")
        if nome == "matheus":
            print(f"Esse aluno teve o resultado de {acertos} acertos e {erros} erros.")
            time.sleep(2)
            if acertos == passar:
                print(f"Esse aluno precisava de 60 pontos, no bimestre ele está com {pontos} pontos.")
                for _ in range(3):
                    print("Somando...")
                    time.sleep(2)
                if passar + pontos == bimestre:
                    print("Ele passou.")
                else:
                    print("Ele não passou.")
            else:
                print("Ele não passou.")
    else:
        print("Senha incorreta.")

prova()
verificaçoes()
sistema()
