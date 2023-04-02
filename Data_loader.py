from Function_file import dataLoad

#Loading primary filtered data 
def load_data():
    filename = input('Please insert file name and upload file:\n>>')
    matrix = dataLoad(filename)
    if len(matrix) == 0:
        print("Data has not been loaded yet. Please load data first.")
    
    return matrix
