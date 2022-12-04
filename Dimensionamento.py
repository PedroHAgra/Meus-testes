import math

comprimento = float(input('Digite o comprimento: '))
largura = float(input('Digite a largura: '))
comodo = int(input('Digite o tipo de área\n[1]Cozinha,área molhada\n[2]Área não molhada\n'))

def area(largura,comprimento):
    return largura*comprimento

def perimetro(largura,comprimento):
    return (2*comprimento)+(2*largura)

def calIluminacao(area):
    cont = 0
    if area(largura,comprimento) < 6:
        C_ilu = 100
        return f'A potencia mínima de iluminação é de {C_ilu} VA'
    else:
        newa = (area(largura,comprimento)-6)
        while(newa > 4):
            newa = newa-4
            cont += 1
            C_ilu = 100 + 60*cont
            return f'A potencia mínima de iluminação é de {C_ilu} VA'

def calTUGs(comodo):
    if comodo == 1:
        nTUG = perimetro(largura,comprimento)/3.5
        nTUG = math.ceil(nTUG)

        if nTUG < 4:
            CTUG = nTUG*600
            return f'A potência mínima para TUGs é de {CTUG}VA'
        else:
            CTUG = (nTUG-3)*100 + 1800
            return f'A potência mínima para TUGs é de {CTUG}VA'

    if comodo == 2:
        if area(largura,comprimento) < 6:
            CTUG = 100
            return f'A potência mínima para TUGs é de {CTUG}VA'
        else:
            nTUG = perimetro(largura,comprimento)/5
            CTUG = nTUG*100
            return f'A potência mínima para TUGs é de {CTUG}VA'
    
calIluminacao(area)
calTUGs(comodo)
