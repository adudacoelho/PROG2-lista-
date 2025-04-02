
def main():

    lst = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
    
    print(lst)
    for i in range(0, len(lst)-1):
        for j in range(i+1, len(lst)):
            c = lst[i] * lst[j]
            if c in lst:
                print(lst[i], "x", lst[j], "=", c) # "%3d"

main()
