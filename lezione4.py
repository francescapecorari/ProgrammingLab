#creo un oggetto 
class CSVfile():
    def __init__(self, name):
      
        #do il nome 
        self.name = name
    
    def get_data(self):
        data = []
        file_csv = open('shampoo_sales.txt', 'r')

        for line in file_csv:
            line = line.strip('\n')
            elemento = line.split ()

            if (elemento[0]!= 'Date'):
                data.append (elemento)
        
        file_csv.close()

        return data

my_file = CSVfile('shampoo_sales.txt')

print(my_file)
print(my_file.name)
print(*my_file.get_data(), sep='\n')





