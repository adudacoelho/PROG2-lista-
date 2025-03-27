def calculaUniao(lst1, lst2):
   
   num = lst1.copy() #Posso fazer isso????
   num2 = lst2.copy()
   num3 = num + num2

   uniao = []
   for elemento in num3:
        if elemento not in uniao:  
            uniao.append(elemento)
   return uniao   
    
def main():

    lst1 = ["morango", "laranja", "abacaxi", "kiwi", "maça", "limão", "melancia", "banana"]
    lst2 = ["morango", "uva", "pera", "melancia", "abacate", "laranja", "pitaia", "banana"]
    
    print(lst1)
    print(lst2)
    
    uniao = calculaUniao(lst1, lst2)  
    
    print("União:", uniao)
 
main()