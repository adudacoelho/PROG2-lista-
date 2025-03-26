import random 

def eh_primo(num):
    if num == 1 :
        return False
    
    cont_div_exatos = 0
    for d in range (1, num + 1):
        if (num % d) == 0:
            cont_div_exatos += 1

    return cont_div_exatos == 2 
        
def extrai_primos(l):
    l_primos = []

    for elem in l:
        if eh_primo(elem):
            l_primos.append(elem)
    return l_primos

def main():
    lst = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 20, 10 , 11 , 12 ,13 ,14 ,15 ,16 ,17 ,18, 19 ,20]
    lst_primos = extrai_primos(lst)
    
    print(lst)
    print(lst_primos)

main()
