import numpy as np

def dataLoad(filename):
    
    #Importing txt file 
    filein=filename
    
    #Loading the data from the file into numpy array
    data=np.loadtxt(filein)
    
    #Creating dictionary that assign the numeric code to bacteria
    bacteria_dict = {
    1: 'Salmonella enterica',
    2: 'Bacillus cereus',
    3: 'Listeria',
    4: 'Brochothrix thermosphacta'
}
    
    #Creating empty matrix N x 3
    matrix=np.empty([0,3])
    print(matrix)
    
    #Creating the loop which read the rows of the data 
    for i in range(len(data[:,0])):
        #print(i)
        if (10<=data[i,0]<=60) and data[i,1]>0 and data[i,2] in bacteria_dict:
            rows=[data[i,0],data[i,1],data[i,2]]
            #print(rows)
            matrix = np.vstack([matrix, rows])
        else:
            if not(10<=data[i,0]<=60):
                print(f"Sample {i+1} has invalid temperature")
            if data[i,1]<0:
                print(f"Sample {i+1} has invalid growth rate")
            if data[i,2] not in bacteria_dict:
                print(f"Sample {i+1} does not correspond to any bacteria")
                
    #Save the matrix data to a new txt file
    saveData("Filtered bacteria data.txt", matrix)
    
    return matrix

def saveData(filename, matrix):
    
    #Save the matrix data to a new text file
    np.savetxt(filename, matrix,fmt='%g')