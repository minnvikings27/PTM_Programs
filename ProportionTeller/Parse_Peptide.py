# Parse_Peptide.py

def Parse_peaks_peptide(input_file, requested_aa, requested_peptide_amino_end_start,
                        requested_peptide_carboxyl_end_finish, requested_analysis_type):

    import csv
    import os

    Row_num = 0
    Raw_sequence_counter = 0
    k = 0

    Peptide_string = ''
    Peptide_sequence = ''
    PTM_AA_location = ''
    Unformatted_aa_string = ''

    #   Start of section that looks for the directory ~/PortionTeller (where ~ stands for the home directory)
    #   and if it can't find that home directory then it will create it.
    Home_directory = os.path.expanduser('~') + '/ProportionTeller/'
    Working_directory = Home_directory + 'Working_directory/'

    Presorted_unformatted_aa_sequences = open(Working_directory + 'Presorted_unformatted_aa_sequences.csv', 'w')

    Presorted_formatted_aa_sequences = open(Working_directory + 'Presorted_formatted_aa_sequences.csv', 'w')

    SERIOHL_KILR_output_file = open(Working_directory + 'SERIOHL_KILR_output_file.csv', 'w')

    input_file = Working_directory + 'Unmatched_Post_Control_Filter_File.csv'

    requested_analysis_type = 'Kalip'

    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            Row_num += 1
            raw_sequence = row[3]

            if row[21] != '':
                Actual_PTM = row[21]
                capture_all_ptms_in_line = Actual_PTM.split(";")

                Number_of_PTMs = len(capture_all_ptms_in_line)

                for i in range(1, Number_of_PTMs + 1):
                    Actual_PTM = capture_all_ptms_in_line[i - 1]
                    PTM_Data = Actual_PTM.split(":")
                    print(PTM_Data)
                    PTM_AA = PTM_Data[0]
                    print(PTM_AA)
                    PTM_AA_name = PTM_AA[0]
                    print(PTM_AA_name)
                    for j in range(1, len(PTM_AA)):
                        PTM_AA_location = PTM_AA_location + PTM_AA[j]
                        print(PTM_AA_location)
                    PTM_AA_location_int = int(PTM_AA_location)
                    PTM_AA_location = ''
                    PTM_Type = PTM_Data[1]
                    modification_made = row[21]
                    location_of_modified_aa = PTM_AA_location_int
                    modified_aa = PTM_AA_name
                    formatted_aa_string = ''

                    print(modified_aa)
                    print(requested_aa)

                    if modified_aa == requested_aa:
                        print('Matched aa Sequences')
                        if raw_sequence[1] == '.':
                            raw_sequence = raw_sequence[2:len(raw_sequence)]
                        else:
                            raw_sequence = raw_sequence[0:len(raw_sequence)]

                        if raw_sequence[len(raw_sequence) - 2] == '.':
                            raw_sequence = raw_sequence[0:len(raw_sequence)-2]
                        else:
                            raw_sequence = raw_sequence[0:len(raw_sequence)]

                        for m in range(0, len(raw_sequence)):
                            Raw_sequence_counter += 1
                            if raw_sequence[m].isalpha():
                                Peptide_sequence = Peptide_sequence + raw_sequence[m]
                        print(Peptide_sequence)
                        peptide_sequence_length = len(Peptide_sequence)
                        entire_peptide_sequence = Peptide_sequence

                        print(peptide_sequence_length)
                        print(entire_peptide_sequence)

                        # Set up the amino part of the modified peptide string
                        if requested_peptide_amino_end_start > location_of_modified_aa:
                            for n in range(0,
                                    (requested_peptide_amino_end_start - location_of_modified_aa + 1)):
                                formatted_aa_string = formatted_aa_string + '-'
                                Unformatted_aa_string = Unformatted_aa_string + ''
                            for n in range(0, location_of_modified_aa):
                                formatted_aa_string = formatted_aa_string + Peptide_sequence[n]
                        else:
                            for n in range(location_of_modified_aa - requested_peptide_amino_end_start - 1,
                                            location_of_modified_aa):
                                formatted_aa_string = formatted_aa_string + Peptide_sequence[n]

                        print('Set up the amino part of the modified peptide string')
                        print(Peptide_sequence)
                        print(formatted_aa_string)

                            # Set up the carboxyl part of the modified peptide string
                        requested_peptide_carboxyl_end_finish = int(requested_peptide_carboxyl_end_finish)
                        if requested_peptide_carboxyl_end_finish > \
                            (len(Peptide_sequence) - location_of_modified_aa):
                            for n in range(location_of_modified_aa, len(Peptide_sequence)):
                                formatted_aa_string = formatted_aa_string + Peptide_sequence[n]
                            for n in range(0, location_of_modified_aa + requested_peptide_carboxyl_end_finish
                                            - len(Peptide_sequence)):
                                formatted_aa_string = formatted_aa_string + '-'
                        else:
                            for n in range(location_of_modified_aa,
                                        location_of_modified_aa + requested_peptide_carboxyl_end_finish):
                                formatted_aa_string = formatted_aa_string + Peptide_sequence[n]

                        print('Formatted aa string:')
                        print(formatted_aa_string)

                        if (formatted_aa_string) != '':
                            print('In writing stage')
                            Presorted_formatted_aa_sequences.write('-')
                            Presorted_formatted_aa_sequences.write(',')
                            Presorted_formatted_aa_sequences.write(formatted_aa_string)
                            Presorted_formatted_aa_sequences.write('\n')
                            if requested_analysis_type == 'SERIOHL-KILR':
                                print('In seriohl-kilr section')
                                formatted_aa_string = formatted_aa_string[0:14] + \
                                    formatted_aa_string[15].lower() + formatted_aa_string[16:]
                                Unformatted_aa_string = formatted_aa_string.replace('-', '')
                                Presorted_unformatted_aa_sequences.write(Unformatted_aa_string)
                                Presorted_unformatted_aa_sequences.write('\n')

                        # SERIOHL_KILR_Reference_File = proportionteller_input_path + '/SERIOHL-KILR_directory/SERIOHL-KILR_Reference_File.csv'

                        # k = 0
                        # with open(SERIOHL_KILR_Reference_File, 'r') as csv_file:
                        #     csv_reader = csv.reader(csv_file, delimiter=',')
                        #     for sk_row in csv_reader:
                        #         k += 1
                        #        if k > 2:
                        #            # seriohl_kilr_peptide_string.write(row[2])
                        #             if Unformatted_aa_string in sk_row[11]:
                        #                 SERIOHL_KILR_output_file.write(Unformatted_aa_string)
                        #                 SERIOHL_KILR_output_file.write(',')
                        #                 SERIOHL_KILR_output_file.write(sk_row[11])
                        #                 SERIOHL_KILR_output_file.write(',')
                        #                 SERIOHL_KILR_output_file.write(sk_row[2])
                        #                 SERIOHL_KILR_output_file.write('\n')

                        PTM_AA_location = ''

            Raw_sequence_counter = 0
            Peptide_sequence = ''

        Peptide_sequence = ''

    return Peptide_string