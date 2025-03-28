def maior(lsta):
    
    num_maior = lsta[0]
   
    for i in range (len(lsta)):
       if (lsta[i] > num_maior):
           num_maior = lsta[i]
      
    return num_maior 
           
def menor(lsta):

    num_menor = lsta[0]

    for i in range (len(lsta)):
       if (lsta[i] < num_menor):
           num_menor = lsta[i]

    return num_menor

def main():

    lsta = [20, 39, 15 , 50, 78, 43, 200, 54, 2, 3 ,4 ,5, 2]

    
    print(lsta)
    num_maior = maior (lsta)
    num_menor = menor (lsta)
    print("O número maior é:", num_maior)
    print("O número menor é:", num_menor )

main()