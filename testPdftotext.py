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
#print os.listdir(abs_file_path)
os.chdir(abs_file_path)
print os.getcwd() + " 1"
try:
    os.stat(abs_file_path+"/Output")
except:
    os.mkdir(abs_file_path+"/Output")  
for filename in os.listdir(abs_file_path):


    # do your stuff
    print filename
   
    file_path = os.path.abspath(filename)
    print(file_path )
    os.chdir(abs_file_path+"/Output")
    outputName = filename.split(",")[0];
    print outputName + "txt"
    print os.getcwd() + " 2"
    subprocess.call(["pdftotext", file_path,str(os.getcwd()+"/"+outputName+".txt"),"-layout"])
    os.chdir(abs_file_path)
    print os.getcwd() + " 3"




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