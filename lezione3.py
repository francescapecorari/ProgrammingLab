#definisco una funzione somma
def somma_valori (values): 
    somma=0

    for item in values:
      somma = somma + item

    return somma
#inizializzo una lista per salvare i valori
values = []
#apro il file in modalità lettura e lo stampo a schermo
my_file = open('shampoo_sales.txt','r')

#devo ricavare i valori delle vendite separandoli dalle date
for line in my_file:

    element = (line.split (','))

#devo togliere la linea con l' intestazione
    if element[0] != 'Date' and element[1]!= 'Sales':
        data = element[0]
        value = element[1]

#aggiungo i valori delle vendite alla lista
        values.append(float(value))

#provo a stampare la lista
print("valori: {}".format(values))

#sommo i valori richiamando la funzione
print("Somma_valori_vendite: {} ".format (somma_valori(values)))

        

      
