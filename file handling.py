"""f = open("text.txt","r")
print(f.read())

"""
"""f = open("naman.txt","a")
f.write("Naman sharma hello ")
f.close 

f = open("naman.txt","r")
print(f.read())"""


"""f = open("mytext.txt","x")
f.write("hey!!")"""


"""f = open("mytext.txt","w")
f.write("hey!!")
f.close()"""

"""import os
os.remove("naman.txt")"""


"""import os 
if os.path.exists("naman.txt"):
    os.remove("naman.txt")
else:
    print("File does not exist ")"""
"""
#Reading a csv file
import csv"""
"""
with open('Transaction ID User Product.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  """


"""data = [["Name","Age"],["naman",22],["cheryl",23]]
with open ("Transaction ID User Product.csv","w",newline="" ) as file:
  writer = csv.writer(file)
  writer.writerrows(data)   
"""





# Write a program to copy the contents of one file to another.

"""with open('mytext.txt', 'r') as source_file, open('text.txt', 'w') as destination_file:
    
    for line in source_file:
        destination_file.write(line)

print("File copied successfully!")"""

#
def count_file_content(mytext.txt):
    
        with open(mytext.txt, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
        
        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")
   


count_file_content( mytext.txt )





















































