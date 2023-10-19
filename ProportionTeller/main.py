# main.py

import csv
import numpy as np
import os
import webbrowser

from Parse_Peptide import Parse_peaks_peptide
from UniProt_Data_Modifications import Create_accession_numbers_file, Modify_fasta_reference_file, \
   Determine_uniprot_aa_placement, Trypsinize_uniprot_string
from Visualizations import Generate_heatmap
from HTML_Page_Builder import Build_html_page
from Screen_Against_Control import Screen_experimental_against_control

# THIS IS A TEST TO CONMFIRM TRANSACTIONS ARE BEING PROCESSED TO GITHUB

Zero_ptms_count = 0
One_ptm_count = 0
Multiple_ptms_count = 0
Phosphorylation_count = 0
Deamidation_count = 0
Oxidation_count = 0
Pyro_glu_count = 0
Carbamidomethylation_count = 0
Acetylation_count = 0
Tyrosine_phosphorylations = 0
Serine_phosphorylations = 0
Threonine_phosphorylations = 0
Requested_residue_unmodified = 0
Total_central_aas = 0
Total_modified_central_aas = 0
Number_of_PTMs = 0
Modified_aa_location = 0

line_count = 0

Prior_protein_accession_number = ''
Protein_accession_number = ''
Capture_all_ptms_in_line = ''
PTM_Type = ''
PTM_AA_location = ''
Neg_input_list = []
AA_list = []

# In alphabetical order
AA_alpha_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

# In hydrophobicity order
AA_hydrophob_list = ['F', 'I', 'L', 'W', 'V', 'M', 'Y', 'C', 'A', 'T', 'H', 'G', 'S', 'Q', 'R', 'K', 'N', 'P', 'E', 'D']

# By volume
AA_by_volume_list = ['G', 'A', 'S', 'C', 'T', 'D', 'P', 'N', 'V', 'E', 'Q', 'H', 'L', 'I', 'K', 'M', 'F', 'Y', 'R', 'W']

# By pKa
AA_by_pKa_list = ['D', 'E', 'H', 'A', 'N', 'Q', 'G', 'I', 'L', 'M', 'F', 'P', 'S', 'T', 'W', 'V', 'C', 'K', 'Y', 'R']

AA_list  = AA_alpha_list

Header = True

Home_directory = os.path.expanduser('~') + '/ProportionTeller/'
Input_directory = Home_directory + 'Input_directory/'
Working_directory = Home_directory + 'Working_directory/'
Output_directory = Home_directory + 'Output_directory/'
Reference_files_directory = Home_directory + 'Reference_files_directory/'


if os.path.exists(Home_directory) is False:
   os.mkdir(Home_directory)

if os.path.exists(Working_directory) is False:
   os.mkdir(Working_directory)

if os.path.exists(Input_directory) is False:
   os.mkdir(Input_directory)

if os.path.exists(Output_directory) is False:
   os.mkdir(Output_directory)

if os.path.exists(Reference_files_directory) is False:
   os.mkdir(Reference_files_directory)

if os.path.exists(Working_directory) is False:
    os.mkdir(Working_directory)

Screen_experimental_against_control(Input_directory,Working_directory)
Unmatched_post_control_filter_file = Working_directory + 'Unmatched_Post_Control_Filter_File.csv'


#ppt_html_page = ProportionTeller_html_path + 'ProportionTeller_User_Input.html'
#ppt_html_page = 'file:' + ppt_html_page

Html_user_input_file = Working_directory + 'Html_input_page.html'
Html_user_input_file = 'file:' + Html_user_input_file

Build_html_page()

webbrowser.open(Html_user_input_file)

Ptm_modifier_file = Input_directory + 'User_Response_File.csv'


with open(Ptm_modifier_file) as Csv_file:
    Csv_reader = csv.reader(Csv_file, delimiter=',')
    for Row in Csv_reader:
        Requested_aa = Row[0]
        Requested_ptm = Row[1]
        Requested_peptide_amino_end_start = Row[2]
        Requested_peptide_carboxyl_end_finish = Row[3]
        Requested_a_score = Row[4]
        Requested_kinase = Row[5]

       # print(requested_aa)
       # print(requested_ptm)
       # print(requested_peptide_amino_end_start)
       # print(Requested_peptide_carboxyl_end_finish)
       # print(requested_a_score)
       # print(requested_kinase)

   # IGNORE THIS IN FAVOR OF NEW USER INTERFACE -    user_input_data = gather_user_input()

# requested_ptm = 'P'
# requested_aa = 'S'
# requested_kinase = 'TYRO3'
Requested_replicate = 1
# requested_peptide_amino_end_start = -4
# Requested_peptide_carboxyl_end_finish = 4
Requested_analysis_type = 'Kalip'

Zero_PTMs_File = open(Output_directory +'/Zero_PTMs.csv', 'w')
One_PTM_File = open(Output_directory +'/One_PTM.csv', 'w')
Multiple_PTMs_File = open(Output_directory +'/Multiple_PTMs.csv', 'w')
Requested_residue_unmodified_file = open(Output_directory +'/Unphosphorylated_Tyrosines.csv', 'w')
# ProportionTeller_files_string = '/' + requested_kinase + '_' + 'N' + '_' + str(Requested_replicate) + '_'
# pos_peaks_file = Input_path + ProportionTeller_files_string + 'protein-peptides.csv'
# pos_peaks_file = Unmatched_post_control_filter_file
# pos_peaks_file = Input_directory + 'Post_Control_Filter.csv'
Fasta_file = Reference_files_directory +'/FASTA_File.csv'
Trypsinized_assay_file = Output_directory + '/Trypsinized_UniProt.csv'
Screened_peaks_file = Output_directory +'/Screened_PEAKS_File.csv'

# Specify path
# path = '/home/User/Desktop/file.txt'

# Check whether the specified
# path exists or not
# isExist = os.path.exists(path)
# print(isExist)
# print(Home_directory)

# Initialize Arrays With Sizes as Indicated by User Input for each of the 20 amino acids

#CHANGE THESE WHEN FILE TRANSFER OF DATA IS COMPLETED
Requested_peptide_amino_end_start = 4
Requested_peptide_carboxyl_end_finish = 4
Central_aa = 'S'


Matrix_width = Requested_peptide_amino_end_start + Requested_peptide_carboxyl_end_finish + 1
Bayesian_Probability_Matrix = [[0 for i in range(Matrix_width)] for j in range(20)]
Lab_Assay_Trypsinized_Probability_Matrix = [[0 for i in range(Matrix_width)] for j in range(20)]
UniProt_Trypsinized_Probability_Matrix = [[0 for i in range(Matrix_width)] for j in range(20)]
Sums_of_UniProt_Trypsinized_List = [0 for i in range(Matrix_width)]



# Set graph parameters that will remain constant throughout the program
Graph_font = 'Times New Roman'
Graph_x_axis_label = [0 for i in range(Matrix_width)]
for i in range(0, Matrix_width):
   Graph_x_axis_label[i] = i - Requested_peptide_amino_end_start
# Graph_y_axis_label = 'ACDEFGHIKLMNPQRSTVWY'
Graph_y_axis_label = AA_list

# Create File That Will Store Accession Numbers
Accession_numbers_file = Create_accession_numbers_file(Working_directory)

# Update FASTA reference file from UniProt as needed
# The FASTA reference file is a local repository of FASTA data referenced by accession number
Modify_fasta_reference_file(Accession_numbers_file)

Requested_ptm = 'P'

if Requested_ptm == 'P':
   ptm_name = 'Phosporylation'
elif Requested_ptm == 'O':
   ptm_name = 'Oxidation'
elif Requested_ptm == 'C':
   ptm_name = 'Carbamidomethylation'
elif Requested_ptm == 'D':
   ptm_name = 'Deamidation'
elif Requested_ptm == 'A':
   ptm_name = 'Acetylation'
elif Requested_ptm == 'Q':
   ptm_name = 'Pyro-glu from Q-Q'

# Now use the FASTA reference file by providing protein accession numbers and getting back FASTA string
with open(Fasta_file) as Csv_file:
   Csv_reader = csv.reader(Csv_file, delimiter=',')
   for Row in Csv_reader:
       Protein_string = Row[1]
       for i in range(0, len(Protein_string)):
           if Protein_string[i] == Requested_aa:
               Total_central_aas += 1

# In silico trypsinize the FASTA file as needed
Trypsinize_uniprot_string(Requested_aa)

UniProt_Trypsinized_Matrix = Determine_uniprot_aa_placement(AA_list, Trypsinized_assay_file, Requested_aa,
   Requested_peptide_amino_end_start, Requested_peptide_carboxyl_end_finish)

for m in range(0, Matrix_width):
   for n in range(0, 20):
       Sums_of_UniProt_Trypsinized_List[m] = Sums_of_UniProt_Trypsinized_List[m] + UniProt_Trypsinized_Matrix[n][m]




for m in range(0, Requested_peptide_amino_end_start):
   for n in range(0, 20):
       UniProt_Trypsinized_Probability_Matrix[n][m] = UniProt_Trypsinized_Matrix[n][m] / Sums_of_UniProt_Trypsinized_List[m]
for m in range(Requested_peptide_amino_end_start + 1, Matrix_width):
   for n in range(0, 20):
       UniProt_Trypsinized_Probability_Matrix[n][m] = UniProt_Trypsinized_Matrix[n][m] / Sums_of_UniProt_Trypsinized_List[m]

max_uniprot_trysinized_value = np.amax(UniProt_Trypsinized_Probability_Matrix)

graph_title = 'In Silico Prob Matrix for Trypsinized Peptide Using - ' + Requested_kinase + ' ' + ptm_name + ' of ' + Requested_aa
graph_max = max_uniprot_trysinized_value
# graph_max = 0.1
Generate_heatmap(UniProt_Trypsinized_Probability_Matrix, graph_max, Graph_font, graph_title, Graph_x_axis_label, Graph_y_axis_label)

Full_Proteins_Matrix = Determine_uniprot_aa_placement(AA_list, Fasta_file, Requested_aa,
   Requested_peptide_amino_end_start, Requested_peptide_carboxyl_end_finish)

max_full_protein_value = np.amax(Full_Proteins_Matrix)

graph_title = 'Full Proteins Matrix for ' + ptm_name + ' of ' + Requested_aa + ' Using ' + Requested_kinase
graph_max = max_full_protein_value
# graph_max = 4000
Generate_heatmap(Full_Proteins_Matrix, graph_max, Graph_font, graph_title, Graph_x_axis_label, Graph_y_axis_label)

# with open('/Users/miltonandrews/desktop/Python_Test_Data/MER_PLUS_R1_protein-peptides.csv') as Csv_file:
# print(pos_peaks_file)
# with open('/Users/miltonandrews/desktop/Python_Test_Data/1.csv') as Csv_file:
with open(Unmatched_post_control_filter_file) as Unmatched_post_control_filter_csv_file:
   Csv_reader = csv.reader(Unmatched_post_control_filter_csv_file, delimiter=',')
   for Row in Csv_reader:
       if Header is True:
           Header = False
           line_count += 1
       else:
           protein_accession_full = Row[2].split('|')
           Protein_accession_number = protein_accession_full[0]
           peptide = Row[3]
           Actual_PTM = Row[21]
           mass_spec_area = float(Row[12])
           Capture_all_ptms_in_line = Actual_PTM.split(";")
           # This if statement captures all cases where a PTM did occur for a particular peptide
           if Actual_PTM != '':
               Number_of_PTMs = len(Capture_all_ptms_in_line)
           else:
               Number_of_PTMs = 0
           if Number_of_PTMs == 0:
               Zero_ptms_count += 1
               Zero_PTMs_File.write(peptide)
               Zero_PTMs_File.write('\n')
               for i in range(0, len(peptide)):
                   if peptide[i] == Requested_aa:
                       Requested_residue_unmodified += 1
                   if Requested_residue_unmodified > 0:
                       Requested_residue_unmodified_file.write(peptide)
                       Requested_residue_unmodified_file.write(',')
                       Requested_residue_unmodified_file.write(str(Requested_residue_unmodified))
                       Requested_residue_unmodified_file.write(',')
                       Requested_residue_unmodified_file.write(str(i+1))
                       Requested_residue_unmodified_file.write(',0\n')
                       Requested_residue_unmodified = 0
           else:
               for m in range(1, Number_of_PTMs + 1):
                   Actual_PTM = Capture_all_ptms_in_line[m - 1]
                   One_ptm_count += 1
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
                       Phosphorylation_count += 1
                       phosphorylation = True
                   if PTM_Type == "Deamidation (NQ)":
                       Deamidation_count += 1
                   if PTM_Type == "Oxidation (M)":
                       Oxidation_count += 1
                   if PTM_Type == "Pyro-glu from Q":
                       Pyro_glu_count += 1
                   if PTM_Type == "Carbamidomethylation":
                       Carbamidomethylation_count += 1
                   if PTM_Type == "Acetylation (Protein N-term)":
                       Acetylation_count += 1
                   One_PTM_File.write('\n')

                   Prior_protein_accession_number = Protein_accession_number
                   PTM_AA_location = ''

                   if Number_of_PTMs > 1:
                       Multiple_ptms_count += 1
                       Multiple_PTMs_File.write(peptide)
                       Multiple_PTMs_File.write('\n')

           line_count += 1
           Capture_all_ptms_in_line = ''

requested_peptide_amino_end_start_peptide_string = \
   Parse_peaks_peptide(Unmatched_post_control_filter_file, Requested_aa, Requested_peptide_amino_end_start,
                       Requested_peptide_carboxyl_end_finish, Requested_analysis_type)

print('From main:')
print(requested_peptide_amino_end_start_peptide_string)

unsorted_formatted_aa_sequence = []

input_file = Working_directory + 'Presorted_formatted_aa_sequences.csv'

with open(input_file, 'r') as Csv_file:
   Csv_reader = csv.reader(Csv_file, delimiter=',')
   for Row in Csv_reader:
       unsorted_formatted_aa_sequence.append(Row[1])

formatted_peptide_sequence = [*set(unsorted_formatted_aa_sequence)]

output_file = Working_directory + 'Unsorted_formatted_aa_sequences.csv'

with open(output_file, 'w') as Csv_file:
   for i in range(0, len(formatted_peptide_sequence)):
       Csv_file.write(formatted_peptide_sequence[i])
       Csv_file.write('\n')

phosphorylation = False

#   print(f'Processed {line_count} lines.')

# print("Total Number of Peptides In File = {}".format(str(line_count)))
# print("")
#  print("Number of Zero PTMs = {}".format(str(Zero_ptms_count)))
# print("Percentage of Zero PTMs = {0:.0%}".format(Zero_ptms_count/line_count))
# print("")
# print("Number of One PTM = {}".format(str(One_ptm_count)))
# print("Percentage of One PTM = {0:.0%}".format(One_ptm_count/line_count))
# print("Of the Number of Single Phosphorylations")
# print("\tRelative Percentages of Single PTMs")
# print("\t" * 2 + "Deamidations = {0:.0%}".format(Deamidation_count/One_ptm_count))
# print("\t" * 2 + "Oxidations = {0:.0%}".format(Oxidation_count/One_ptm_count))
# print("\t" * 2 + "Pyro-glu from Q = {0:.0%}".format(Pyro_glu_count/One_ptm_count))
# print("\t" * 2 + "Carbamidomethylations = {0:.0%}".format(Carbamidomethylation_count/One_ptm_count))
# print("\t" * 2 + "Acetylations = {0:.0%}".format(Acetylation_count/One_ptm_count))
# print("\t" * 2 + "Phosphorylations = {0:.0%}".format(Phosphorylation_count/One_ptm_count))
# print("\t" * 2 + "Percentage of Single PTM Phosphorylations by Amino Acid Relative to Total Number of Phosphorylations")
# print("\t" * 3 + "Tyrosine = {0:.0%}".format(Tyrosine_phosphorylations/Phosphorylation_count))
# print("\t" * 3 + "Serine = {0:.0%}".format(Serine_phosphorylations/Phosphorylation_count))
# print("\t" * 3 + "Threonine = {0:.0%}".format(Threonine_phosphorylations/Phosphorylation_count))
# print("\t" * 2 + "Percentage of Phosphorylated PTMs by Amino Acid Relative to Total Number of Peptides")
# print("\t" * 3 + "Tyrosine = {0:.0%}".format(Tyrosine_phosphorylations/line_count))
# print("\t" * 3 + "Serine = {0:.0%}".format(Serine_phosphorylations/line_count))
# print("\t" * 3 + "Threonine = {0:.0%}".format(Threonine_phosphorylations/line_count))

# print("Number of Multiple PTMs = {}".format(str(Multiple_ptms_count)))
# print("Percentage of Multiple PTMs = {0:.0%}".format(Multiple_ptms_count/line_count))

Trypsinized_Lab_Assay_File = Working_directory + 'Presorted_formatted_aa_sequences.csv'

Lab_Assay_Trypsinized_Matrix = Determine_uniprot_aa_placement(AA_list, Trypsinized_Lab_Assay_File, Requested_aa,
   Requested_peptide_amino_end_start, Requested_peptide_carboxyl_end_finish)

for i in range(0,20):
    print(Lab_Assay_Trypsinized_Matrix[i])

max_lab_trypsinized_value = np.amax(Lab_Assay_Trypsinized_Matrix)

# graph_max = 800
Generate_heatmap(Lab_Assay_Trypsinized_Matrix, graph_max, Graph_font, graph_title, Graph_x_axis_label, Graph_y_axis_label)

Sums_of_Lab_Assay_Trypsinized_Matrix = [0 for i in range(Matrix_width)]
for m in range(0, Matrix_width):
   for n in range(0, 20):
       Sums_of_Lab_Assay_Trypsinized_Matrix[m] = Sums_of_Lab_Assay_Trypsinized_Matrix[m] + Lab_Assay_Trypsinized_Matrix[n][m]

for m in range(0, Requested_peptide_amino_end_start):
   for n in range(0, 20):
       Lab_Assay_Trypsinized_Probability_Matrix[n][m] = \
           Lab_Assay_Trypsinized_Matrix[n][m] / Sums_of_Lab_Assay_Trypsinized_Matrix[m]
for m in range(Requested_peptide_amino_end_start + 1, Matrix_width):
   for n in range(0, 20):
       Lab_Assay_Trypsinized_Probability_Matrix[n][m] = \
           Lab_Assay_Trypsinized_Matrix[n][m] / Sums_of_Lab_Assay_Trypsinized_Matrix[m]

max_lab_trypsinized_probability_value = np.amax(Lab_Assay_Trypsinized_Probability_Matrix)

graph_title = 'Lab Assay Prob Matrix for Trypsinized Peptide - Using ' + Requested_kinase + ' With ' + ptm_name + ' of ' + Requested_aa
graph_max = max_lab_trypsinized_probability_value
# graph_max = 0.1
Generate_heatmap(Lab_Assay_Trypsinized_Probability_Matrix, graph_max, Graph_font, graph_title, Graph_x_axis_label, Graph_y_axis_label)

with open(Trypsinized_assay_file) as Csv_file:
   Csv_reader = csv.reader(Csv_file, delimiter=',')
   for Row in Csv_reader:
       central_aa_total_search = Row[1]
       for i in range(1, len(central_aa_total_search)):
           if central_aa_total_search[i] == Requested_aa:
               Total_central_aas += 1

with open(Working_directory + 'Presorted_formatted_aa_sequences.csv') as Csv_file:
   Csv_reader = csv.reader(Csv_file, delimiter=',')
   for Row in Csv_reader:
       central_aa_total_search = Row[1]
       for i in range(1, len(central_aa_total_search)):
           if central_aa_total_search[i] == Requested_aa:
               Total_modified_central_aas += 1

probability_central_aa_is_modified = Total_modified_central_aas / Total_central_aas

for m in range(0, Requested_peptide_amino_end_start):
   for n in range(0, 20):
       # if UniProt_Trypsinized_Probability_Matrix[n][m] == 0:
       #    UniProt_Trypsinized_Probability_Matrix[n][m] = 0.00001
       Bayesian_Probability_Matrix[n][m] = \
       ((Lab_Assay_Trypsinized_Probability_Matrix[n][m] * probability_central_aa_is_modified)/UniProt_Trypsinized_Probability_Matrix[n][m])
       Bayesian_Probability_Matrix[n][m] = Bayesian_Probability_Matrix[n][m]
for m in range(Requested_peptide_amino_end_start + 1, Matrix_width):
   for n in range(0, 20):
       # if UniProt_Trypsinized_Probability_Matrix[n][m] == 0:
       #    UniProt_Trypsinized_Probability_Matrix[n][m] = 0.00001
       Bayesian_Probability_Matrix[n][m] = \
       ((Lab_Assay_Trypsinized_Probability_Matrix[n][m] *
           probability_central_aa_is_modified)/UniProt_Trypsinized_Probability_Matrix[n][m])


max_bayesian_value = np.amax(Bayesian_Probability_Matrix)

graph_title = 'Bayesian Prob Matrix for Trypsinized Peptide - Using ' + Requested_kinase + ' With ' + ptm_name + ' of ' + Requested_aa
graph_max = max_bayesian_value
# graph_max = 0.015
Generate_heatmap(Bayesian_Probability_Matrix, graph_max, Graph_font, graph_title, Graph_x_axis_label, Graph_y_axis_label)

Zero_PTMs_File.close()
One_PTM_File.close()
Multiple_PTMs_File.close()
Requested_residue_unmodified_file.close()
