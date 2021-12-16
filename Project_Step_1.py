import os
import urllib.request

#1 Create a new project folder and .txt file.

os.chdir(r'C:\Users\phili\OneDrive\Desktop')

os.makedirs(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_2')

os.chdir(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_2')

new_text_file = open('full_text_file.txt', 'w')

new_text_file.write('TESTING')

new_text_file.close()

read_full_text = open('full_text_file.txt', 'r')

print(read_full_text.read())

read_full_text.close()

#2 Open file from Project Gutenberg and save to .txt file.

response = urllib.request.urlopen('https://www.gutenberg.org/files/20158/20158-0.txt')
data = response.readlines()

with open(r'C:\Users\phili\OneDrive\Desktop\Doc_Eng_Project\Step_2\full_text_file.txt', 'w', encoding = 'utf-8-sig') as file:
    for line in data:
        lines = line.decode('utf-8-sig')
        print(lines)
        file.write(lines)
        
read_new_file = open('full_text_file.txt', 'r', encoding = 'utf-8-sig')

print(read_new_file.read())