from Data_loader import load_data
from Data_filter import filter_data
from Function_file import dataStatistics, dataPlot
#from Option_helper import filter_data,load_data
import numpy as np 

if __name__ == '__main__':
    
    matrix = np.zeros(0)
    restricted_matrix = np.zeros(0)
    
    while True:
        
        try:
            user_input = int(input('Please insert a number from 1 to 5: \n'+
                                    '[1] LoadData\n' +
                                    '[2] Filter data\n' +
                                    '[3] Display statistics\n' +
                                    '[4] Generate plots\n' +
                                    '[5] Quit\n'))
            if user_input> 5 or user_input < 1 :
                raise ValueError('Please select a number from the filter menu')
        except:
             
            print("Please insert a number in the selected range")
       
            continue
        if user_input == 5:
            break

        if user_input == 1: #LoadData to analise
            
            matrix = load_data()
            restricted_matrix = np.copy(matrix)

            
        elif user_input == 2: # filter data
            if len(matrix)== 0 :
                print("Please load data before continuing")
            else:
                restricted_matrix = filter_data(restricted_matrix, matrix)
        elif user_input == 3: #display Statistics in the selected range
            if len(matrix)== 0 :
                print("Please load data before continuing")
            else:
                statistic = ["Mean Temperature",
                    "Mean Growth rate","Std Temperature","Std Growth rate","Rows","Mean Cold Growth rate",
                    "Mean Hot Growth rate\n"]
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
            
    print('Quit programme')
    
