import numpy as np 

#Filtering part by it's bacteria type, growth rate, or both. Obtained matrix 
#will be used to do statistical calculations
def filter_data(restricted_matrix, matrix):
    while True:
        try:
            user_input_filterdata = int(input('Please insert a number from 1 to 4 \n'+
                                    '[1] Filter Bacteria type\n' +
                                    '[2] Filter growth rate\n' +
                                    '[3] Reset\n' +
                                    '[4] Return to main menu\n'))
            if user_input_filterdata > 4 or user_input_filterdata < 1:
                print()
                raise ValueError('Please select a number from the filter menu')
        except ValueError as j:
            print(j) 
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
                user_inputBacteriatype = int(input('Please select a Bacteria type\n'+
                                                    f'[1] = {bacteria_dict[1] }\n' +
                                                    f'[2] = {bacteria_dict[2] }\n' +
                                                    f'[3] = {bacteria_dict[3] }\n' +
                                                    f'[4] = {bacteria_dict[4] }\n' +
                                                    '[5] Quit current menu\n'))
                if user_inputBacteriatype not in restricted_matrix:
                    print("Please select existing Bacteria type")  # Should be an option to override restricted_matrix to the new one, after I select another bacteria type
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