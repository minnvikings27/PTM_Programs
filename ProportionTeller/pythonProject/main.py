# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

DNAstring = ""

DNAsequenceX_file = open("/Users/miltonandrews/Downloads/DNAsequenceX.txt", "r")

line  = DNAsequenceX_file.readline()

while DNAsequenceX_file:
    line  = DNAsequenceX_file.readline().replace('\n', '')
    if line == "":
        break
    DNAstring = DNAstring + line
DNAsequenceX_file.close()

promoter = "TATAA"

index = DNAstring.find(promoter)

print(DNAstring)
print(index)