# CalculadoraDeBases
# Função de conversão de decimal para demais bases
def Dec2(dec, base):
    listaVal = []  # Vetor o qual será armazenado o resto da(s) divisão(ões).
    quociente = 0
    resto = 0
    while dec > 0:
        # Obtendo o quociente e o produto da divisão 
        quociente = dec//base
        resto = dec%base
        # Adicionando o valor do resto ao final do vetor
        if(base == 16):
            resto = conv2hex(resto)
            listaVal.append(resto)
        else:
            listaVal.append(resto)
        # Atualizando o valor do decimal
        dec = quociente
    listaVal.reverse() # Invertendo as posições 
    # Transformando em número inteiro
    conv = 0 # Variável a qual armazenará o valor convertido
    if(base == 16):
        # Array para String
        conv = ''.join(listaVal)
    else:
        n = len(listaVal)
        for i in range(n):
            conv += listaVal[i] * 10**(n-(i+1))
    return(conv)

def conv2hex(resto):
    conversao = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    return conversao.get(resto, str(resto))

def conv2hexII(digito):
    conversao = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    return conversao.get(digito, str(digito))

# Função de Conversão de demais bases para decimal
def Base2(base, valor):
    conv = 0
    vetor = []
    for digito in str(valor).upper():
        if '0' <= digito <= '9':
            vetor.append(int(digito))
        elif 'A' <= digito <= 'F':
            vetor.append(conv2hexII(digito))
        else:
            raise ValueError("Digito inválido para a base {}" .format(base))

    n = len(vetor)-1
    for i in range(len(vetor)):
        conv += vetor[i] * (base**n)
        n -= 1
    return(conv)

def linhas(tam = 50):
    return '-' * tam

def simbolos(base):
    subscritos = {
    2: '\u2082',
    8: '\u2088',
    16: '\u2081\u2086',
    10: '\u2081\u2080'
    }
    return subscritos.get(base, "Não suportado")

def despedida():
    print("Obrigado por utilizar o programa!")
# Menu

print(linhas())
print("Bem-vindo".center(50))
print(linhas())

op1 = int(input("Qual o tipo de conversão deseja realizar?\n"
        "[1] Decimal para demais bases\n"
        "[2] Demais bases para decimal\n"
        "[0] Sair\n"))
match op1:
    case 0:
        despedida()
    case 1:
        # Decimal para demais bases
        resp = 'S'
        while(resp.upper() == 'S'):
            valor = int(input("Digite o número decimal: "))
            base = int(input("Digite a base para conversão: \n"
            "[2]  Binário\n"
            "[8]  Octal\n" + 
            "[16] Hexadecimal\n"))
            if(base != 2 and base!= 8 and base != 16):
                print("Opção inválida")
            else:
                print("({}){} = ({}){}" .format(valor, simbolos(10), Dec2(valor, base), simbolos(base)))
            # Chamada para repetição
            resp = input("Deseja continuar(S/N)?: ")
    case 2:
        # demais bases para decimal
        resp = 'S'
        while(resp.upper() == 'S'):
            base = int(input("Qual será a base do número digitado?: \n"
                "[2]  Binário\n"
                "[8]  Octal\n"
                "[16] Hexadecimal\n"))
            if(base != 2 and base!= 8 and base != 16):
                print("Opção inválida")
            else:
                if(base == 16):
                    valor = input("Digite o valor da base 16: ")
                    valor = valor.upper()
                else:
                    valor = int(input("Digite o valor de base {}: " .format(base)))
                if(base == 8 and 8<= valor <=9):
                    raise ValueError("Não os valores 9 e 8 na base 8!")
                else:
                    print("({}){} = ({}){}" .format(valor, simbolos(base), Base2(base, valor), simbolos(10)))
            # Chamada para repetição
            resp = input("Deseja continuar(S/N)?: ")
    case _:
        # Comando inválido
        print("Opção inválida!")
# Despedidas
if(op1 != 0):
    despedida()