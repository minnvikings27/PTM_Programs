def parse_peaks_peptide(input_file, requested_aa, requested_peptide_amino_end_start,
                        requested_peptide_carboxyl_end_finish, requested_analysis_type):

    import csv
    import os

    row_num = 0
    raw_sequence_counter = 0
    k = 0

    peptide_string = ''
    peptide_sequence = ''
    PTM_AA_location = ''
    unformatted_aa_string = ''

    header = True

    #   Start of section that looks for the directory ~/PortionTeller (where ~ stands for the home directory)
    #   and if it can't find that home directory then it will create it.
    home_directory = os.path.expanduser('~')
    proportionteller_home_path = home_directory + '/Proportion_Teller'

    if os.path.exists(proportionteller_home_path) is False:
        print('Making PortionTeller directory')
        os.mkdir(proportionteller_home_path)

    proportionteller_output_path = proportionteller_home_path + '/Output_Files'

    if os.path.exists(proportionteller_output_path) is False:
        os.mkdir(proportionteller_output_path)
    #   End of section that looks for and if necessary makes the PortionTeller directory

    unformatted_trypsinized_lab_assay_file = open(proportionteller_output_path + '/pre_sorted_unformatted_Trypsinized_Lab_Assay.csv', 'w')

    formatted_trypsinized_lab_assay_file = open(proportionteller_output_path + '/pre_sorted_formatted_Trypsinized_Lab_Assay.csv', 'w')

    SERIOHL_KILR_output_file = open(proportionteller_output_path + '/SERIOHL_KILR_output_file.csv', 'w')


    input_file = '/Users/miltonandrews/Proportion_Teller/Input_Files/ABL_PLUS_R1_protein-peptides.csv'

    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row_num += 1
            raw_sequence = row[3]
            if header == False:
                if row[21] != '':
                    Actual_PTM = row[21]
                    capture_all_ptms_in_line = Actual_PTM.split(";")
                    Number_of_PTMs = len(capture_all_ptms_in_line)
                    for i in range(1, Number_of_PTMs + 1):
                        Actual_PTM = capture_all_ptms_in_line[i - 1]
                        PTM_Data = Actual_PTM.split(":")
                        PTM_AA = PTM_Data[0]
                        PTM_AA_name = PTM_AA[0]
                        for j in range(1, len(PTM_AA)):
                            PTM_AA_location = PTM_AA_location + PTM_AA[j]
                        PTM_AA_location_int = int(PTM_AA_location)
                        PTM_AA_location = ''
                        PTM_Type = PTM_Data[1]
                        modification_made = row[21]
                        location_of_modified_aa = PTM_AA_location_int
                        modified_aa = PTM_AA_name
                        formatted_aa_string = ''
                        if modified_aa == requested_aa:
                            if raw_sequence[1] == '.':
                                raw_sequence = raw_sequence[2:len(raw_sequence)]
                            else:
                                raw_sequence = raw_sequence[0:len(raw_sequence)]
                            if raw_sequence[len(raw_sequence) - 2] == '.':
                                raw_sequence = raw_sequence[0:len(raw_sequence)-2]
                            else:
                                raw_sequence = raw_sequence[0:len(raw_sequence)]
                            for m in range(0, len(raw_sequence)):
                                raw_sequence_counter += 1
                                if raw_sequence[m].isalpha():
                                    peptide_sequence = peptide_sequence + raw_sequence[m]
                            peptide_sequence_length = len(peptide_sequence)
                            entire_peptide_sequence = peptide_sequence

                            # Set up the amino part of the modified peptide string
                            if requested_peptide_amino_end_start > location_of_modified_aa:
                                for n in range(0,
                                        (requested_peptide_amino_end_start - location_of_modified_aa + 1)):
                                    formatted_aa_string = formatted_aa_string + '-'
                                    unformatted_aa_string = unformatted_aa_string + ''
                                for n in range(0, location_of_modified_aa):
                                    formatted_aa_string = formatted_aa_string + peptide_sequence[n]
                            else:
                                for n in range(location_of_modified_aa - requested_peptide_amino_end_start - 1,
                                                location_of_modified_aa):
                                    formatted_aa_string = formatted_aa_string + peptide_sequence[n]

                                # Set up the carboxyl part of the modified peptide string
                            requested_peptide_carboxyl_end_finish = int(requested_peptide_carboxyl_end_finish)
                            if requested_peptide_carboxyl_end_finish > \
                                (len(peptide_sequence) - location_of_modified_aa):
                                for n in range(location_of_modified_aa, len(peptide_sequence)):
                                    formatted_aa_string = formatted_aa_string + peptide_sequence[n]
                                for n in range(0, location_of_modified_aa + requested_peptide_carboxyl_end_finish
                                                - len(peptide_sequence)):
                                    formatted_aa_string = formatted_aa_string + '-'
                            else:
                                for n in range(location_of_modified_aa,
                                            location_of_modified_aa + requested_peptide_carboxyl_end_finish):
                                    formatted_aa_string = formatted_aa_string + peptide_sequence[n]

                            if (formatted_aa_string) != '':
                                formatted_trypsinized_lab_assay_file.write('-')
                                formatted_trypsinized_lab_assay_file.write(',')
                                formatted_trypsinized_lab_assay_file.write(formatted_aa_string)
                                formatted_trypsinized_lab_assay_file.write('\n')
                                if requested_analysis_type == 'SERIOHL-KILR':
                                    formatted_aa_string = formatted_aa_string[0:14] + \
                                        formatted_aa_string[15].lower() + formatted_aa_string[16:]
                                    unformatted_aa_string = formatted_aa_string.replace('-', '')
                                    unformatted_trypsinized_lab_assay_file.write(unformatted_aa_string)
                                    unformatted_trypsinized_lab_assay_file.write('\n')

                            proportionteller_input_path = proportionteller_home_path + '/Input_Files'

                            if os.path.exists(proportionteller_input_path) is False:
                                os.mkdir(proportionteller_input_path)

                            # SERIOHL_KILR_Reference_File = proportionteller_input_path + '/SERIOHL-KILR_directory/SERIOHL-KILR_Reference_File.csv'

                            # k = 0
                            # with open(SERIOHL_KILR_Reference_File, 'r') as csv_file:
                            #     csv_reader = csv.reader(csv_file, delimiter=',')
                            #     for sk_row in csv_reader:
                            #         k += 1
                            #        if k > 2:
                            #            # seriohl_kilr_peptide_string.write(row[2])
                            #             if unformatted_aa_string in sk_row[11]:
                            #                 SERIOHL_KILR_output_file.write(unformatted_aa_string)
                            #                 SERIOHL_KILR_output_file.write(',')
                            #                 SERIOHL_KILR_output_file.write(sk_row[11])
                            #                 SERIOHL_KILR_output_file.write(',')
                            #                 SERIOHL_KILR_output_file.write(sk_row[2])
                            #                 SERIOHL_KILR_output_file.write('\n')

                            PTM_AA_location = ''

                raw_sequence_counter = 0

                peptide_sequence = ''

            header = False

        peptide_sequence = ''

    return peptide_string