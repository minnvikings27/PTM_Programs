

def screen_experimental_against_control(ProportionTeller_input_path,ProportionTeller_working_directory):

    import csv

    header_modified_file = True
    header_unmodified_file = True
    i = 0

    experimental_file = ProportionTeller_input_path + '/Experimental.csv'
    control_file = ProportionTeller_input_path + '/Control.csv'
    matched_post_control_filter_file = ProportionTeller_working_directory + '/Matched_Post_Control_Filter_File.csv'
    unmatched_post_control_filter_file = ProportionTeller_working_directory + '/Unmatched_Post_Control_Filter_File.csv'

    # dataFrame = pd.read_csv(experimental_file)

    match = False

    with open(matched_post_control_filter_file, 'w') as matched_post_control_csv_file:
        with open(unmatched_post_control_filter_file, 'w') as unmatched_post_control_csv_file:
            with open(experimental_file) as experimental_csv_file:
               experimental_csv_line = csv.reader(experimental_csv_file, delimiter=',')
               for experimental_csv_row in experimental_csv_line:
                   if header_modified_file == True:
                       header_modified_file = False
                   else:
                        with open(control_file) as control_csv_file:
                            control_csv_line = csv.reader(control_csv_file, delimiter=',')
                            for control_csv_row in control_csv_line:
                                if header_unmodified_file == True:
                                    header_unmodified_file = False
                                else:
                                    if experimental_csv_row[3] == control_csv_row[3]:

                                        match = True
                            if match == False:
                                unmatched_post_control_csv_file.write(experimental_csv_row[0])
                                unmatched_post_control_csv_file.write(',')
                                unmatched_post_control_csv_file.write(experimental_csv_row[1])
                                unmatched_post_control_csv_file.write(',')
                                unmatched_post_control_csv_file.write(experimental_csv_row[2])
                                unmatched_post_control_csv_file.write(',')
                                unmatched_post_control_csv_file.write(experimental_csv_row[3])
                                unmatched_post_control_csv_file.write(',')
                                unmatched_post_control_csv_file.write(experimental_csv_row[4])
                                unmatched_post_control_csv_file.write(',')
                                unmatched_post_control_csv_file.write(experimental_csv_row[5])
                                unmatched_post_control_csv_file.write('\n')
                                i = i + 1
                            else:
                                matched_post_control_csv_file.write(control_csv_row[0])
                                matched_post_control_csv_file.write(',')
                                matched_post_control_csv_file.write(control_csv_row[1])
                                matched_post_control_csv_file.write(',')
                                matched_post_control_csv_file.write(control_csv_row[2])
                                matched_post_control_csv_file.write(',')
                                matched_post_control_csv_file.write(control_csv_row[3])
                                matched_post_control_csv_file.write(',')
                                unmatched_post_control_csv_file.write(control_csv_row[4])
                                unmatched_post_control_csv_file.write(',')
                                matched_post_control_csv_file.write(control_csv_row[5])
                                matched_post_control_csv_file.write('\n')
                                match = False
    print(i)
