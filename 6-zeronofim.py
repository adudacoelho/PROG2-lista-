def zeroNoFim(lsta):
    
#def zeroNoFim(lsta):
    count_zero = 0  # Conta a quantidade de zeros na lista
    for i in range(len(lsta)):
        if lsta[i - count_zero] == 0:  # Ajuste para a movimentação da lista
            lsta.insert(len(lsta), 0)  # Insere um zero no final da lista
            del lsta[i - count_zero]  # Remove o zero da posição original
            count_zero += 1  # Atualiza o contador de zeros movidos
    return lsta

def main():
    lsta = [10, 20, 30, 0, 40, 50, 60, 0, 70, 0, 80, 90, 100]
    lstb = zeroNoFim(lsta)

    print(lsta)
    print(lstb)
main()