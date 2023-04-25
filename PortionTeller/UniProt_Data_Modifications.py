total_AA_in_UniProt_Data = [0]

def trypsinize_uniprot_string(requested_aa):

    # This function uses FASTA data that was already pulled down from the UniProt database and does an artificial
    # trypsin cleavage at the carboxylic end of whenever lysine or arginine residue is encounters.

    import csv
    import os

    in_silico_peptide = ''
    requested_aa_found_in_peptide = False

    home_directory = os.path.expanduser('~') + '/Proportion_Teller'

    reference_path = home_directory + '/Reference_Files/'

    output_path = home_directory + '/Output_Files/'

    FASTA_File = reference_path + 'FASTA_File.csv'

    trypsinized_uniprot_file = output_path + 'Trypsinized_UniProt.csv'

    with open(trypsinized_uniprot_file, 'w') as trypsinized_fasta_file:
        with open(FASTA_File,'r') as fasta_file:
            csv_reader = csv.reader(fasta_file, delimiter=',')
            for row in csv_reader:
                protein_accession_number = row[0]
                uniprot_protein_fasta = row[1]
                for i in range(0, len(uniprot_protein_fasta)):
                    in_silico_peptide = in_silico_peptide + uniprot_protein_fasta[i]
                    if uniprot_protein_fasta[i] == requested_aa:
                        requested_aa_found_in_peptide = True
                    if uniprot_protein_fasta[i] in ['K', 'R']:
                        if len(in_silico_peptide) > 5:
                            if requested_aa_found_in_peptide is True:
                                trypsinized_fasta_file.write(protein_accession_number)
                                trypsinized_fasta_file.write(',')
                                trypsinized_fasta_file.write(in_silico_peptide)
                                trypsinized_fasta_file.write('\n')
                                in_silico_peptide = ''
                                requested_aa_found_in_peptide = False
                            else:
                                in_silico_peptide = ''
                                requested_aa_found_in_peptide = False
        if len(in_silico_peptide) > 5:
            trypsinized_fasta_file.write(in_silico_peptide)
            trypsinized_fasta_file.write(',')
            trypsinized_fasta_file.write(protein_accession_number)
            trypsinized_fasta_file.write('\n')
    trypsinized_fasta_file.close()
    fasta_file.close()
    return(trypsinized_fasta_file)


def create_accession_numbers_file(input_file):

    import csv
    import os

    list_of_all_files_in_dir = []
    valid_csv_files = []
    current_file_name = ''



    prior_protein_accession_number = ''

    home_directory = os.path.expanduser('~') + '/Proportion_Teller'

    input_path = home_directory + '/Input_Files/'

    output_path = home_directory + '/Output_Files/'

    output_accession_numbers_file = output_path + '/Protein_Accession_Numbers.csv'

    unique_protein_accession_numbers = open(output_accession_numbers_file, 'w')

    list_of_all_files_in_dir = os.listdir(input_path)

    for i in range(0, len(list_of_all_files_in_dir)):
        current_file_name = list_of_all_files_in_dir[i]
        if current_file_name[-4] == '.' and current_file_name[-3] == 'c' and current_file_name[-2] == 's' and current_file_name[-1] == 'v':
            valid_csv_files.append(current_file_name)

    for i in range(0, len(valid_csv_files)):
        input_file = input_path + '/' + valid_csv_files[i]



        with open(input_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                protein_accession_full = row[2].split('|')
                if protein_accession_full[0] == 'tr' or protein_accession_full[0] == 'sp':
                    protein_accession_number = protein_accession_full[1]
                else:
                    protein_accession_number = protein_accession_full[0]
                if protein_accession_number != prior_protein_accession_number:
                    unique_protein_accession_numbers.write(protein_accession_number)
                    unique_protein_accession_numbers.write('\n')
                    prior_protein_accession_number = protein_accession_number
                print(protein_accession_number)

        unique_protein_accession_numbers.close()

    return output_accession_numbers_file


def modify_fasta_reference_file(accession_numbers_file):

    import requests
    import csv
    import os

    list_of_all_files_in_dir = []
    valid_csv_files = []
    current_file_name = ''

    home_directory = os.path.expanduser('~')

    reference_file_path = home_directory + '/Proportion_Teller/Reference_Files'

    output_accession_numbers_file = reference_file_path + '/Unique_Protein_Accession_Numbers.csv'

    unique_protein_accession_numbers = open(output_accession_numbers_file, 'w')

    prior_protein_accession_number = ''

    home_directory = os.path.expanduser('~')

    reference_file_path = home_directory + '/Proportion_Teller/Reference_Files'

    fasta_file = reference_file_path + '/FASTA_File.csv'

    fasta_dictionary = {"Accession": []}

    with open(fasta_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            fasta_dictionary[row[0]] = row[1]
    fasta_file = open(fasta_file, 'a')
    with open(accession_numbers_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            protein_accession_number = row[0]
            if protein_accession_number not in fasta_dictionary:
                uniprot_request_url = "http://www.uniprot.org/uniprot/"
                r = requests.get(uniprot_request_url + protein_accession_number + ".fasta")
                uniprot_responsebody = r.text
                uniprot_fasta = ''
                header = True
                for m in range(0, len(uniprot_responsebody)):
                    if header is False and uniprot_responsebody[m].isalpha():
                        uniprot_fasta = uniprot_fasta + uniprot_responsebody[m]
                    if uniprot_responsebody[m] == '=' and uniprot_responsebody[m - 1] == 'V' and \
                            uniprot_responsebody[m - 2] == 'S':
                        header = False
                fasta_file.write(protein_accession_number)
                fasta_file.write(',')
                fasta_file.write(uniprot_fasta)
                fasta_file.write('\n')

    return fasta_file


def determine_uniprot_aa_placement(AA_list, input_file, central_aa, requested_peptide_amino_end_start,
    requested_peptide_carboxyl_end_finish):

    import csv

    #CHANGE THESE WHEN FILE TRANSFER OF DATA IS COMPLETED
    # requested_peptide_amino_end_start = 4
    # requested_peptide_carboxyl_end_finish = 4
    # central_aa = 'Y'

    i = 0

    matrix_width = requested_peptide_amino_end_start + requested_peptide_carboxyl_end_finish + 1

    UniProt_AA_locations = [[0 for i in range(matrix_width)] for i in range(20)]

    central_aa_count = 0

    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            peptide_sequence = row[1]
            peptide_sequence = '^^^^^^^^^^^^^^^^^^^^^^^' + peptide_sequence + '^^^^^^^^^^^^^^^^^^^^^^^^^^'
            requested_peptide_amino_end_start = int(requested_peptide_amino_end_start)
            requested_peptide_carboxyl_end_finish = int(requested_peptide_carboxyl_end_finish)

            for i in range(0, len(peptide_sequence)):
                if peptide_sequence[i] == central_aa:
                        central_aa_count += 1
                        central_aa_position = i
                        for j in range(0, 20):
                            for k in range(0, requested_peptide_amino_end_start):
                                if peptide_sequence[central_aa_position - k - 1] == AA_list[j]:
                                    UniProt_AA_locations[j][requested_peptide_amino_end_start-k-1] += 1
                            for k in range(0, requested_peptide_carboxyl_end_finish):
                                if peptide_sequence[central_aa_position + k + 1] == AA_list[j]:
                                    UniProt_AA_locations[j][requested_peptide_amino_end_start+k+1] += 1

            total_AA_in_UniProt_Data[0] += 1

    return UniProt_AA_locations