# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Import External csv file

# More Comments

import csv
import numpy as np
import os
import pandas as pd
import html5lib
import webbrowser

from Parse_Peptide import parse_peaks_peptide
from UniProt_Data_Modifications import create_accession_numbers_file, modify_fasta_reference_file, \
    determine_uniprot_aa_placement, trypsinize_uniprot_string
from User_Interaction import gather_user_input
from Visualizations import generate_heatmap
from HTML_Page_Builder import build_html_page


zero_ptms_count = 0
one_ptm_count = 0
multiple_ptms_count = 0
phosphorylation_count = 0
deamidation_count = 0
oxidation_count = 0
pyro_glu_count = 0
carbamidomethylation_count = 0
acetylation_count = 0
tyrosine_phosphorylations = 0
serine_phosphorylations = 0
threonine_phosphorylations = 0
requested_residue_unmodified = 0
line_count = 0
total_central_aas = 0
total_modified_central_aas = 0
Number_of_PTMs = 0
modified_aa_location = 0


prior_protein_accession_number = ''
protein_accession_number = ''
capture_all_ptms_in_line = ''
PTM_Type = ''
PTM_AA_location = ''
neg_input_list = []
AA_list = []

# In alphabetical order
AA_alpha_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

# In hydrophobicity order
AA_hydrophob_list = ['F', 'I', 'L', 'W', 'V', 'M', 'Y', 'C', 'A', 'T', 'H', 'G', 'S', 'Q', 'R', 'K', 'N', 'P', 'E', 'D']

# By volume
AA_by_volume_list = ['G', 'A', 'S', 'C', 'T', 'D', 'P', 'N', 'V', 'E', 'Q', 'H', 'L', 'I', 'K', 'M', 'F', 'Y', 'R', 'W']

# By pKa
AA_by_pKa_list = ['D', 'E', 'H', 'A', 'N', 'Q', 'G', 'I', 'L', 'M', 'F', 'P', 'S', 'T', 'W', 'V', 'C', 'K', 'Y', 'R']

AA_list  = AA_by_pKa_list

header = True

home_directory = os.path.expanduser('~') + '/Proportion_Teller'

proportion_teller_html_path = home_directory + '/HTML_Files/'

if os.path.exists(home_directory) is False:
    os.mkdir(home_directory)

if os.path.exists(proportion_teller_html_path) is False:
    os.mkdir(proportion_teller_html_path)

proportion_teller_input_path = home_directory + '/Input_Files'

if os.path.exists(proportion_teller_input_path) is False:
    os.mkdir(proportion_teller_input_path)

proportion_teller_output_path = home_directory + '/Output_Files'

if os.path.exists(proportion_teller_output_path) is False:
    os.mkdir(proportion_teller_output_path)

proportion_teller_reference_files_path = home_directory + '/Reference_Files'

if os.path.exists(proportion_teller_reference_files_path) is False:
    os.mkdir(proportion_teller_reference_files_path)



ppt_html_page = proportion_teller_html_path + 'Proportion_Teller_User_Input.html'
ppt_html_page = 'file:' + ppt_html_page

build_html_page()

webbrowser.open(ppt_html_page)

ptm_modifier_file = proportion_teller_input_path + '/User_Response_File.txt'


with open(ptm_modifier_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        requested_aa = row[0]
        requested_ptm = row[1]
        requested_peptide_amino_end_start = row[2]
        requested_peptide_carboxyl_end_finish = row[3]
        requested_a_score = row[4]
        requested_kinase = row[5]

        print(requested_aa)
        print(requested_ptm)
        print(requested_peptide_amino_end_start)
        print(requested_peptide_carboxyl_end_finish)
        print(requested_a_score)
        print(requested_kinase)

    # IGNORE THIS IN FAVOR OF NEW USER INTERFACE -    user_input_data = gather_user_input()

# requested_ptm = 'P'
# requested_aa = 'S'
# requested_kinase = 'TYRO3'
requested_replicate = 1
# requested_peptide_amino_end_start = -4
# requested_peptide_carboxyl_end_finish = 4
requested_analysis_type = 'Kalip'

Zero_PTMs_File = open(proportion_teller_output_path +'/Zero_PTMs', 'w')
One_PTM_File = open(proportion_teller_output_path +'/One_PTM', 'w')
Multiple_PTMs_File = open(proportion_teller_output_path +'/Multiple_PTMs', 'w')
requested_residue_unmodified_file = open(proportion_teller_output_path +'/Unphosphorylated_Tyrosines.csv', 'w')
proportion_teller_files_string = '/' + requested_kinase + '_' + 'N' + '_' + str(requested_replicate) + '_'
pos_peaks_file = proportion_teller_input_path + proportion_teller_files_string + 'protein-peptides.csv'
fasta_file = proportion_teller_reference_files_path +'/FASTA_File.csv'
trypsinized_assay_file = proportion_teller_output_path + '/Trypsinized_UniProt.csv'
screened_peaks_file = proportion_teller_output_path +'/Screened_PEAKS_File.csv'


requested_control = 'MINUS'

if requested_control == 'PLUS':
    neg_portionteller_files_string = '/' + requested_kinase + '/' + requested_kinase + '_PLUS_' + requested_replicate + '_'
    neg_peaks_file = proportion_teller_input_path + neg_portionteller_files_string + 'protein-peptides.csv'
    pos_portionteller_files_string = '/' + requested_kinase + '/' + requested_kinase + '_PLUS_' + requested_replicate + '_'
    pos_peaks_file = proportion_teller_input_path + pos_portionteller_files_string + 'protein-peptides.csv'









""""
with open(neg_peaks_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for neg_input_row in csv_reader:
        neg_input_list.append(neg_input_row[3])

"""

"""
with open(screened_peaks_file,'w') as screened_peaks_file:
    with open(pos_peaks_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for pos_input_row in csv_reader:
            # print(pos_input_row[3])
            # print(neg_input_list[3])
            if pos_input_row[3] not in neg_input_list[3]:
                screened_peaks_file.print(pos_input_row)

"""


"""

formatted_peptide_sequence = [*set(formatted_peptide_sequence)]

output_file = '/Users/miltonandrews/desktop/Python_Output/CDK2_P25_Trypsinized_Lab_Assay.csv'

with open(output_file, 'w') as csv_file:
    for i in range(0, len(formatted_peptide_sequence)):
        csv_file.write(formatted_peptide_sequence[i])
        csv_file.write('\n')

"""

# Specify path
# path = '/home/User/Desktop/file.txt'

# Check whether the specified
# path exists or not
# isExist = os.path.exists(path)
# print(isExist)
# print(home_directory)

# Initialize Arrays With Sizes as Indicated by User Input for each of the 20 amino acids

#CHANGE THESE WHEN FILE TRANSFER OF DATA IS COMPLETED
requested_peptide_amino_end_start = 4
requested_peptide_carboxyl_end_finish = 4
central_aa = 'Y'


matrix_width = requested_peptide_amino_end_start + requested_peptide_carboxyl_end_finish + 1
Bayesian_Probability_Matrix = [[0 for i in range(matrix_width)] for j in range(20)]
Lab_Assay_Trypsinized_Probability_Matrix = [[0 for i in range(matrix_width)] for j in range(20)]
UniProt_Trypsinized_Probability_Matrix = [[0 for i in range(matrix_width)] for j in range(20)]
Sums_of_UniProt_Trypsinized_List = [0 for i in range(matrix_width)]



# Set graph parameters that will remain constant throughout the program
graph_font = 'Times New Roman'
graph_x_axis_label = [0 for i in range(matrix_width)]
for i in range(0, matrix_width):
    graph_x_axis_label[i] = i - requested_peptide_amino_end_start
# graph_y_axis_label = 'ACDEFGHIKLMNPQRSTVWY'
graph_y_axis_label = AA_list

# Create File That Will Store Accession Numbers
accession_numbers_file = create_accession_numbers_file(pos_peaks_file)

# Update FASTA reference file from UniProt as needed
# The FASTA reference file is a local repository of FASTA data referenced by accession number
modify_fasta_reference_file(accession_numbers_file)

requested_ptm = 'P'

if requested_ptm == 'P':
    ptm_name = 'Phosporylation'
elif requested_ptm == 'O':
    ptm_name = 'Oxidation'
elif requested_ptm == 'C':
    ptm_name = 'Carbamidomethylation'
elif requested_ptm == 'D':
    ptm_name = 'Deamidation'
elif requested_ptm == 'A':
    ptm_name = 'Acetylation'
elif requested_ptm == 'Q':
    ptm_name = 'Pyro-glu from Q-Q'

# Now use the FASTA reference file by providing protein accession numbers and getting back FASTA string
with open(fasta_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        protein_string = row[1]
        for i in range(0, len(protein_string)):
            if protein_string[i] == requested_aa:
                total_central_aas += 1

# In silico trypsinize the FASTA file as needed
trypsinize_uniprot_string(requested_aa)

UniProt_Trypsinized_Matrix = determine_uniprot_aa_placement(AA_list, trypsinized_assay_file, requested_aa,
    requested_peptide_amino_end_start, requested_peptide_carboxyl_end_finish)

for m in range(0, matrix_width):
    for n in range(0, 20):
        Sums_of_UniProt_Trypsinized_List[m] = Sums_of_UniProt_Trypsinized_List[m] + UniProt_Trypsinized_Matrix[n][m]




for m in range(0, requested_peptide_amino_end_start):
    for n in range(0, 20):
        UniProt_Trypsinized_Probability_Matrix[n][m] = UniProt_Trypsinized_Matrix[n][m] / Sums_of_UniProt_Trypsinized_List[m]
for m in range(requested_peptide_amino_end_start + 1, matrix_width):
    for n in range(0, 20):
        UniProt_Trypsinized_Probability_Matrix[n][m] = UniProt_Trypsinized_Matrix[n][m] / Sums_of_UniProt_Trypsinized_List[m]

max_uniprot_trysinized_value = np.amax(UniProt_Trypsinized_Probability_Matrix)

graph_title = 'In Silico Prob Matrix for Trypsinized Peptide Using - ' + requested_kinase + ' ' + ptm_name + ' of ' + requested_aa
graph_max = max_uniprot_trysinized_value
# graph_max = 0.1
generate_heatmap(UniProt_Trypsinized_Probability_Matrix, graph_max, graph_font, graph_title, graph_x_axis_label, graph_y_axis_label)

Full_Proteins_Matrix = determine_uniprot_aa_placement(AA_list, fasta_file, requested_aa,
    requested_peptide_amino_end_start, requested_peptide_carboxyl_end_finish)

max_full_protein_value = np.amax(Full_Proteins_Matrix)

graph_title = 'Full Proteins Matrix for ' + ptm_name + ' of ' + requested_aa + ' Using ' + requested_kinase
graph_max = max_full_protein_value
# graph_max = 4000
generate_heatmap(Full_Proteins_Matrix, graph_max, graph_font, graph_title, graph_x_axis_label, graph_y_axis_label)

with open('/Users/miltonandrews/desktop/Python_Test_Data/MER_PLUS_R1_protein-peptides.csv') as csv_file:
# with open('/Users/miltonandrews/desktop/Python_Test_Data/1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if header is True:
            header = False
            line_count += 1
        else:
            protein_accession_full = row[2].split('|')
            protein_accession_number = protein_accession_full[0]
            peptide = row[3]
            Actual_PTM = row[21]
            mass_spec_area = float(row[12])
            capture_all_ptms_in_line = Actual_PTM.split(";")
            # This if statement captures all cases where a PTM did occur for a particular peptide
            if Actual_PTM != '':
                Number_of_PTMs = len(capture_all_ptms_in_line)
            else:
                Number_of_PTMs = 0
            if Number_of_PTMs == 0:
                zero_ptms_count += 1
                Zero_PTMs_File.write(peptide)
                Zero_PTMs_File.write('\n')
                for i in range(0, len(peptide)):
                    if peptide[i] == requested_aa:
                        requested_residue_unmodified += 1
                    if requested_residue_unmodified > 0:
                        requested_residue_unmodified_file.write(peptide)
                        requested_residue_unmodified_file.write(',')
                        requested_residue_unmodified_file.write(str(requested_residue_unmodified))
                        requested_residue_unmodified_file.write(',')
                        requested_residue_unmodified_file.write(str(i+1))
                        requested_residue_unmodified_file.write(',0\n')
                        requested_residue_unmodified = 0
            else:
                for m in range(1, Number_of_PTMs + 1):
                    Actual_PTM = capture_all_ptms_in_line[m - 1]
                    one_ptm_count += 1
                    One_PTM_File.write(peptide)
                    One_PTM_File.write(',')
                    One_PTM_File.write(Actual_PTM)
                    PTM_Data = Actual_PTM.split(":")
                    PTM_AA = PTM_Data[0]
                    PTM_AA_name = PTM_AA[0]
                    for n in range(1, len(PTM_AA)):
                        PTM_AA_location = PTM_AA_location + PTM_AA[n]
                    PTM_AA_location_int = int(PTM_AA_location)
                    One_PTM_File.write(',')
                    One_PTM_File.write(PTM_AA_location)
                    PTM_Type = PTM_Data[1]
                    PTM_A_Score = PTM_Data[2]
                    if PTM_Type == "Phosphorylation (STY)":
                        phosphorylation_count += 1
                        phosphorylation = True
                    if PTM_Type == "Deamidation (NQ)":
                        deamidation_count += 1
                    if PTM_Type == "Oxidation (M)":
                        oxidation_count += 1
                    if PTM_Type == "Pyro-glu from Q":
                        pyro_glu_count += 1
                    if PTM_Type == "Carbamidomethylation":
                        carbamidomethylation_count += 1
                    if PTM_Type == "Acetylation (Protein N-term)":
                        acetylation_count += 1
                    One_PTM_File.write('\n')

                    prior_protein_accession_number = protein_accession_number
                    PTM_AA_location = ''

                    if Number_of_PTMs > 1:
                        multiple_ptms_count += 1
                        Multiple_PTMs_File.write(peptide)
                        Multiple_PTMs_File.write('\n')

            line_count += 1
            capture_all_ptms_in_line = ''

requested_peptide_amino_end_start_peptide_string = \
    parse_peaks_peptide(pos_peaks_file, requested_aa, requested_peptide_amino_end_start,
                        requested_peptide_carboxyl_end_finish, requested_analysis_type)

formatted_peptide_sequence = []

input_file = '/Users/miltonandrews/desktop/Python_Output/pre_sorted_P35_R0_Trypsinized_Lab_Assay.csv'

with open(input_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        formatted_peptide_sequence.append(row[1])

formatted_peptide_sequence = [*set(formatted_peptide_sequence)]

output_file = '/Users/miltonandrews/desktop/Python_Output/CDK2_P25_Trypsinized_Lab_Assay.csv'

with open(output_file, 'w') as csv_file:
    for i in range(0, len(formatted_peptide_sequence)):
        csv_file.write(formatted_peptide_sequence[i])
        csv_file.write('\n')


phosphorylation = False

#   print(f'Processed {line_count} lines.')

print("Total Number of Peptides In File = {}".format(str(line_count)))
print("")
print("Number of Zero PTMs = {}".format(str(zero_ptms_count)))
print("Percentage of Zero PTMs = {0:.0%}".format(zero_ptms_count/line_count))
print("")
print("Number of One PTM = {}".format(str(one_ptm_count)))
print("Percentage of One PTM = {0:.0%}".format(one_ptm_count/line_count))
print("Of the Number of Single Phosphorylations")
print("\tRelative Percentages of Single PTMs")
print("\t" * 2 + "Deamidations = {0:.0%}".format(deamidation_count/one_ptm_count))
print("\t" * 2 + "Oxidations = {0:.0%}".format(oxidation_count/one_ptm_count))
print("\t" * 2 + "Pyro-glu from Q = {0:.0%}".format(pyro_glu_count/one_ptm_count))
print("\t" * 2 + "Carbamidomethylations = {0:.0%}".format(carbamidomethylation_count/one_ptm_count))
print("\t" * 2 + "Acetylations = {0:.0%}".format(acetylation_count/one_ptm_count))
print("\t" * 2 + "Phosphorylations = {0:.0%}".format(phosphorylation_count/one_ptm_count))
print("\t" * 2 + "Percentage of Single PTM Phosphorylations by Amino Acid Relative to Total Number of Phosphorylations")
print("\t" * 3 + "Tyrosine = {0:.0%}".format(tyrosine_phosphorylations/phosphorylation_count))
print("\t" * 3 + "Serine = {0:.0%}".format(serine_phosphorylations/phosphorylation_count))
print("\t" * 3 + "Threonine = {0:.0%}".format(threonine_phosphorylations/phosphorylation_count))
print("\t" * 2 + "Percentage of Phosphorylated PTMs by Amino Acid Relative to Total Number of Peptides")
print("\t" * 3 + "Tyrosine = {0:.0%}".format(tyrosine_phosphorylations/line_count))
print("\t" * 3 + "Serine = {0:.0%}".format(serine_phosphorylations/line_count))
print("\t" * 3 + "Threonine = {0:.0%}".format(threonine_phosphorylations/line_count))

print("Number of Multiple PTMs = {}".format(str(multiple_ptms_count)))
print("Percentage of Multiple PTMs = {0:.0%}".format(multiple_ptms_count/line_count))

Trypsinized_Lab_Assay_File = '/Users/miltonandrews/desktop/Python_Output/pre_sorted_Trypsinized_Lab_Assay.csv'

Lab_Assay_Trypsinized_Matrix = determine_uniprot_aa_placement(AA_list, Trypsinized_Lab_Assay_File, requested_aa,
    requested_peptide_amino_end_start, requested_peptide_carboxyl_end_finish)

max_lab_trypsinized_value = np.amax(Lab_Assay_Trypsinized_Matrix)

graph_title = 'Lab Assay for Trypsinized Peptide - ' + ptm_name + ' of ' + requested_aa + ' Using ' + requested_kinase
graph_max = max_lab_trypsinized_value
# graph_max = 800
generate_heatmap(Lab_Assay_Trypsinized_Matrix, graph_max, graph_font, graph_title, graph_x_axis_label, graph_y_axis_label)

Sums_of_Lab_Assay_Trypsinized_Matrix = [0 for i in range(matrix_width)]
for m in range(0, matrix_width):
    for n in range(0, 20):
        Sums_of_Lab_Assay_Trypsinized_Matrix[m] = Sums_of_Lab_Assay_Trypsinized_Matrix[m] + Lab_Assay_Trypsinized_Matrix[n][m]

for m in range(0, requested_peptide_amino_end_start):
    for n in range(0, 20):
        Lab_Assay_Trypsinized_Probability_Matrix[n][m] = \
            Lab_Assay_Trypsinized_Matrix[n][m] / Sums_of_Lab_Assay_Trypsinized_Matrix[m]
for m in range(requested_peptide_amino_end_start + 1, matrix_width):
    for n in range(0, 20):
        Lab_Assay_Trypsinized_Probability_Matrix[n][m] = \
            Lab_Assay_Trypsinized_Matrix[n][m] / Sums_of_Lab_Assay_Trypsinized_Matrix[m]

max_lab_trypsinized_probability_value = np.amax(Lab_Assay_Trypsinized_Probability_Matrix)

graph_title = 'Lab Assay Prob Matrix for Trypsinized Peptide - Using ' + requested_kinase + ' With ' + ptm_name + ' of ' + requested_aa
graph_max = max_lab_trypsinized_probability_value
# graph_max = 0.1
generate_heatmap(Lab_Assay_Trypsinized_Probability_Matrix, graph_max, graph_font, graph_title, graph_x_axis_label, graph_y_axis_label)

with open(trypsinized_assay_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        central_aa_total_search = row[1]
        for i in range(1, len(central_aa_total_search)):
            if central_aa_total_search[i] == requested_aa:
                total_central_aas += 1

with open('/Users/miltonandrews/desktop/Python_Output/pre_sorted_Trypsinized_Lab_Assay.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        central_aa_total_search = row[1]
        for i in range(1, len(central_aa_total_search)):
            if central_aa_total_search[i] == requested_aa:
                total_modified_central_aas += 1

probability_central_aa_is_modified = total_modified_central_aas / total_central_aas

for m in range(0, requested_peptide_amino_end_start):
    for n in range(0, 20):
        # if UniProt_Trypsinized_Probability_Matrix[n][m] == 0:
        #    UniProt_Trypsinized_Probability_Matrix[n][m] = 0.00001
        Bayesian_Probability_Matrix[n][m] = \
        ((Lab_Assay_Trypsinized_Probability_Matrix[n][m] * probability_central_aa_is_modified)/UniProt_Trypsinized_Probability_Matrix[n][m])
        Bayesian_Probability_Matrix[n][m] = Bayesian_Probability_Matrix[n][m]
for m in range(requested_peptide_amino_end_start + 1, matrix_width):
    for n in range(0, 20):
        # if UniProt_Trypsinized_Probability_Matrix[n][m] == 0:
        #    UniProt_Trypsinized_Probability_Matrix[n][m] = 0.00001
        Bayesian_Probability_Matrix[n][m] = \
        ((Lab_Assay_Trypsinized_Probability_Matrix[n][m] *
            probability_central_aa_is_modified)/UniProt_Trypsinized_Probability_Matrix[n][m])

max_bayesian_value = np.amax(Bayesian_Probability_Matrix)

graph_title = 'Bayesian Prob Matrix for Trypsinized Peptide - Using ' + requested_kinase + ' With ' + ptm_name + ' of ' + requested_aa
graph_max = max_bayesian_value
# graph_max = 0.015
generate_heatmap(Bayesian_Probability_Matrix, graph_max, graph_font, graph_title, graph_x_axis_label, graph_y_axis_label)

Zero_PTMs_File.close()
One_PTM_File.close()
Multiple_PTMs_File.close()
requested_residue_unmodified_file.close()
