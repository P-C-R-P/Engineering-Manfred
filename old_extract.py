import re, os

#1 Create a new project directory.

os.chdir(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project')

os.makedirs(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_4')

os.chdir(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_4')

#2 Find index positions of start/end and copy extracts to new files.

with open(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_2\full_text_file.txt', 'r', encoding = 'utf-8') as extract:
    text = extract.read()
    chillon_start = re.findall(r'THE PRISONER OF CHILLON\n', text)
    print('This is the start of The Prisoner of Chillon:', chillon_start)
    chillon_end = re.findall(r'.*sigh\.', text)
    print('This is the end of The Prisoner of Chillon:', chillon_end)
    manfred_start = re.findall('Manfred:\n', text, re.IGNORECASE)
    print('This is the start of Manfred:', manfred_start)
    manfred_end = re.findall(r'.*poem."\]', text)
    print('This is the end of Manfred:', manfred_end)
    
    in_text_1 = text.index(chillon_start[0])
    print(in_text_1)
    in_text_2 = text.index(chillon_end[0])
    print(in_text_2)
    in_text_3 = text.index(manfred_start[0])
    print(in_text_3)
    in_text_4 = text.index(manfred_end[0])
    print(in_text_4)
    
    with open(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_4\chillon_text.txt', 'w') as chillon_extract:
        chillon_final = chillon_extract.write(text[in_text_1 : in_text_2 + len(chillon_end[0])])
        print(chillon_final)
        chillon_extract.close()
        
        with open(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_4\chillon_text.txt', 'r') as read_chillon:
            chillon_test = read_chillon.read()
            print(chillon_test)
            read_chillon.close()

    with open(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_4\manfred_text.txt', 'w', encoding = 'utf-8') as manfred_extract:
        manfred_final = manfred_extract.write(text[in_text_3 : in_text_4 + len(manfred_end[0])])
        print(manfred_final)
        manfred_extract.close()
        
        with open(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_4\manfred_text.txt', 'r', encoding = 'utf-8') as read_manfred:
            manfred_test = read_manfred.read()
            print(manfred_test)
            read_manfred.close()