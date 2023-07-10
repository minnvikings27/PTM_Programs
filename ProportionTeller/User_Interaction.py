
def gather_user_input():

    # import customtkinter


    modification_type = ['Phosphorylation (STY)', 'Oxidation (M)', 'Carbamidomethylation', 'Deamidation (NQ)',
                         'Acetylation (Protein N-term)', 'Pyro-glu from Q-Q']

    modified_amino_acid =  ['Tyrosine', 'Serine', 'Threonine', 'Methionine', 'Argenine', 'Glutamine', 'Alanine',
                            'Cysteine', 'Aspartate', 'Glutamate', 'Phenylalanine', 'Glycine', 'Histidine',
                            'Isoleucine', 'Lysine', 'Leucine', 'Asparagine', 'Proline', 'Valine', 'Tryptophan']

    modifier = ['ABL', 'MER', 'TYRO3', 'CDK25', 'P25', 'P35']

    amino_side_positions = ['-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', '-10', '-11', '-12', '-13', '-14',
                            '-15', '-16', '-17', '-18', '-19', '-20']

    carboxyl_side_positions = ['+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10', '+11', '+12', '+13', '+14',
                               '+15', '+16', '+17', '+18', '+19', '+20']

    assay_type = ['Kalip', 'SERIOHL-KILR']

    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('blue')
    root = customtkinter.CTk()
    root.geometry('300x450')
    root.title('PortionTeller 1.0')

    def modification_type_response(choice1):

        modification_type_response.req_ptm = choice1
        if modification_type_response.req_ptm == 'Phosphorylation (STY)':
            modification_type_response.req_ptm = 'P'
        if modification_type_response.req_ptm == 'Oxidation (M)':
            modification_type_response.req_ptm = 'O'
        if modification_type_response.req_ptm == 'Carbamidomethylation':
            modification_type_response.req_ptm = 'C'
        if modification_type_response.req_ptm == 'Deamidation (NQ)':
            modification_type_response.req_ptm = 'D'
        if modification_type_response.req_ptm == 'Acetylation (Protein N-term)':
            modification_type_response.req_ptm = 'A'
        if modification_type_response.req_ptm == 'Pyro-glu from Q-Q':
            modification_type_response.req_ptm = 'Q'

    def amino_acid_type_response(choice2):
        amino_acid_type_response.req_aa = choice2
        if amino_acid_type_response.req_aa == 'Tyrosine':
            amino_acid_type_response.req_aa = 'Y'
        if amino_acid_type_response.req_aa == 'Serine':
            amino_acid_type_response.req_aa = 'S'
        if amino_acid_type_response.req_aa == 'Threonine':
            amino_acid_type_response.req_aa = 'T'
        if amino_acid_type_response.req_aa == 'Methionine':
            amino_acid_type_response.req_aa = 'M'
        if amino_acid_type_response.req_aa == 'Argenine':
            amino_acid_type_response.req_aa = 'R'
        if amino_acid_type_response.req_aa == 'Glutamine':
            amino_acid_type_response.req_aa = 'Q'
        if amino_acid_type_response.req_aa == 'Alanine':
            amino_acid_type_response.req_aa = 'A'
        if amino_acid_type_response.req_aa == 'Cysteine':
            amino_acid_type_response.req_aa = 'C'
        if amino_acid_type_response.req_aa == 'Aspartate':
            amino_acid_type_response.req_aa = 'D'
        if amino_acid_type_response.req_aa == 'Glutamate':
            amino_acid_type_response.req_aa = 'E'
        if amino_acid_type_response.req_aa == 'Phenylalanine':
            amino_acid_type_response.req_aa = 'F'
        if amino_acid_type_response.req_aa == 'Glycine':
            amino_acid_type_response.req_aa = 'G'
        if amino_acid_type_response.req_aa == 'Histidine':
            amino_acid_type_response.req_aa = 'H'
        if amino_acid_type_response.req_aa == 'Isoleucine':
            amino_acid_type_response.req_aa = 'I'
        if amino_acid_type_response.req_aa == 'Lysine':
            amino_acid_type_response.req_aa = 'K'
        if amino_acid_type_response.req_aa == 'Leucine':
            amino_acid_type_response.req_aa = 'L'
        if amino_acid_type_response.req_aa == 'Asparagine':
            amino_acid_type_response.req_aa = 'N'
        if amino_acid_type_response.req_aa == 'Proline':
            amino_acid_type_response.req_aa = 'P'
        if amino_acid_type_response.req_aa == 'Valine':
            amino_acid_type_response.req_aa = 'V'
        if amino_acid_type_response.req_aa == 'Tryptophan':
            amino_acid_type_response.req_aa = 'W'
    def assign_requested_kinase(choice3):
        assign_requested_kinase.requested_kinase = choice3
    def assign_requested_control(choice4):
        assign_requested_control.requested_control = choice4
    def assign_requested_replicate(choice5):
        assign_requested_replicate.requested_replicate = choice5
    def assign_requested_amino_side_start(choice6):
        assign_requested_amino_side_start.requested_amino_side_start = int(choice6)
    def assign_requested_carboxyl_side_start(choice7):
        assign_requested_carboxyl_side_start.requested_carboxyl_side_start = int(choice7)
    def assign_requested_carboxyl_side_start(choice8):
        assign_requested_carboxyl_side_start.requested_carboxyl_side_start = choice8
    def assign_requested_analysis_type(choice9):
        assign_requested_analysis_type.requested_analysis_type = choice9

    modification_type_response.req_ptm = ''
    amino_acid_type_response.req_aa = ''
    assign_requested_kinase.requested_kinase = ''
    assign_requested_control.requested_control = ''
    assign_requested_replicate.requested_replicate = ''
    assign_requested_amino_side_start.requested_amino_side_start = ''
    assign_requested_carboxyl_side_start.requested_carboxyl_side_start = ''
    assign_requested_analysis_type.requested_analysis_type = ''

    optionmenu_1 = customtkinter.CTkOptionMenu(master=root, values=modification_type,
            command=modification_type_response)
    optionmenu_1.pack(pady=12, padx=10)
    optionmenu_1.set('Mod Type - Default Phosphorylation')

    optionmenu_2 = customtkinter.CTkOptionMenu(master=root, values=modified_amino_acid,
            command=amino_acid_type_response)
    # modification_type_response.req_ptm = customtkinter.StringVar(value='Phosphorylation (STY)')
    optionmenu_2.pack(pady=10, padx=10)
    optionmenu_2.set('Modified AA - Default Serine')

    optionmenu_3 = customtkinter.CTkOptionMenu(master=root, values=modifier,
            command=assign_requested_kinase)
    # modification_type_response.req_ptm = customtkinter.StringVar(value='Phosphorylation (STY)')
    optionmenu_3.pack(pady=10, padx=10)
    optionmenu_3.set('Modifier - Default P25')

    optionmenu_4 = customtkinter.CTkOptionMenu(master=root, values=['Yes', 'No'],
            command=assign_requested_control)
    # modification_type_response.req_ptm = customtkinter.StringVar(value='Phosphorylation (STY)')
    optionmenu_4.pack(pady=10, padx=10)
    optionmenu_4.set('Screen Against Control?')

    optionmenu_5 = customtkinter.CTkOptionMenu(master=root, values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            command=assign_requested_replicate)
    # modification_type_response.req_ptm = customtkinter.StringVar(value='Phosphorylation (STY)')
    optionmenu_5.pack(pady=10, padx=10)
    optionmenu_5.set('Replicate Number')

    optionmenu_6 = customtkinter.CTkOptionMenu(master=root, values=amino_side_positions,
            command=assign_requested_amino_side_start)
    # modification_type_response.req_ptm = customtkinter.StringVar(value='Phosphorylation (STY)')
    optionmenu_6.pack(pady=10, padx=10)
    optionmenu_6.set('N Side Positions - Default -4')

    optionmenu_7 = customtkinter.CTkOptionMenu(master=root, values=carboxyl_side_positions,
            command=assign_requested_carboxyl_side_start)
    # modification_type_response.req_ptm = customtkinter.StringVar(value='Phosphorylation (STY)')
    optionmenu_7.pack(pady=10, padx=10)
    optionmenu_7.set('C Side Positions - Default +4')

    optionmenu_8 = customtkinter.CTkOptionMenu(master=root, values=assay_type,
            command=assign_requested_analysis_type)
    # modification_type_response.req_ptm = customtkinter.StringVar(value='Phosphorylation (STY)')
    optionmenu_8.pack(pady=10, padx=10)
    optionmenu_8.set('Assay - Default Kalip')


    # req_left_pep_start = customtkinter.StringVar()
    # entry1 = customtkinter.CTkEntry(master=root, placeholder_text='How Many N Side?')
    # entry1.pack(pady=10, padx=10)
    # req_left_pep_start = entry1.get()
    # print(entry1.get())

    # entry2 = customtkinter.CTkEntry(master=root, placeholder_text='How Many C Side?')
    # entry2.pack(pady=10, padx=10)
    # req_right_pep_start = entry2.get()

    button_1 = customtkinter.CTkButton(master=root, text='Run', command=root.destroy)
    button_1.pack(pady=10, padx=10)

    # checkbox = customtkinter.CTkCheckBox(master=frame, text='Remember me!')
    # checkbox.pack(pady=12, padx=10)

    root.mainloop()

    if modification_type_response.req_ptm == '':
        modification_type_response.req_ptm = 'P'
    if amino_acid_type_response.req_aa == '':
        amino_acid_type_response.req_aa = 'S'
    if assign_requested_kinase.requested_kinase == '':
        assign_requested_kinase.requested_kinase = 'P25'
    if assign_requested_control.requested_control == '':
        assign_requested_control.requested_control = 'PLUS'
    if assign_requested_control.requested_control == 'Yes':
        assign_requested_control.requested_control = 'PLUS'
    if assign_requested_replicate.requested_replicate == '':
        assign_requested_replicate.requested_replicate = '0'
    assign_requested_replicate.requested_replicate = 'R' + assign_requested_replicate.requested_replicate
    if assign_requested_amino_side_start.requested_amino_side_start == '':
        assign_requested_amino_side_start.requested_amino_side_start = '-4'
    if assign_requested_carboxyl_side_start.requested_carboxyl_side_start == '':
        assign_requested_carboxyl_side_start.requested_carboxyl_side_start = '+4'
    if assign_requested_analysis_type.requested_analysis_type == '':
        assign_requested_analysis_type.requested_analysis_type = 'Standard'

    return modification_type_response.req_ptm, \
                amino_acid_type_response.req_aa, \
                    assign_requested_kinase.requested_kinase, \
                        assign_requested_control.requested_control, \
                            assign_requested_replicate.requested_replicate, \
                                assign_requested_amino_side_start.requested_amino_side_start, \
                                    assign_requested_carboxyl_side_start.requested_carboxyl_side_start, \
                                        assign_requested_analysis_type.requested_analysis_type