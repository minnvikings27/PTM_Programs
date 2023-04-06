def build_html_page():

    import os

    from get_modification_types import gather_ptm_reactions

    i = 0
    j = 0

    # ptm_reactions = []

    ptm_modifiers = []

    current_ptm = []

    ptm_modifiers_2 = []

    amino_acids_list = ['Tyrosine', 'Serine', 'Threonine', 'Alanine', 'Arginine', 'Asparagine', 'Aspartatic Acid', \
                        'Cysteine', 'Glutamic Acid', 'Glutamine', 'Glycine', 'Histidine', 'Isoleucine', 'Leucine', \
                        'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Tryptophan', 'Valine']

    ptm_reactions = gather_ptm_reactions()

    input_path = os.path.expanduser('~') + '/Proportion_Teller/Input_Files/User_Input/'

    ptm_modifier_file = input_path + 'PTM_Modifiers.txt'

    with open(ptm_modifier_file) as f:
        ptm_modifiers = f.readlines()

    # print the list
    print(ptm_modifiers)

    # remove new line characters
    ptm_modifiers = [x.strip() for x in ptm_modifiers]

    for i in range (0, len(ptm_modifiers)):
        current_ptm = ptm_modifiers[i]
        if current_ptm[0] != '#':
            ptm_modifiers_2.append(ptm_modifiers[i])
    print(ptm_modifiers_2)

    ppt_html_page = input_path + 'PortionTeller_User_Input.html'
    ppt_html_file = open(ppt_html_page, 'w')

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
    ppt_html_file.write('style = \"position:fixed; left:100px; top:300px; color: yellow\">\n')
    ppt_html_file.write('</div>\n')

    ppt_html_file.write('<label> Modified amino acid(s) </label> <br>\n')
    for i in range(0,len(amino_acids_list)):
        ppt_html_file.write('<input type = \"checkbox\" id = \"' + amino_acids_list[i] + '\" name = \"' +
                            amino_acids_list[i] + '\" value = \"' + amino_acids_list[i] + '\">\n')
        ppt_html_file.write('<label for=\"' + amino_acids_list[i] + '\">' + amino_acids_list[i] + '</label>\n')
        ppt_html_file.write('<br>\n')

    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:100px; top:100px;\">\n')
    ppt_html_file.write('</div>\n')
    ppt_html_file.write('<label for=\"amino_side_location\"> Amino Side Location:</label>\n')
    ppt_html_file.write('<select name = \"amino_side_location\" id=\"amino_side_location\">\n')

    for i in range(1,21):
        j = -1 * i
        ppt_html_file.write('<option value = \"' + str(j) + '\">' + str(j) + '</option>\n')
    ppt_html_file.write('</select>\n')

    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:500px; top:100px;\">\n')
    ppt_html_file.write('</div>\n')
    ppt_html_file.write('<label for=\"carboxyl_side_location\"> Carboxyl Side Location:</label>\n')
    ppt_html_file.write('<select name = \"carboxyl_side_location\" id=\"carboxyl_side_location\">\n')

    for i in range(1,21):
        ppt_html_file.write('<option value = \"' + str(i) + '\">' + str(i) + '</option>\n')
    ppt_html_file.write('</select>\n')

    ppt_html_file.write('<div.fixed {\n')
    ppt_html_file.write('style = \"position:fixed; left:500px; top:300px;\">\n')
    ppt_html_file.write('</div>\n')

    ppt_html_file.write('<label> PTM Reaction(s) </label> <br>\n')

    for i in range(0,len(ptm_reactions)):
        ppt_html_file.write('<input type = \"checkbox\" id = \"' + ptm_reactions[i] + '\" name = \"' +
                            ptm_reactions[i] + '\" value = \"' + ptm_reactions[i] + '\">\n')
        ppt_html_file.write('<label for=\"' + ptm_reactions[i] + '\">' + ptm_reactions[i] + '</label>\n')
        ppt_html_file.write('<br>\n')

    ppt_html_file.write('</body>\n')

    ppt_html_file.write('<script>\n')



    ppt_html_file.write('</script>\n')


    ppt_html_file.write('</html>\n')

    return()

""""

    < ! File
    Name
    Text
    Entry
    Box >
    < div.fixed
    {
        style = "position:fixed; left:100px; top:100px; color: yellow" >
                < / div >

                    PEAKS
    file
    name: < input
    type = text >

           <! PTM
    Reaction
    Name >
    < div.fixed
    {
        style = "position:fixed; left:500px; top:100px;" >
                < / div >

                    < label
    for ="ptm-reaction" > PTM Reaction:< / label >

                                           < select
    name = "ptm-reaction"
    id = "ptm-reaction" >

         < option
    value = "ABL" > ABL < / option >
                            < option
    value = "CDK25" > CDK25 < / option >
                                < option
    value = "MER" > MER < / option >
                            < option
    value = "P25" > P25 < / option >
                            < option
    value = "P35" > P35 < / option >
                            < option
    value = "TYRO3" > TYRO3 < / option >

                                < / select >

                                    <! PTM
    Type >
    < div.fixed
    {
        style = "position:fixed; left:900px; top:100px;" >
                < / div >

                    < label
    for ="modification_type" > Modification type:< / label >

                                                     < select
    name = "modification_type"
    id = "modification_type" >

         < option
    value = "Phosphorylation_(STY)" > Phosphorylation(STY) < / option >
                                                               < option
    value = "Oxidation_(M)" > Oxidation(M) < / option >
                                               < option
    value = "Carbamidomethylation" > Carbamidomethylation < / option >
                                                              < option
    value = "Deamidation_(NQ)" > Deamidation(NQ) < / option >
                                                     < option
    value = "Acetylation_(Protein_N-term)" > Acetylation(Protein
    N - term) < / option >
                  < option
    value = "Pyro-glu_from_Q-Q" > Pyro - glu
    from Q

    -Q < / option >

           < / select >


                                  < div.fixed
    {
        style = "position:fixed; left:800px; top:800px;" >
                < / div >

                    < button
    id = "submit" > Submit < / button >

                               < b
    id = "submit" > < / b >

                        < script >

                        const
    x = document.getElementById("submit")

    const
    amino_acids = [];

    x.addEventListener("click", getCheckboxValue)

    function
    getCheckboxValue()
    {

        var
    amino_acids = " ";

    if (document.getElementById("tyrosine").checked === true)
    {
        amino_acids = amino_acids + "Y";
    }
    if (document.getElementById("serine").checked === true) {
    amino_acids = amino_acids + "S";
    }
    if (document.getElementById("threonine").checked == = true) {
    amino_acids = amino_acids + "T";
    }
    if (document.getElementById("alanine").checked == = true) {
    amino_acids = amino_acids + "A";
    }
    if (document.getElementById("argenine").checked == = true) {
    amino_acids = amino_acids + "R";
    }
    if (document.getElementById("asparagine").checked == = true) {
    amino_acids = amino_acids + "N";
    / * amino_acids.push("Asparagine"); * /
    }
    if (document.getElementById("aspartic_acid").checked == = true) {
    amino_acids = amino_acids + "D";
    }
    if (document.getElementById("cysteine").checked == = true) {
    amino_acids = amino_acids + "C";
    }
    if (document.getElementById("glutamic_acid").checked == = true) {
    amino_acids = amino_acids + "E";
    }
    if (document.getElementById("glutamine").checked == = true) {
    amino_acids = amino_acids + "Q";
    }
    if (document.getElementById("glycine").checked == = true) {
    amino_acids = amino_acids + "G";
    }
    if (document.getElementById("histidine").checked == = true) {
    amino_acids = amino_acids + "H";
    }
    if (document.getElementById("isoleucine").checked == = true) {
    amino_acids = amino_acids + "I";
    }
    if (document.getElementById("leucine").checked == = true) {
    amino_acids = amino_acids + "L";
    }
    if (document.getElementById("lysine").checked == = true) {
    amino_acids = amino_acids + "K";
    }
    if (document.getElementById("methionine").checked == = true) {
    amino_acids = amino_acids + "M";
    }
    if (document.getElementById("phenylalanine").checked == = true) {
    amino_acids = amino_acids + "F";
    }
    if (document.getElementById("proline").checked == = true) {
    amino_acids = amino_acids + "P";
    }
    if (document.getElementById("tryptophan").checked == = true) {
    amino_acids = amino_acids + "W";
    }
    if (document.getElementById("valine").checked == = true) {
    amino_acids = amino_acids + "V";
    }

    var e = document.getElementById("ptm-reaction");
    var value = e.value;
    var ptm_reaction_type = e.options[e.selectedIndex].text;

    var e = document.getElementById("modification_type");
    var value = e.value;
    var modification_type = e.options[e.selectedIndex].text;

    var e = document.getElementById("amino_side_location");
    var value = e.value;
    var amino_side_location = e.options[e.selectedIndex].text;

    var e = document.getElementById("carboxyl_side_location");
    var value = e.value;
    var carboxyl_side_location = e.options[e.selectedIndex].text;

    document.getElementById("submit").innerHTML +=
    amino_acids + "," + ptm_reaction_type + "," + modification_type + "," + amino_side_location + "," + carboxyl_side_location;

    total_csv_data = amino_acids + "," + ptm_reaction_type + "," + modification_type + "," + amino_side_location + "," + carboxyl_side_location;

    var csv = total_csv_data;
    var data = new Blob([csv]);
    var a2 = document.getElementById("download_button");
    a2.href = URL.createObjectURL(data);

    / *
    let f = new File([res], 'myFile.txt', {type: 'text/plain'});
    console.log(f);

    let
    url = (f);
    console.log(url)

    let
    a = document.createElement('a')
    console.log(a)

    a.href = url;
    a.download = f.name;
    a.textContent = `Download ${f.name}
    `;
    document.querySelector('main').append(a);
    * /

    } / *END
    OF
    FUNCTION * /

    < / script >

        < a
    id = "download_button"
    download = "Download.csv"
    type = "text/csv" > Download
    CSV < / a >

            < / body >

                < / html >


"""

