

import numpy as np
import re 

#Filtering part by it's bacteria type, growth rate, or both. Obtained matrix 
#will be used to do statistical calculations
def filter_data(restricted_matrix, matrix):

#==============================================================================
                            #This is main filter menu
#==============================================================================
    while True:
        try:
            user_input_filterdata = int(input(' '*8+'┃'+ 'Data filter menu┃\n'+
                                    '┏' + '━'*36 + '┓\n'+
                                    '┃ Please insert a number from 1 to 4 ┃\n'+
                                    '┗' + '━'*36 + '┛\n'+
                                    '[1] Filter Bacteria type\n' +
                                    '[2] Filter growth rate\n' +
                                    '[3] Reset\n' +
                                    '[4] Return to main menu\n'+
                                    '>>'))
            if user_input_filterdata > 4 or user_input_filterdata < 1:
                print()
                print('+'+'-'*40+'+')
                print('|' + ' '*16 + 'WARNING!' + ' '*16 + '|')
                raise ValueError('|' + ' '*2 + 'Select a number from the filter menu' + ' '*2 + '|')
        except ValueError as j:
            print(j) 
            print('|' + ' '*12 + 'Please try again' + ' '*12 + '|')
            print('+' + '-'*40 + '+') # check main script, and do the same display window
       
            continue
#==============================================================================
                #Filtering data based on the type of bacteria
#==============================================================================              
        if user_input_filterdata == 1:
            bacteria_dict = {
                        1: 'Salmonella enterica',
                        2: 'Bacillus cereus',
                        3: 'Listeria',
                        4: 'Brochothrix thermosphacta'
                    }
# =============================================================================
#             #combined_matrix=restricted_matrix.copy()
#             combined_matrix=None
# =============================================================================
            while True:
                user_inputBacteriatype = input('┏' + '━'*29 + '┓\n'+
                                                   '┃Please select a Bacteria type┃\n'+
                                                   '┗' + '━'*29 + '┛\n'+
                                                   f'[1] = {bacteria_dict[1] }\n' +
                                                   f'[2] = {bacteria_dict[2] }\n' +
                                                   f'[3] = {bacteria_dict[3] }\n' +
                                                   f'[4] = {bacteria_dict[4] }\n' +
                                                   '[5] = Quit current menu\n'+
                                                   '>>')
                
                if user_inputBacteriatype == 5:
                    break
            
                

                #Filter the data based on the selected bacteria types
                user_inputBacteriatype = re.findall(r'\d+(?:\.\d+)?', str(user_inputBacteriatype)) #give an opportunity to enter like 0.1&0.5 or any other symbol between, and still will recognise that

                user_inputBacteriatype = [float(input) for input in user_inputBacteriatype]
                        #Create mask for rows within only the Bacteria data types
                mask = np.isin(restricted_matrix[:, 2], user_inputBacteriatype)
                if np.any(mask):
                    #create restricted matrix with  selected values for Bacteria types
                    restricted_matrix = restricted_matrix[mask, :]
                    break
#comment X alex, please delete later: i create a simila function to that for growth rate
#  and run it with the debug option( very useful by the way). I basically used that but
# with a list of floats corresponding to the user's input. in this case i used no.isin
#  because it only needs to go through the list and there is no need for the logical and
#the no.isin function i found on the internet when i was having issues with any in there. 
# the rest after is the same as x growth rate. it all works now i made a few other minor changes
#very minor but run code to see it. 
        #accept errors in typing
                else:
                    print()
                    print('+'+'-'*41+'+')
                    print('|' + ' '*17 + 'WARNING!' + ' '*16 + '|')
                    print('|' + ' '*1 + 'Please input existing Bacteria types' + ' '*1 + '|')
                    print('+' + '-'*41 + '+')
    
               
                print(restricted_matrix)
                print(f'Filtered by bacteria type: {bacteria_dict[user_inputBacteriatype]}')
               
                print('If needed, enter option [2] to apply growth rate filter')
                print('Enter option [3] to reset filtered data')
                break
            
#=============================================================================
     #Here I tried to create another option for user to filter according 
     #bacteria type several times and combine several bacteria's. 
     #Seems it doesn't work as inteded. Program uses restricted_matrix which
     #was filtered before, but doesn't take copy version of matrix. That's 
     #why if user enters next type '2', program finds in restricted_matrix
     #only data of first bacteria, and outputs message 'Please select existing Bacteria type'.
# =============================================================================
#                 filtered_matrix=np.array([row for row in restricted_matrix if row[2] == user_inputBacteriatype])
#                 print(f'Filtered by bacteria type:{bacteria_dict[user_inputBacteriatype]}')
#                 
#                 while True:
#                     if combined_matrix is None:
#                         user_input_combined_filters=input('Do you want to use this filter as the new restricted matrix? (y/n)\n')
#                     else:
#                         user_input_combined_filters=input('Do you want to combine this filter with the previous one? (y/n)\n')
#                     if user_input_combined_filters.lower()=='y':
#                         if combined_matrix is None:
#                             combined_matrix=filtere_matrix
#                             print(f'New restricted matrix: {len(combined_matrix)} rows remaining')
#                         else:
#                             combined_matrix=np.concatenate((combined_matrix,filtere_matrix))
#                             print(f'Combined filters: {len(combined_matrix)} rows remaining')
#                         break
#                     elif user_input_combined_filters.lower()=='n':
#                         restricted_matrix=filtere_matrix
#                         print('If needed, select another bacteria type or exit')
#                         break
#                     else:
#                         print('Invalid input, please enter y or n')
# 
# =============================================================================


#==============================================================================
                    #Filtering data based on the growth rate
#==============================================================================      
            
        elif user_input_filterdata == 2:
            while True :
                user_inputGrowthrate = input('┏' + '━'*51 + '┓\n'+
                                             '┃ Please select a valid Growth rate range (dec-dec).┃\n'+
                                             '┗' + '━'*51 + '┛\n'+
                                             '>>')
                                             #'Please select a valid Growth rate range (dec-dec)\n')
                user_inputGrowthrate = re.findall(r'\d+(?:\.\d+)?', user_inputGrowthrate) #give an opportunity to enter like 0.1&0.5 or any other symbol between, and still will recognise that
                lowerBound = float(user_inputGrowthrate[0])
                upperBound = float(user_inputGrowthrate[1])
                        # Create a mask for rows within the growth rate range
                mask = np.logical_and(restricted_matrix[:, 1] >= lowerBound, restricted_matrix[:, 1] <= upperBound)
                if np.any(mask):
                    restricted_matrix = restricted_matrix[mask, :]
                    break
# =============================================================================
#                     #The colon : in [mask, :] is used to select all columns of the numpy array. 
#                     #So, the resulting subset of restricted_matrix will contain all columns, 
#                     #but only the rows that correspond to True values in the mask array.
# =============================================================================
                    
                        # Create a smaller matrix with only the rows within the growth rate range
                            
                else:
                    print()
                    print('+'+'-'*41+'+')
                    print('|' + ' '*17 + 'WARNING!' + ' '*16 + '|')
                    print('|' + ' '*1 + 'Please input existing Growth rate range' + ' '*1 + '|')
                    print('+' + '-'*41 + '+')
                    
                    continue
        elif user_input_filterdata == 3:
            restricted_matrix = np.copy(matrix)
        elif user_input_filterdata == 4:
            return restricted_matrix
