from Data_loader import load_data
from Data_filter import filter_data
from Function_file import dataStatistics, dataPlot
#from Option_helper import filter_data,load_data
import numpy as np 

if __name__ == '__main__':

#==============================================================================
                    #Creating main menu for user input
    
    matrix = np.zeros(0)
    restricted_matrix = np.zeros(0)
    data_loaded=False
    
    while True:                                                                 
        
        try:
            user_input = int(input('Enter a number from 1 to 5: \n'+
                                    '[1] LoadData\n' +
                                    '[2] Filter data\n' +
                                    '[3] Display statistics\n' +
                                    '[4] Generate plots\n' +
                                    '[5] Quit\n'+
                                    '>>'))
            if user_input> 5 or user_input < 1 :
                print()
                print('+'+'-'*40+'+')
                print('|' + ' '*16 + 'WARNING!' + ' '*16 + '|')
                raise ValueError('|' + ' ' + 'Please select a number from main menu' + ' '*2 + '|')
        except ValueError as e:
            print(e)
            print('+' + '-'*40 + '+')
       
            continue
#==============================================================================        
        # matrix=np.zeros(0)
        # restricted_matrix=np.zeros(0) 
        #This code linescannot be inside while loop, 
        #since they are only executed if the user enters an invalid value for 
        #'User_input' and the 'continue' statement is executed. 
#==============================================================================

                    #[1]st selection-Uploading data
                            
        if user_input == 1: #LoadData to analise
            #print(matrix)
            matrix = load_data() #matrix comes from load_data function
            #print(matrix)
            restricted_matrix = np.copy(matrix) #making copy of this matrix
            data_loaded=True

#==============================================================================

                    #[2]nd selection - Filtering part
           
        elif user_input == 2:
            #print(matrix)
            #print(restricted_matrix)
            #if len(matrix)== 0 : # checking if data was uploaded
            if not data_loaded:
                print("Please load data before continuing") #if not, print
            else:
                restricted_matrix = filter_data(restricted_matrix, matrix) #result come from function filter_data
#==============================================================================

                    #[3]rd selection - display statistics
                
        elif user_input == 3: 
            if len(matrix)== 0 :
                print("Please load data before continuing")
            else:
                statistic = ["Mean Temperature",
                    "Mean Growth rate","Std Temperature","Std Growth rate","Rows","Mean Cold Growth rate",
                    "Mean Hot Growth rate"]
                while True:
                    user_inputstatistics = int(input('Please select what statistical function to display\n'+
                                    "[1] Mean Temperature\n" +
                                    "[2] Mean Growth rate\n" +
                                    "[3] Std Temperature\n"  +
                                    "[4] Std Growth rate\n"  +
                                    "[5] Rows\n"+
                                    "[6] Mean Cold Growth rate\n" +
                                    "[7] Mean Hot Growth rate\n"+
                                    "[8] Exit\n"))
                
                    if 0 < user_inputstatistics <= 7: 
                        print(dataStatistics(restricted_matrix, statistic[user_inputstatistics - 1] ))
                        print(f"{statistic[user_inputstatistics - 1]} Statistics in selected range")
                        print(dataStatistics(matrix, statistic[user_inputstatistics - 1] ))
                        print(f"{statistic[user_inputstatistics - 1]} Statistics for complete dataset")
                        input('Press Enter to return to menu ...\n')
                    elif user_inputstatistics == 8 :
                        break
                    else:
                        print("Please select an existing statistical function")
            

        elif user_input == 4: #Generate plots
            if len(matrix)== 0 :
                print("Please load data before continuing")
            else:
                plot_data = dataPlot(restricted_matrix)
        
        if user_input == 5:
            print('Quit programme')
            break
            
    
    
