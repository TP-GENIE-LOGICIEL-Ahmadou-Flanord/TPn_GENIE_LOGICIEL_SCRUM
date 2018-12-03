import subprocess
import os
#script_dir = os.path.dirname(__file__)
#print script_dir + " dfsdf"	
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
print script_path
print script_dir
#subprocess.call(["pdftotext", "-l", "/etc/resolv.conf"])
#pdftotext fichier.pdf fichier.txt -layout
path = 'Papers'
output = '../papers/output/'
abs_file_path = os.path.join(script_dir, path)
print abs_file_path	
for filename in os.listdir(abs_file_path):
    # do your stuff
    print(filename + " erttr")
    #subprocess.call(["pdftotext", str(filename), str(path),"-layout"])




#with open(os.path.expanduser("lorem_ipsum.pdf"), "r") as f:
#subprocess.call(["pdftotext", "./lorem_ipsum.pdf", "./lorem_ipsum.txt","-layout"])
#fichier = open("./lorem_ipsum.txt" , "r")
#for line in fichier:
#	print line;
#print(fichier.read())

# Iterate over all the pages
#for page in pdf:
    #print(page)

# Just read the second page
#print(pdf)

# Or read all the text at once
#print(pdf.read_all())