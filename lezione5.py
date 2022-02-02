#classe per il file CSV
class CSVfile():
    def __init__(self, name):
      
        #do il nome 
        self.name = name

        
        #provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            file_csv = open(self.name, 'r')
            file_csv.readline()

        except Exception as e:
            self.can_read = False
            print('errore di apertura del file: "{}"'.format(e))
    
    def get_data(self):

      # Se nell'init ho settato can_read a False vuol dire che
       # il file non poteva essere aperto o era illeggibile
        if not self.can_read:
            
            print('errore, file non aperto o illeggibile')
        #esco dalla funzione
            return None
        
        else:
        #inizializzo una lista vuota per salvare i valori 
            data = []

            #apro il file
            file_csv = open(self.name, 'r')
        
            #leggo il file riga per riga
            for line in file_csv:
           
                #"ripulisco" le righe dagli spazi
                line = line.strip('\n')

                #faccio lo split delle righe sulla virgola
                elemento = line.split (',')

                #pulisco il carattere di newline dall'ultimo elemento con la funzione strip()
                elemento[-1]= elemento[-1].strip()

                #non sto processando l'intestazione
                if elemento[0]!= 'Date':
                    #aggiungo gli elementi alla lista
                    data.append (elemento)
        
            #chiudo il file
            file_csv.close()

            #ritorno i dati quando ho processato tutte le righe
            return data

#estendo la classe CSVfile a NumericalCSVFile
class NumericalCSVFile(CSVfile):

    def get_data(self):
        
        #chiamo la get_data del genitore
        string_data=super().get_data()

        #preparo una lista per contenere i valori in formato numerico
        numerical_data=[]

        for string_row in string_data:
            #preparo una lista di supporto per salvare la riga in "formato" numerico
            numerical_row=[]

            #ciclo su tutti gli elementi della riga con un enumeratore così ho anche l'indice "i" di posizione dell'elemento nella riga
            for i, element in enumerate(string_row):
        
                if i==0:
                    #il primo elemento della riga lo lascio in forma stringa
                    numerical_row.append(elemento)

                else:
                    #converto a float tutti gli altri e se fallisco stampo un messaggio di errore e salto la riga
                    try:
                        numerical_row.append(float(elemento))

                    except Exception as e:
                        print('Errore di conversione del valore "{}" a valore numerico: "{}"'.format(elemento, e)
                        break

        #aggiungo la riga in formato numerico alla lista "esterna", ma solo se ho processato tutti gli elementi. Qui controllo per la lunghezza, ma avrei anch potuto usare una variabile di suporto o fare due break in cascata
        if len(numerical_row) == len(string_row):
            numerical_data.append(numerical_row)

    return numerical_data            

            
        
#Corpo del programma
my_file = CSVfile(name = 'shampoo_sales.txt')

print('Nome del mio file: "{}"'.format(my_file.name))
print('Dati contenuti nel mio file: "{}"'.format(my_file.get_data())

my_numerical_file= NumericalCSVFile(name= 'shampoo_sales.txt')
print('Nome del file: "{}"'.format(my_numerical_file.name))
print('Dati contenuti nel file: "{}"'.format(my_numerical_file.get_data()))










