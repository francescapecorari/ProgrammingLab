def somma_lista(my_list):
    somma=0

    for item in my_list:
        somma = somma + item

    return somma

my_list = [1,2,3,4,5,6,7]
        
print("Somma lista: {}". format(somma_lista(my_list)))       





