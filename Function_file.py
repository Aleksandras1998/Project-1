import numpy as np
import matplotlib.pyplot as plt

#Function №.1 - Data load function
def dataLoad(filename):
    
    #Importing txt file
    
    try:
        data=np.loadtxt(filename)
        print(chr(95)*47)
        print(f'Data loaded successfully from {filename}')
        print(chr(8254)*47)
    
    except:
        if not filename.endswith('.txt'): #Check file data type
            print()
            print(f'{filename} needs to have .txt extension')
            print(f'Error loading data from {filename}. Please try again')
        
        return None
        
    #Creating dictionary that assign the numeric code to bacteria
    bacteria_dict = {
    1: 'Salmonella enterica',
    2: 'Bacillus cereus',
    3: 'Listeria',
    4: 'Brochothrix thermosphacta'
}
    #Creating empty matrix N x 3
    matrix=np.empty([0,3])
    #print(matrix)
    
    print('Description of error:')
    
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


#Function №.2 - Data statistics function
def saveData(filename, matrix):
    
    #Save the matrix data to a new text file
    np.savetxt(filename, matrix,fmt='%g')

def dataStatistics(data, statistic):
    
    statsdata = data
       
    #Creating if statements for stats calculations
    if statistic == "Mean Temperature":
        return np.mean(statsdata[:,0])
        
    if statistic == "Mean Growth rate":
        return np.mean(statsdata[:,1])
        
    if statistic == "Std Temperature":
        return np.std(statsdata[:,0])
        
    if statistic == "Std Growth rate":
        return np.std(statsdata[:,1])
        
    if statistic == "Rows":
        return len(statsdata[:,0])
        
    if statistic == "Mean Cold Growth rate":
        Coldgrowthrates=[]
        for i in range(len(statsdata[:,0])):
            if statsdata[i,0]<20:
                Coldgrowthrate=[statsdata[i,1]]
                Coldgrowthrates.append(Coldgrowthrate)
        Coldgrowthrates=np.vstack(Coldgrowthrates)
        return np.mean(Coldgrowthrates)
            
        
    if statistic == "Mean Hot Growth rate":
        Hotgrowthrates=[]
        for i in range(len(statsdata[:,0])):
            if statsdata[i,0]>50:
                Hotgrowthrate=[statsdata[i,1]]
                Hotgrowthrates.append(Hotgrowthrate)
        return np.mean(Hotgrowthrates)


#Function №.3 - Data plot function
def dataPlot(data):
    #Plotting
    
    '''with open('Filtered bacteria data.txt', 'r') as data:
    # Read file contents
     filein = data.read()
    statsdata=np.loadtxt(filein)'''   

    statsdata=data                      
    # Creating a figure with two subplots
    fig,axs=plt.subplots(2,1,figsize=(12,6))
    
                                    #1st Plot
    
    first_count=0
    second_count=0
    third_count=0
    fourth_count=0
    Bacteria_name = np.array(['Salmonella\nenterica', 'Bacillus\ncereus',\
                              'Listeria', 'Brochothrix\nthermosphacta'])
    x=Bacteria_name
    #print(x)
    
    #Creating loop to counts how many bacterias of different type we have
    
    for j in range(len(statsdata[:,0])):
        
        if statsdata[j,2] == 1:
            first_count+=1
        elif statsdata[j,2] == 2:
            second_count+=1
        elif statsdata[j,2] == 3:
            third_count+=1
        elif statsdata[j,2] == 4:
            fourth_count+=1
        y=np.array([first_count,second_count,third_count,fourth_count])
        
    # First sublot - bacteria counts
     
    axs[0].bar(x,y)
    axs[0].set_title('Number of bacteria')
    axs[0].set_xlabel('Name of bacteria')
    axs[0].set_ylabel('Counts')
  
                                    #2nd Plot.
    
    
    #Creating empty vector for x-axis
    x1=[]
    x2=[]
    x3=[]
    x4=[]
    
    
    #Creating empty vector for y-axis
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    
    #Creating loop for temperature and growth rate for each bacteria type
    
    for k in range(len(statsdata[:,0])):
        if statsdata[k,2] ==1:
            x1.append(statsdata[k,0]) #Temperature of bacteria Nr.1
            y1.append(statsdata[k,1]) #Growth rate of bacteria Nr.1
    #print(x1)
    #print(y1)
        elif statsdata[k,2] ==2:
            x2.append(statsdata[k,0])
            y2.append(statsdata[k,1])
    #print(x2)
    #print(y2)
        elif statsdata[k,2] ==3:
            x3.append(statsdata[k,0])
            y3.append(statsdata[k,1])
    #print(x3)
    #print(y3)
        elif statsdata[k,2] ==4:
            x4.append(statsdata[k,0])
            y4.append(statsdata[k,1])
    #print(x4)
    #print(y4)
    
    #Defining different colors for each bacteria
    color1='green'
    color2='blue'
    color3='red'
    color4='purple'
    
    #Defining different marker for each bacteria
    marker1='o'
    marker2='s'
    marker3='^'
    marker4='d'
    
    # Second subplot. temperature-growth rate scatter plot for 4 bacteria types
    axs[1].scatter(x1, y1, color=color1, marker=marker1, label='Salmonella enterica')
    axs[1].scatter(x2, y2, color=color2, marker=marker2, label='Bacillus cereus')
    axs[1].scatter(x3, y3, color=color3, marker=marker3, label='Listeria')
    axs[1].scatter(x4, y4, color=color4, marker=marker4, label='Brochothrix thermosphacta')
    axs[1].set_xlabel('Temperature')
    axs[1].set_ylabel('Growth rate')
    axs[1].legend()
    
    # show the figure
    plt.show()
    
    #dataPlot(data)
    return (dataPlot)
    


    
