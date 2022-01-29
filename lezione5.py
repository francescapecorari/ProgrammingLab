#classe per il file CSV
class CSVfile():
    def __init__(self, name):
      
        #do il nome 
        self.name = name
        #provo ad aprirlo e leggere una riga
        self.can_read = True
        try: file_csv open(self.name, 'r')
            file_csv.readline()
        except Exception as e:
            self.can_read:
            print('errore di apertura del file: "{}"'.format(e))
    
    def get_data(self):

      # Se nell'init ho settato can_read a False vuol dire che
       # il file non poteva essere aperto o era illeggibile
        if not self.can_read:
            print('errore, file non aperto o illeggibile')
        #esco dalla funzione
        return none
        
       else:
        #inizializzo una lista vuota per salvare i valori    
        data = []
        #apro il file
        file_csv = open('shampoo_sales.txt', 'r')
        #leggo il file riga per riga
        for line in file_csv:
           #"ripulisco" le righe dagli spazi
            line = line.strip('\n')
           #faccio lo split delle righe sulla virgola
            elemento = line.split (',')
           #non sto processando l'intestazione
            if (elemento[0]!= 'Date'):
              #aggiungo gli elementi alla lista
                data.append (elemento)
        #chiudo il file
        file_csv.close()
        #ritorno i dati quando ho processato tutte le righe
        return data

#Corpo del programma
my_file = CSVfile(name = 'shampoo_sales.txt')

print('Nome del mio file: "{}"'.format(my_file.name)
print(my_file.name)
print(*my_file.get_data(), sep='\n')










