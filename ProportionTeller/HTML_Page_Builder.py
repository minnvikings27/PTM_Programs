amino_acids_list = ['Tyrosine', 'Serine', 'Threonine', 'Alanine', 'Arginine', 'Asparagine', 'Aspartate',
                    'Cysteine', 'Glutamate', 'Glutamine', 'Glycine', 'Histidine', 'Isoleucine', 'Leucine',
                    'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Tryptophan', 'Valine']


amino_acids_one_letter_list = ['Y', 'S', 'T', 'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K',
                               'M', 'F', 'P', 'W', 'V']


def build_html_page():

    import os
    from get_modification_types import gather_ptm_reactions

    i = 0
    j = 0

    # ptm_modifier_input = []

    # current_ptm = []

    ptm_modifiers = []

    home_directory = os.path.expanduser('~') + '/ProportionTeller'

    input_path = home_directory + '/Input_Files/'

    ptm_modifier_file = input_path + 'PTM_Modifiers.txt'

    proportion_teller_html_path = home_directory + '/HTML_Files/'

    ptm_reactions = gather_ptm_reactions()

    with open(ptm_modifier_file) as f:
        ptm_modifier_input = f.readlines()

    # remove new line characters
    ptm_modifier_input = [x.strip() for x in ptm_modifier_input]

    for i in range (0, len(ptm_modifier_input)):
        current_ptm = ptm_modifier_input[i]
        if current_ptm[0] != '#':
            ptm_modifiers.append(ptm_modifier_input[i])
    # print(ptm_modifiers)

    ppt_html_page = proportion_teller_html_path + 'Proportion_Teller_User_Input.html'
    ppt_html_file = open(ppt_html_page, 'w')

    # ***************** Web Page Code Begins Here *****************

    ppt_html_file.write('<html>\n')
    ppt_html_file.write('<head>\n')
    ppt_html_file.write('<title>  Proportion Teller </title>\n')
    ppt_html_file.write('</head>\n')
    ppt_html_file.write('<style>\n')
    ppt_html_file.write('body {background-color: rebeccapurple;}\n')
    ppt_html_file.write('h1 {color: yellow;}\n')
    ppt_html_file.write('h1 {text-align: center;}\n')
    ppt_html_file.write('</style>\n')
    ppt_html_file.write('<body>\n')
    ppt_html_file.write('<h1>\n')
    ppt_html_file.write('Proportion Teller\n')
    ppt_html_file.write('</h1>\n')


    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:100px; top:150px; color: yellow\">\n')
    ppt_html_file.write('</div>\n')

    ppt_html_file.write('<label> Modified amino acid(s) </label> <br>\n')
    for i in range(0,len(amino_acids_list)):
        ppt_html_file.write('<input type = \"checkbox\" id = \"' + amino_acids_list[i] + '\" name = \"' +
                            amino_acids_list[i] + '\" value = \"' + amino_acids_list[i] + '\">\n')
        ppt_html_file.write('<label for=\"' + amino_acids_list[i] + '\">' + amino_acids_list[i] + '</label>\n')
        ppt_html_file.write('<br>\n')

    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:350px; top:150px;\">\n')
    ppt_html_file.write('</div>\n')
    ppt_html_file.write('<label> PTM Reaction(s) </label> <br>\n')

    for i in range(0,len(ptm_reactions)):
        ppt_html_file.write('<input type = \"checkbox\" id = \"' + ptm_reactions[i] + '\" name = \"' +
                            ptm_reactions[i] + '\" value = \"' + ptm_reactions[i] + '\">\n')
        ppt_html_file.write('<label for=\"' + ptm_reactions[i] + '\">' + ptm_reactions[i] + '</label>\n')
        ppt_html_file.write('<br>\n')


    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:600px; top:150px;\">\n')
    ppt_html_file.write('</div>\n')
    ppt_html_file.write('<label for=\"amino_side_location\"> Amino Side Location:</label>\n')
    ppt_html_file.write('<select name = \"amino_side_location\" id=\"amino_side_location\">\n')

    for i in range(1,21):
        j = -1 * i
        ppt_html_file.write('<option value = \"' + str(j) + '\">' + str(j) + '</option>\n')
    ppt_html_file.write('</select>\n')

    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:850px; top:150px;\">\n')
    ppt_html_file.write('</div>\n')
    ppt_html_file.write('<label for=\"carboxyl_side_location\"> Carboxyl Side Location:</label>\n')
    ppt_html_file.write('<select name = \"carboxyl_side_location\" id=\"carboxyl_side_location\">\n')

    for i in range(1,21):
        ppt_html_file.write('<option value = \"' + str(i) + '\">' + str(i) + '</option>\n')
    ppt_html_file.write('</select>\n')

    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:1100px; top:150px;\">\n')
    ppt_html_file.write('</div>\n')
    ppt_html_file.write('<label for=\"a_score_cutoff\"> A Score Cutoff:</label>\n')
    ppt_html_file.write('<select name = \"a_score_cutoff\" id=\"a_score_cutoff\">\n')

    for i in range(0,21):
        j = 5 * i
        ppt_html_file.write('<option value = \"' + str(j) + '\">' + str(j) + '</option>\n')
    ppt_html_file.write('</select>\n')



    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:1300px; top:150px;\">\n')
    ppt_html_file.write('</div>\n')
    ppt_html_file.write('<label for=\"ptm_modifier\"> PTM Modifier:</label>\n')
    ppt_html_file.write('<select name = \"ptm_modifier\" id=\"ptm_modifier\">\n')

    for i in range(0,len(ptm_modifiers)):
        ppt_html_file.write('<option value = \"' + ptm_modifiers[i] + '\">' + ptm_modifiers[i] + '</option>\n')
    ppt_html_file.write('</select>\n')

    ppt_html_file.write('</body>\n')

    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:800px; top:800px;\">\n')
    # ppt_html_file.write('</div>\n')

    # ppt_html_file.write('<button id =\"submit\">Submit</button>')
    # ppt_html_file.write('<b id=\"submit\"></b>')

    # ppt_html_file.write('<div>\n')

    ppt_html_file.write('<input type=\"button\" id=\"bt\" value=\"Run Analysis\" onclick=\"saveFile()\"/>\n')

    ppt_html_file.write('</div>\n')




    # ***************** Java script coding begins here *****************

    ppt_html_file.write('<script>\n')

    # ppt_html_file.write('const x = document.getElementById(\"submit\")\n')

    ppt_html_file.write('const amino_acids = [];\n')

    # ppt_html_file.write('x.addEventListener(\"click\", getCheckboxValue)\n')

    ppt_html_file.write('let saveFile = () => {\n')

    ppt_html_file.write('var amino_acids = \"\";\n')
    for i in range (0, len(amino_acids_list)):
        ppt_html_file.write('if (document.getElementById(\"' + amino_acids_list[i] + '\").checked === true) {\n')
        ppt_html_file.write('amino_acids = amino_acids + \"' + amino_acids_one_letter_list[i] + '\";\n')
        ppt_html_file.write('}\n')

    ppt_html_file.write('var ptm_reaction_type = \"\";\n')
    for i in range(0,len(ptm_reactions)):
        ppt_html_file.write('if (document.getElementById(\"' + ptm_reactions[i] + '\").checked === true) {\n')
        ppt_html_file.write('ptm_reaction_type = ptm_reaction_type + \"' + ptm_reactions[i] + '\";\n')
        ppt_html_file.write('}\n')

    ppt_html_file.write('var e = document.getElementById(\"amino_side_location\");\n')
    ppt_html_file.write('var value = e.value;\n')
    ppt_html_file.write('var amino_side_location = e.options[e.selectedIndex].text;\n')

    ppt_html_file.write('var e = document.getElementById(\"carboxyl_side_location\");\n')
    ppt_html_file.write('var value = e.value;\n')
    ppt_html_file.write('var carboxyl_side_location = e.options[e.selectedIndex].text;\n')

    ppt_html_file.write('var e = document.getElementById(\"a_score_cutoff\");\n')
    ppt_html_file.write('var value = e.value;\n')
    ppt_html_file.write('var a_score_cutoff = e.options[e.selectedIndex].text;\n')

    ppt_html_file.write('var e = document.getElementById(\"ptm_modifier\");\n')
    ppt_html_file.write('var value = e.value;\n')
    ppt_html_file.write('var ptm_modifier = e.options[e.selectedIndex].text;\n')

    ppt_html_file.write('document.getElementById(\"bt\").innerHTML +=\n')
    ppt_html_file.write('amino_acids + \",\" + ptm_reaction_type + \",\" + ptm_modifier + \",\" + amino_side_location + \",\" + a_score_cutoff + \",\" + carboxyl_side_location;\n')

    ppt_html_file.write('total_csv_data = amino_acids + \",\" + ptm_reaction_type + \",\" + ptm_modifier + \",\" + amino_side_location + \",\" + a_score_cutoff + \",\" + carboxyl_side_location;\n')
    ppt_html_file.write('var csv = total_csv_data;\n')

    ppt_html_file.write('const link = document.createElement(\"a\");')
    ppt_html_file.write('const textToBLOB = new Blob([csv], {type:\'text/plain\'});\n')
    ppt_html_file.write('link.href = URL.createObjectURL(textToBLOB);')
    ppt_html_file.write('link.download = \'/Users/miltonandrews/ProportionTeller/Input_Files/User_Response_File.csv\';\n')
    ppt_html_file.write('link.click();')
    ppt_html_file.write('URL.revokeObjectURL(link.href);')
    # ppt_html_file.write('var a2 = document.getElementById("download_button");\n')
    # ppt_html_file.write('a2.href = URL.createObjectURL(data);\n')

    ppt_html_file.write('let newLink = document.createElement(\"a2\");\n')
    ppt_html_file.write('newLink.download = sFileName;\n')

    ppt_html_file.write('if (window.webkitURL != null) {\n')
    ppt_html_file.write('newLink.href = window.webkitURL.createObjectURL(textToBLOB);\n')
    ppt_html_file.write('}\n')
    ppt_html_file.write('else {\n')
    ppt_html_file.write('newLink.href=window.URL.createObjectURL(textToBLOB);\n')
    ppt_html_file.write('newLink.style.display = \"none\";\n')
    ppt_html_file.write('document.body.appendChild(newLink);\n')
    ppt_html_file.write('}\n')
    ppt_html_file.write('newLink.click();\n')

    # ppt_html_file.write('let fileHandle;\n')
    # ppt_html_file.write('document.querySelector(\".html\").onclick = async () = > {\n')
    # ppt_html_file.write('[fileHandle] = await window.showOpenFilePicker();\n')

    # ppt_html_file.write('const file = await fileHandle.getFile();\n')
    # ppt_html_file.write('const content = await file.text();\n')

    # ppt_html_file.write('return content;\n')
    # ppt_html_file.write('};\n')

    ppt_html_file.write('}\n')

    ppt_html_file.write('</script>\n')

    # ppt_html_file.write('<a id = \"download_button\" download = \"Download.csv\" type = \"text/csv\" > Download CSV </a>\n')

    # ppt_html_file.write('const amino_acids = []\n')

    # ppt_html_file.write('x.addEventListener(\"click\", getCheckboxValue)\n')

    # ppt_html_file.write('function getCheckboxValue() {\n')

    ppt_html_file.write('</html>\n')

    return()