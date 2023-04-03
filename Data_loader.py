from Function_file import dataLoad

# def load_data():
#     while True:
#         filename = input('Please insert file name and upload file:\n>>')
#         matrix = dataLoad(filename)
#     if matrix is not None and len(matrix)>0:
#         #print("Data has not been loaded yet. Please load data first.")
    
#         return matrix

def load_data():
    while True:
        try:
            filename = input('Please insert file name and upload file:\n>>')
            matrix = dataLoad(filename)
            
            if matrix is not None:
                # File loaded successfully, so break out of the while loop
                break
            else:
                # File not loaded successfully, so continue the while loop
                continue
            
        except:
            print(f'Error loading data from {filename}. Please try again')
    
    return matrix