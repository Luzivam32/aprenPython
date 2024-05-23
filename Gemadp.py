#Gerenciamento de Memória arquivos e depuração de programas
print("Alo, mundo")
#Tipos Mútaveis
'''
#Tipos não Mútaveis
print('O tipo int, bool, float, str e complex é não mútaveis')
a = 3
b = 3.0
c = 'hello'

d = [2, 3, 5, 8, 11]
print("troco o 8 por 7")
print("list são Mútaveis")
d[3] = 7
# Mudou o valor de 'a'
a = 6
b = a
print(" a duas variaveis aponta pro mesmo volor", a,"e", b)
print(a,b,c,d)

a = [3,4,5]
b = a
def h(lst):
    lst[0]=5

mylist = [3,6,9,12]
print(h(mylist))'''
def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)
n_words, n_char = readFile('teste.txt')

