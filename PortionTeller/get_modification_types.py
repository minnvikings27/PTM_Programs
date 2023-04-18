def gather_ptm_reactions():

    import csv
    import os

    ptm_mod_type = []
    string_segment_1 = []
    string_segment_2 = []

    header = True

    home_directory = os.path.expanduser('~') + '/Proportion_Teller'
    ppt_html_file = home_directory + '/Input_Files/ABL_PLUS_R1_protein-peptides.csv'

    with open(ppt_html_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if header is True:
                header = False
            else:
                if len(row[21]) > 0:
                    string_segment_1 = row[21].split(';')
                    # print(string_segment_1)
                    for i in range(0,len(string_segment_1)):
                        string_segment_2 = string_segment_1[i].split(':')
                        # print(string_segment_2[1])
                        if string_segment_2[1] not in ptm_mod_type:
                            ptm_mod_type.append(string_segment_2[1])

    ptm_mod_type = sorted(ptm_mod_type)
    return(ptm_mod_type)
