def num_consoantes(name):
    cont_consoante = 0
    for char in name:
        if char.isalpha() and (char not in [ a, A, e, E , i , I, o , O, u , U]):
           cont_cons = cont_cons + 1
    return cont_cons

def main():
    lst_nomes = []

    nome = input("Entre com o nome: ")
    while nome != "":
        lst_nomes.append(nome)
        nome = input("Entre com o nome: ")

    for nome in lst_nomes:
        print(nome, num_consoante(nome))

main()
