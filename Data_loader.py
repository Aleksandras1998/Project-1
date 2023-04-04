from Function_file import dataLoad

def load_data():
    while True:
        try:
            filename = input('┏' + '━'*41 + '┓\n'+
                             '┃ Please insert file name and upload file ┃\n'+
                             '┗' + '━'*41 + '┛\n>>')
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