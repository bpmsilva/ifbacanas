import getpass

FORCA_1 = \
'''
----
|  |
|
|
|
----
'''

FORCA_2 = \
'''
----
|  |
|  o
|
|
----
'''

FORCA_3 = \
'''
----
|  |
|  o
|  |
|
----
'''

FORCA_4 = \
'''
----
|  |
|  o
| /|
|
----
'''

FORCA_5 = \
'''
----
|  |
|  o
| /|\\
|
----
'''

FORCA_6 = \
'''
----
|  |
|  o
| /|\\
| /
----
'''


FORCA_7 = \
'''
----
|  |
|  O
| /|\\
| / \\
------
'''

print(FORCA_1)
print(FORCA_2)
print(FORCA_3)
print(FORCA_4)
print(FORCA_5)
print(FORCA_6)
print(FORCA_7)

while True:
    p1 = getpass.getpass('Entre com a palavra: ')
    p2 = getpass.getpass('Digite a palavra novamente: ')

    # Comparar a palavra p1 com a palavra p2
    if p1 == p2:
        print('Vamos começar o jogo!')
        break
    else:
        print('Palavras não são iguais')
