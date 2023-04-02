import os
import numpy as np 
def selectFromDict(options, name):

    index = 0
    indexValidList = []
    print('Select a ' + name + ':')
    for optionName in options:
        index = index + 1
        indexValidList.extend([options[optionName]])
        print('[' + str(index) + '] ' + optionName)
    inputValid = False
    while not inputValid:
        inputRaw = input(name + ': ')
        try:
            inputNo = int(inputRaw) - 1
            if inputNo > -1 and inputNo < len(indexValidList):
                selected = indexValidList[inputNo]
                print('Selected ' +  name + ': ' + selected)
                inputValid = True
                break
            else:
                print('Please select a valid ' + name + ' number [1-' + str(len(indexValidList)) + ']')
                
        except:
            print('INVALID NUMBER!\nPlease select a valid ' + name + ' number [1-' + str(len(indexValidList)) + ']')

    return selected

def get_options_dicts():

    # Options for yes/no prompts
    yes_no_options = {}
    yes_no_options['Yes'] = 'yes'
    yes_no_options['No'] = 'no'

    # Options for user actions prompts
    user_options = {}
    user_options['1'] = '[1] LoadData\n'
    user_options['2'] = '[2] Filter data\n'
    user_options['3'] = '[3] Display\n'
    user_options['4'] = '[4] Generate plots\n'
    user_options['5'] =  '[5] Quit\n'
    
    # Options for filters prompts
    filter_options = {}
    filter_options['bacteria'] = 'bacteria'
    filter_options['growth_rate'] = 'growth_rate'

    # Options for bacteria filter prompts
    bacteria_options = {}
    user_options['Salmonella enterica'] = 'Salmonella enterica'
    user_options[' Bacillus cereus'] = ' Bacillus cereus'
    user_options['Listeria'] = ' Listeria'
    user_options[' Brochothrix thermosphacta'] = ' Brochothrix thermosphacta'
    # Options for data statistics prompts


    return yes_no_options, user_options, filter_options, bacteria_options

from data_utils import dataLoad, dataPlot, dataStatistics

def filter_data(restricted_matrix, matrix):
    while True:
        user_input_filterdata = int(input('Please insert a number from 1 to 5 \n'+
                                '[1] Filter Bacteria type\n' +
                                '[2] Filter growth rate\n' +
                                '[3] Reset\n' +
                                '[4] Return to main menu\n'))
        if user_input_filterdata > 4 or user_input_filterdata < 1:
            print('Please select a number from the filter menu')
            continue
        elif user_input_filterdata == 1:
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
        

    

def load_data():
    filename = input('Please insert file name and upload file\n')

    if filename.endswith('.txt') :  # check file data type
        matrix = dataLoad(filename)
        if len(matrix) == 0:
            print("Data has not been loaded yet. Please load data first.")
    else:
        print("Invalid file extension.Please provide a file with .txt extension.")
    return matrix
