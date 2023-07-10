import csv
import os
import numpy as np
from datetime import datetime

# datetime object containing current date and time
start_time = datetime.now()

print("now =", start_time)

# dd/mm/YY H:M:S
dt_string = start_time.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# The next line represents a generic counter, replacing the index variables i,j,k,l,m,etc.
counter = []
# The following represents the number of dimensions in a matrix, one dimension for each AA sequence
# For example, a two-dimensional matrix is made up of all AA combinations AA, AC, AD,...YV, YW, YY
# A three-dimensional matrix is made up of all AA combinations AAA, AAC, AAD, .., GAA, GAC, ... YYV, YYW, YYY
number_of_dimensions = 5
# This list keeps track of the number of times a specific AA appears in a location
dimension_values = []
# The following variable i is a running index used in the following for loop
i = 0
# Numerical relative percentage cutoff value for reporting output
cutoff_value = 0

# Append the counter and dimension_values matrices to match the number of required indices and initialize them to zero
for i in range(number_of_dimensions):
    counter.append(0)
    dimension_values.append(0)

# AA list in alphabetical order
AA_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

# The following are operating system assignments of required directories and files
# This line points to the home directory for Proportion Teller where all program files are read from or written to
home_directory = os.path.expanduser('~') + '/Proportion_Teller'

# Assign a variable name to the path for output files
proportion_teller_output_path = home_directory + '/Output_Files'

# If the output file path does not exist in the home directory then create it
if os.path.exists(proportion_teller_output_path) is False:
    os.mkdir(proportion_teller_output_path)

# Assign a variable name to the path for reference files (for example the FASTA file)
proportion_teller_reference_files_path = home_directory + '/Reference_Files/'

# If the reference file path does not exist in the home directory then create it
if os.path.exists(proportion_teller_reference_files_path) is False:
    os.mkdir(proportion_teller_reference_files_path)

# Assign and variable name to the human proteome FASTA file
fasta_reference_file_FULL = proportion_teller_reference_files_path + 'Human_Proteome_Full.fasta'

# Assign and variable name to the human proteome csv file
fasta_file = proportion_teller_reference_files_path + 'Human_Proteome_Full.csv'

if number_of_dimensions == 2:
    frequency_matrix = [[0 for col in range(len(AA_list))] for row in range(len(AA_list))]

if number_of_dimensions == 3:
    frequency_matrix = [[[0 for col in range(len(AA_list))] for col in range(len(AA_list))] \
                           for row in range(len(AA_list))]

if number_of_dimensions == 4:
    frequency_matrix = [[[[0 for col in range(len(AA_list))] for col in range(len(AA_list))]\
                            for col in range(len(AA_list))] for row in range(len(AA_list))]

if number_of_dimensions == 5:
    frequency_matrix = [[[[[0 for col in range(len(AA_list))] for col in range(len(AA_list))]\
                            for col in range(len(AA_list))] for col in range(len(AA_list))]\
                                for row in range(len(AA_list))]

if number_of_dimensions == 6:
    frequency_matrix = [[[[[[0 for col in range(len(AA_list))] for col in range(len(AA_list))] \
                            for col in range(len(AA_list))] for col in range(len(AA_list))] \
                                for row in range(len(AA_list))] for row in range(len(AA_list))]

if number_of_dimensions == 7:
    frequency_matrix = [[[[[[[0 for col in range(len(AA_list))] for col in range(len(AA_list))] \
                            for col in range(len(AA_list))] for col in range(len(AA_list))] \
                                for row in range(len(AA_list))] for row in range(len(AA_list))] \
                                    for row in range(len(AA_list))]

if number_of_dimensions == 8:
    frequency_matrix = [[[[[[[[0 for col in range(len(AA_list))] for col in range(len(AA_list))] \
                            for col in range(len(AA_list))] for col in range(len(AA_list))] \
                                for row in range(len(AA_list))] for row in range(len(AA_list))] \
                                    for row in range(len(AA_list))] for row in range(len(AA_list))]

if number_of_dimensions == 9:
    frequency_matrix = [[[[[[[[[0 for col in range(len(AA_list))] for col in range(len(AA_list))] \
                            for col in range(len(AA_list))] for col in range(len(AA_list))] \
                                for row in range(len(AA_list))] for row in range(len(AA_list))] \
                                    for row in range(len(AA_list))] for row in range(len(AA_list))] \
                                        for row in range(len(AA_list))]

total_pairs = 0
current_line = ''

fasta_file_pointer = open(fasta_file, 'w')

with open(fasta_reference_file_FULL) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        aa_seq = row[0]
        if (aa_seq[0] == '>'):
            if len(current_line) > 0:
                fasta_file_pointer.write(current_line)
                fasta_file_pointer.write('\n')
#                print(current_line)
            current_line = ''
        else:
            current_line = current_line + aa_seq

fasta_file_pointer.write(current_line)
fasta_file_pointer.write('\n')
# print(current_line)

fasta_file_pointer.close()

with open(fasta_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        aa_seq = row[0]
        for counter[0] in range(len(aa_seq)-number_of_dimensions-1):
            for counter[1] in range(len(AA_list)):
                for counter[2] in range (number_of_dimensions):
                    if (aa_seq[counter[0]+counter[2]] == AA_list[counter[1]]):
                        dimension_values[counter[2]] = counter[1]

            if number_of_dimensions == 2:
                frequency_matrix[dimension_values[0]][dimension_values[1]] += 1
            if number_of_dimensions == 3:
                frequency_matrix[dimension_values[0]][dimension_values[1]][dimension_values[2]] += 1
            if number_of_dimensions == 4:
                frequency_matrix[dimension_values[0]][dimension_values[1]][dimension_values[2]][dimension_values[3]] += 1
            if number_of_dimensions == 5:
                frequency_matrix[dimension_values[0]][dimension_values[1]][dimension_values[2]][dimension_values[3]]\
                    [dimension_values[4]] += 1
            if number_of_dimensions == 6:
                frequency_matrix[dimension_values[0]][dimension_values[1]][dimension_values[2]][dimension_values[3]] \
                    [dimension_values[4]][dimension_values[5]] += 1
            if number_of_dimensions == 7:
                frequency_matrix[dimension_values[0]][dimension_values[1]][dimension_values[2]][dimension_values[3]] \
                    [dimension_values[4]][dimension_values[5]][dimension_values[6]] += 1
            if number_of_dimensions == 8:
                frequency_matrix[dimension_values[0]][dimension_values[1]][dimension_values[2]][dimension_values[3]] \
                    [dimension_values[4]][dimension_values[5]][dimension_values[6]][dimension_values[7]] += 1
            if number_of_dimensions == 9:
                frequency_matrix[dimension_values[0]][dimension_values[1]][dimension_values[2]][dimension_values[3]] \
                    [dimension_values[4]][dimension_values[5]][dimension_values[6]][dimension_values[7]] \
                    [dimension_values[8]] += 1
            total_pairs += 1

if number_of_dimensions == 1:
    for counter[0] in range(20):
        frequency_matrix[counter[0]] = (frequency_matrix[counter[0]] / total_pairs)

if number_of_dimensions == 2:
    for counter[0] in range(20):
        for counter[1] in range(20):
                frequency_matrix[counter[0]][counter[1]] = (frequency_matrix[counter[0]][counter[1]] / total_pairs)

if number_of_dimensions == 3:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                frequency_matrix[counter[0]][counter[1]][counter[2]] = \
                        (frequency_matrix[counter[0]][counter[1]][counter[2]] \
                            / total_pairs) * 100000

if number_of_dimensions == 4:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] = \
                            (frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                                / total_pairs) * 10000000

if number_of_dimensions == 5:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]][counter[4]] = \
                                (frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                                    [counter[4]] / total_pairs) * 10000000

if number_of_dimensions == 6:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        for counter[5] in range(20):
                                        frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]][counter[4]] \
                                            [counter[5]] = (frequency_matrix[counter[0]][counter[1]][counter[2]] \
                                                [counter[3]][counter[4]][counter[5]] / total_pairs) * 10000000

if number_of_dimensions == 7:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        for counter[5] in range(20):
                            for counter[6] in range(20):
                                        frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]][counter[4]]\
                                            [counter[5]][counter[6]]= \
                                                (frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                                                    [counter[4]][counter[5]][counter[6]] \
                                                        / total_pairs) * 10000000

if number_of_dimensions == 8:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        for counter[5] in range(20):
                            for counter[6] in range(20):
                                for counter[7] in range(20):
                                        frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]][counter[4]]\
                                            [counter[5]][counter[6]][counter[7]] = \
                                                (frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                                                    [counter[4]][counter[5]][counter[6]][counter[7]] \
                                                        / total_pairs) * 10000000

if number_of_dimensions == 9:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        for counter[5] in range(20):
                            for counter[6] in range(20):
                                for counter[7] in range(20):
                                    for counter[8] in range(20):
                                        frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]][counter[4]] \
                                            [counter[5]][counter[6]][counter[7]][counter[8]] = \
                                                (frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                                                    [counter[4]][counter[5]][counter[6]][counter[7]] \
                                                        [counter[8]] / total_pairs) * 10000000

if number_of_dimensions == 1:
    for counter[0] in range(20):
            if frequency_matrix[counter[0]] > cutoff_value:
                # if (j == 0):
                print("%1.10f  " % frequency_matrix[counter[0]])
                # print(counter[0])
                print(AA_list[counter[0]])
                print()

if number_of_dimensions == 2:
    for counter[0] in range(20):
        for counter[1] in range(20):
            if frequency_matrix[counter[0]][counter[1]] > cutoff_value:
                # if (j == 0):
                print("%1.10f  " % frequency_matrix[counter[0]][counter[1]])
                # print(counter[0],counter[1])
                print(AA_list[counter[0]],AA_list[counter[1]])
                print()

if number_of_dimensions == 3:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                    if frequency_matrix[counter[0]][counter[1]][counter[2]] > cutoff_value:
                        # if (j == 0):
                        print("%1.10f  " % frequency_matrix[counter[0]][counter[1]][counter[2]])
                        # print(counter[0],counter[1],counter[2])
                        print(AA_list[counter[0]],AA_list[counter[1]],AA_list[counter[2]])
                        print()

if number_of_dimensions == 4:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    if frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] > cutoff_value:
                        # if (j == 0):
                        print("%1.10f  " % frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]])
                        # print(counter[0],counter[1],counter[2],counter[3])
                        print(AA_list[counter[0]],AA_list[counter[1]],AA_list[counter[2]], AA_list[counter[3]])
                        print()

if number_of_dimensions == 5:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        #if frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                        #    [counter[4]] > cutoff_value:
                        if (counter[4] == 19 and counter[3] == 9 and counter[2] == 3):
                            if frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]][counter[4]] > cutoff_value:
                                print("%1.10f  " % frequency_matrix[counter[0]][counter[1]] \
                                    [counter[2]][counter[3]][counter[4]])
                                # print(counter[0],counter[1],counter[2],counter[3],counter[4])
                                print(AA_list[counter[0]],AA_list[counter[1]],AA_list[counter[2]], \
                                    AA_list[counter[3]],AA_list[counter[4]])
                                print()

if number_of_dimensions == 6:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        for counter[5] in range(20):
                            if frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                                [counter[4]][counter[5]] > cutoff_value:
                # if (j == 0):
                                print("%1.10f  " % frequency_matrix[counter[0]][counter[1]] \
                                    [counter[2]][counter[3]][counter[4]][counter[5]])
                                # print(counter[0],counter[1],counter[2],counter[3],counter[4], \
                                #     counter[5])
                                print(AA_list[counter[0]], AA_list[counter[1]], AA_list[counter[2]],
                                    AA_list[counter[3]], AA_list[counter[4]], AA_list[counter[5]])
                            print()

if number_of_dimensions == 7:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        for counter[5] in range(20):
                            for counter[6] in range(20):
                                if frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                                    [counter[4]][counter[5]][counter[6]] > cutoff_value:
                                    # if (j == 0):
                                    print("%1.10f  " % frequency_matrix[counter[0]][counter[1]] \
                                        [counter[2]][counter[3]][counter[4]][counter[5]][counter[6]])
                                    # print(counter[0],counter[1],counter[2],counter[3],counter[4],
                                    #       counter[5],counter[6])
                                    print(AA_list[counter[0]],AA_list[counter[1]],AA_list[counter[2]],
                                            AA_list[counter[3]],AA_list[counter[4]],AA_list[counter[5]],
                                                AA_list[counter[6]])
                            print()

if number_of_dimensions == 8:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        for counter[5] in range(20):
                            for counter[6] in range(20):
                                for counter[7] in range(20):
                                    if frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]]\
                                        [counter[4]][counter[5]][counter[6]][counter[7]] > cutoff_value:
                                        # if (j == 0):
                                        print("%1.10f  " % frequency_matrix[counter[0]][counter[1]]\
                                            [counter[2]][counter[3]][counter[4]][counter[5]][counter[6]]\
                                            [counter[7]])
                                        # print(counter[0],counter[1],counter[2],counter[3],counter[4],
                                        #       counter[5],counter[6],counter[7])
                                        print(AA_list[counter[0]],AA_list[counter[1]],AA_list[counter[2]],
                                                AA_list[counter[3]],AA_list[counter[4]],AA_list[counter[5]],
                                                    AA_list[counter[6]],AA_list[counter[7]])
                            print()

if number_of_dimensions == 9:
    for counter[0] in range(20):
        for counter[1] in range(20):
            for counter[2] in range(20):
                for counter[3] in range(20):
                    for counter[4] in range(20):
                        for counter[5] in range(20):
                            for counter[6] in range(20):
                                for counter[7] in range(20):
                                    for counter[8] in range(20):
                                        if frequency_matrix[counter[0]][counter[1]][counter[2]][counter[3]] \
                                            [counter[4]][counter[5]][counter[6]][counter[7]][counter[8]] > cutoff_value:
                                            # if (j == 0):
                                            print("%1.10f  " % frequency_matrix[counter[0]][counter[1]] \
                                                [counter[2]][counter[3]][counter[4]][counter[5]][counter[6]] \
                                                [counter[7]][counter[8]])
                                            # print(counter[0],counter[1],counter[2],counter[3],counter[4],
                                            #       counter[5],counter[6],counter[7],counter[8])
                                            print(AA_list[counter[0]],AA_list[counter[1]],AA_list[counter[2]],
                                                    AA_list[counter[3]],AA_list[counter[4]],AA_list[counter[5]],
                                                        AA_list[counter[6]],AA_list[counter[7]],AA_list[counter[8]])
                            print()

print("Program start time =", start_time)

# dd/mm/YY H:M:S
# dt_string = start_time.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)

# datetime object containing current date and time
end_time = datetime.now()

print("Program end time =", end_time)

elapsed_time = end_time - start_time
print("Elapsed time = ", elapsed_time)

# dd/mm/YY H:M:S
#dt_string = end_time.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)

# print(total_pairs)
