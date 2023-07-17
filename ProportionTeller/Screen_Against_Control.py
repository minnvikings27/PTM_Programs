

def Screen_experimental_against_control(Input_directory,Working_directory):

    import csv

    Header_modified_file = True
    Header_unmodified_file = True
    i = 0

    Experimental_file = Input_directory + 'Experimental.csv'
    Control_file = Input_directory + 'Control.csv'
    Matched_post_control_filter_file = Working_directory + 'Matched_Post_Control_Filter_File.csv'
    Unmatched_post_control_filter_file = Working_directory + 'Unmatched_Post_Control_Filter_File.csv'

    # dataFrame = pd.read_csv(experimental_file)

    Match = False

    with open(Matched_post_control_filter_file, 'w') as Matched_post_control_csv_file:
        with open(Unmatched_post_control_filter_file, 'w') as Unmatched_post_control_csv_file:
            with open(Experimental_file) as Experimental_csv_file:
               Experimental_csv_line = csv.reader(Experimental_csv_file, delimiter=',')
               for Experimental_csv_row in Experimental_csv_line:
                   if Header_modified_file == True:
                       Header_modified_file = False
                   else:
                        with open(Control_file) as Control_csv_file:
                            Control_csv_line = csv.reader(Control_csv_file, delimiter=',')
                            for Control_csv_row in Control_csv_line:
                                if Header_unmodified_file == True:
                                    Header_unmodified_file = False
                                else:
                                    if Experimental_csv_row[3] == Control_csv_row[3]:
                                        Match = True
                            if Match == False:
                                for i in range(0, 23):
                                    Unmatched_post_control_csv_file.write(Experimental_csv_row[i])
                                    Unmatched_post_control_csv_file.write(',')
                                Unmatched_post_control_csv_file.write('\n')
                                i = i + 1
                            else:
                                for i in range(0, 23):
                                    Matched_post_control_csv_file.write(Control_csv_row[i])
                                    Matched_post_control_csv_file.write(',')
                                Matched_post_control_csv_file.write('\n')
                                Match = False

    return()
