from data_utils import dataLoad, dataPlot, dataStatistics
#from option_helper import filter_data,load_data
import numpy as np 



#Filtering part by it's bacteria type, growth rate, or both. Obtained matrix 
#will be used to do statistical calculations
def filter_data(restricted_matrix, matrix):
    while True:
        try:
            user_input_filterdata = int(input('Please insert a number from 1 to 5 \n'+
                                    '[1] Filter Bacteria type\n' +
                                    '[2] Filter growth rate\n' +
                                    '[3] Reset\n' +
                                    '[4] Return to main menu\n'))
            if user_input_filterdata > 4 or user_input_filterdata < 1:
                raise ValueError('Please select a number from the filter menu')
        except:
             
            print("Please insert a number in the selected range")
       
            continue
        if user_input_filterdata == 1:
            bacteria_dict = {
                        1: 'Salmonella enterica',
                        2: 'Bacillus cereus',
                        3: 'Listeria',
                        4: 'Brochothrix thermosphacta'
                    }
            while True:
                user_inputBacteriatype = int(input(f'Please select a Bacteria type\n'+
                                                    f'[1] = {bacteria_dict[1] }\n' +
                                                    f'[2] = {bacteria_dict[2] }\n' +
                                                    f'[3] = {bacteria_dict[3] }\n' +
                                                    f'[4] = {bacteria_dict[4] }\n' +
                                                    f'[5] Quit current menu\n'))
                if user_inputBacteriatype not in restricted_matrix:
                    print("Please select existing Bacteria type")
                    continue
                elif user_inputBacteriatype == 5:
                    break

                restricted_matrix = np.array([row for row in restricted_matrix if row[2] == user_inputBacteriatype])
                break 
        elif user_input_filterdata == 2:
            while True :
                user_inputGrowthrate = input('Please select a valid Growth rate range (dec-dec)\n')
                user_inputGrowthrate = user_inputGrowthrate.split("-")
                lowerBound = float(user_inputGrowthrate[0])
                upperBound = float(user_inputGrowthrate[1])
                        # Create a mask for rows within the growth rate range
                mask = np.logical_and(restricted_matrix[:, 1] >= lowerBound, restricted_matrix[:, 1] <= upperBound)
                if np.any(mask):
                    restricted_matrix = restricted_matrix[mask, :]
                    break
                        # Create a smaller matrix with only the rows within the growth rate range
                            # Print the original and restricted matrices
                            #print('Original matrix:\n', matrix)
                            #print('Restricted matrix:\n', restricted_matrix)
                            ##Save the restricted matrix data to a new text file
                            #np.savetxt(restricted_matrix,fmt='%g')
                else: 
                    print("Please input existing Growth rate range ")
                    continue
        elif user_input_filterdata == 3:
            restricted_matrix = np.copy(matrix)
        elif user_input_filterdata == 4:
            return restricted_matrix
         
#____________________________

#Loading primary filtered data 
def load_data():
    filename = input('Please insert file name and upload file\n')
    matrix = dataLoad(filename)
    if len(matrix) == 0:
        print("Data has not been loaded yet. Please load data first.")
    
    return matrix

#_______________________________



if __name__ == '__main__':
    matrix = np.zeros(0)
    restricted_matrix = np.zeros(0)

    while True:
        
        try:
            user_input = int(input('Please insert a number from 1 to 5 \n'+
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
    

#In statistics part: by using filter function nad filtering based on the bacteria type, 
#by selecting Salmonella entrica it returns me back to the previous menu. Same issue with filter growth rate.

#There should be function, that let us to choose several types of bacteria and filter them 
#based on the temperature or growth rate. Also, we could find specific range of min/max values of each parameter
#and ask user to enter only the interval between min and max values (min<value<max)

#In the filter option Nr.2, when we chose to filter by the criteria 'Filter bacteria type'
#After we get the same option menu, have the comment 'Data was filtered using 'filter bacteria type''
#Continue if you want-chose filter growth rate, if not return to main menu.

#When we are in main menu, and we already filtered data, if we enter 4 it doesn't generate plot
#Generate code doesn't work
 