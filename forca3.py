
def mostrarErro0():

    print("""
__________
|       |
|
|
|
|
|
|
|
|
|    """)

def mostrarErro1():

    print("""
__________
|       |
|      ...
|     '0 0'
|      \*/
|
|
|
|
|
|    """)

def mostrarErro2():
    print("""
__________
|       |
|      ...
|     '0 0'
|      \*/
|  *****
|
|
|
|
|    """)

def mostrarErro3():
    print("""
__________
|       |
|      ...
|     '0 0'
|      \*/
|  ***** *****
|
|
|
|
|  """)

def mostrarErro4():
    print("""
__________
|       |
|      ...
|     '0 0'
|      \*/
|  ****( )*****
|      / \\
|
|
|
|    """)

def mostrarErro5():
    print("""
__________
|       |
|      ...
|     '0 0'
|      \*/
|  ****( )*****
|      / \\
|      *
|     *
|    *
|    """)

def mostrarErro6():
    print("""
__________
|       |
|      ...
|     '0 0'
|      \*/
|  ****( )*****
|      / \\
|      * *
|     *   *
|    *     *
|    """)

def mostrarErro7():
    print("""
__________
|       |
|      ...
|     '- -'
|      \@/
|  ****( )*****
|      / \\
|      * *
|     *   *
|    *     *
|    """)

def mostrarVitoria():
    print("""


      (0 0)
 —oOO– (_)—–.
╔═══════════════════╗
║ParabénsVocê venceu║
╚═══════════════════╝
‘———————————————-oOO
……..|__|__|
………. || ||
……. ooO Ooo""")

bancoDePalavras = ["asfalto", "geladeira", "tapete", "refrigerador"]
dica = ['Rua', 'Cozinha', 'Limpar os pés', 'Congelar']

from random import randint
num = randint(0,len(bancoDePalavras)-1)

palavra = bancoDePalavras[num]
espaco = ['_']*len(palavra)
errado = 's'
letrascertas = [' ']*len(palavra)
letraserradas = []
saida = 0
certas = 0

while saida < 7:

    if saida == 0:
        mostrarErro0()

    if saida == 1:
        mostrarErro1()

    if saida == 2:
        mostrarErro2()

    if saida == 3:
        mostrarErro3()

    if saida == 4:
        mostrarErro4()

    if saida == 5:
        mostrarErro5()

    if saida == 6:
        mostrarErro6()
    print('|    ',' '.join(letrascertas))
    print('|___ ',' '.join(espaco))
    print('As letras erradas são',', '.join(letraserradas))
    print ('Dica', dica[num])

    repetiu = 'n'
    letra = input('Digite um letra: ')
    for x in letrascertas:
        if letra == x:
            repetiu = 's'
    p = 0
    for valor in palavra:
        if valor == letra:
            letrascertas[p] = letra
            if repetiu == 'n':
                certas += 1
            errado = 'n'
            if certas == len(palavra):
                saida = 8
        p += 1
    if errado == 's':
        letraserradas.append(letra)
        saida += 1
    if errado == 'n':
        errado ='s'
    if saida == 7:
        mostrarErro7()
    if saida == 8:
        mostrarVitoria()
