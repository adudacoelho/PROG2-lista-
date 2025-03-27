def calculaIntersecao(lst1, lst2):
   
   num = lst1.copy() #Posso fazer isso????
   num2 = lst2.copy()
   num3 = []

   for i in range (len(num)): 
     if num[i] in num2:
         num3.append(num[i])
    
   if len(num3) > 0:
        return num3  
   else:
        return []  
    
def main():

    lst1 = ["morango", "laranja", "abacaxi", "kiwi", "maça", "limão", "melancia", "banana"]
    lst2 = ["morango", "uva", "pera", "melancia", "abacate", "laranja", "pitaia", "banana"]
    
    print(lst1)
    print(lst2)
    
    intersecao = calculaIntersecao(lst1, lst2)  
    
    if intersecao: 
        print("Interseção:", intersecao)
    else:
        print("Não tem interseção.")
main()