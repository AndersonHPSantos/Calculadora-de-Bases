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

def despedida():
    print("Obrigado por utilizar o programa!")
# Menu
print("Bem-vindo")
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
                print("({})10 = ({}){}" .format(valor, Dec2(valor, base), base))
            # Chamada para repetição
            resp = input("Deseja continuar(S/N)?: ")
    case 2:
        # demais bases para decimal
        print("Em breve")
    case _:
        # Comando inválido
        print("Opção inválida!")
# Despedidas
if(op1 != 0):
    despedida()