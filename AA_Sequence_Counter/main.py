# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Import External csv file

# More Comments

import csv
import os
import webbrowser

neg_input_list = []
AA_list = []

i = 0
j = 0
col_no = 0
row_no = 0

# In alphabetical order
AA_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

header = True

home_directory = os.path.expanduser('~') + '/Proportion_Teller'

proportion_teller_output_path = home_directory + '/Output_Files'

if os.path.exists(proportion_teller_output_path) is False:
    os.mkdir(proportion_teller_output_path)

proportion_teller_reference_files_path = home_directory + '/Reference_Files/'

if os.path.exists(proportion_teller_reference_files_path) is False:
    os.mkdir(proportion_teller_reference_files_path)

fasta_file = proportion_teller_reference_files_path + 'FASTA_File.csv'

init_matrix_0 = []
init_matrix_1 = []
init_matrix_2 = []
init_matrix_3 = []
init_matrix_4 = []
init_matrix_5 = []
init_matrix_6 = []
init_matrix_7 = []
init_matrix_8 = []
init_matrix_9 = []
init_matrix_10 = []
init_matrix_11 = []
init_matrix_12 = []
init_matrix_13 = []
init_matrix_14 = []
init_matrix_15 = []
init_matrix_16 = []
init_matrix_17 = []
init_matrix_18 = []
init_matrix_19 = []

frequency_matrix = []

total_pairs = 0

for i in range(0,19):
    init_matrix_0.append(0)
for i in range(0, 19):
    init_matrix_1.append(0)
for i in range(0, 19):
    init_matrix_2.append(0)
for i in range(0, 19):
    init_matrix_3.append(0)
for i in range(0, 19):
    init_matrix_4.append(0)
for i in range(0, 19):
    init_matrix_5.append(0)
for i in range(0, 19):
    init_matrix_6.append(0)
for i in range(0, 19):
    init_matrix_7.append(0)
for i in range(0, 19):
    init_matrix_8.append(0)
for i in range(0, 19):
    init_matrix_9.append(0)
for i in range(0, 19):
    init_matrix_10.append(0)
for i in range(0, 19):
    init_matrix_11.append(0)
for i in range(0, 19):
    init_matrix_12.append(0)
for i in range(0, 19):
    init_matrix_13.append(0)
for i in range(0, 19):
    init_matrix_14.append(0)
for i in range(0, 19):
    init_matrix_15.append(0)
for i in range(0, 19):
    init_matrix_16.append(0)
for i in range(0, 19):
    init_matrix_17.append(0)
for i in range(0, 19):
    init_matrix_18.append(0)
for i in range(0, 19):
    init_matrix_19.append(0)

frequency_matrix.append(init_matrix_0)
frequency_matrix.append(init_matrix_1)
frequency_matrix.append(init_matrix_2)
frequency_matrix.append(init_matrix_3)
frequency_matrix.append(init_matrix_4)
frequency_matrix.append(init_matrix_5)
frequency_matrix.append(init_matrix_6)
frequency_matrix.append(init_matrix_7)
frequency_matrix.append(init_matrix_8)
frequency_matrix.append(init_matrix_9)
frequency_matrix.append(init_matrix_10)
frequency_matrix.append(init_matrix_11)
frequency_matrix.append(init_matrix_12)
frequency_matrix.append(init_matrix_13)
frequency_matrix.append(init_matrix_14)
frequency_matrix.append(init_matrix_15)
frequency_matrix.append(init_matrix_16)
frequency_matrix.append(init_matrix_17)
frequency_matrix.append(init_matrix_18)
frequency_matrix.append(init_matrix_19)

with open(fasta_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        aa_seq = row[1]
        for i in range(0, (len(aa_seq)-1)):
            # duet = aa_seq[i] + aa_seq[i+1]
            for j in range(0,19):
                if (aa_seq[i] == AA_list[j]):
                    row_no = j
                if (aa_seq[i+1] == AA_list[j]):
                    col_no = j
            frequency_matrix[row_no][col_no] += 1
            total_pairs += 1

for i in range(0,19):
    print(frequency_matrix[i])
print(total_pairs)

