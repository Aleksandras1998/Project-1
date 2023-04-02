import numpy as np

def dataStatistics(data, statistic):
    
    #Importing txt file
    filein=data
    
    #Loading the data from the file into numpy array
    statsdata=np.loadtxt(filein)
       
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
        Hotgrowthrates=np.vstack(Hotgrowthrates)
        return np.mean(Hotgrowthrates)

    
