
"""6. Develop a program to sort the contents of a text file and write the sorted contents into a separate text file. 
[Hint: Use string methods strip(), len(), list methods sort(), append(), and file methods open(),readlines(),and write()]."""

list_text=[]
file_name=input("Enter input file(input.txt):")

def input_file():
    with open (file_name,"r") as file:
        line=file.readlines()
        if len(line) > 0:
            for words in line:
                words= words.strip()
                if words != "":
                    list_text.append(words)       

def sort():
    input_file()
    output_file=input("Enter output file(output.txt):")
    file=open(output_file,'w+')
    list_text.sort()
    print("-" * 26)
    for out in list_text:
        file.write(out + "\n")
        print(out)
        
    file.close()
        
    print("This are saved in order")
    print("-"*26)
sort()
