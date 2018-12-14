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
    #ExtractTExt(str(os.getcwd()+"/"+outputName+".txt"))
    fic =str(os.getcwd()+"/"+outputName+".txt")
    f = open(fic, 'r')
    data = f.read()
    splat = data.split("\n\n")
    text = ""
    for number, paragraph in enumerate(splat, 1):
    	print "number " ,number
    	if "Abstract" not in paragraph :
    		text +=paragraph
    	else :
			print ("on the Abstract")
			#print paragraph 
			text  +=paragraph
			break
	f.close()
	with open(fic, 'w+') as f:
		f.write(text)
	f.close()

	os.chdir(abs_file_path)
	print os.getcwd() + " 3"

#for filename in os.listdir(abs_file_path+"/Output"):


    # do your stuff
    
#os.chdir(abs_file_path+"/Output")

def ExtractTExt(filename):
	
	f = open(filename, 'r')

	data = f.read()
	array1 = []
	array2 = []
	array3 = []
	splat = data.split("\n\n")
	text = ""
	for number, paragraph in enumerate(splat, 1):
		print "number " ,number
		if "Abstract" not in paragraph :
			#print paragraph
			text +=paragraph
		else:
			print ("on the Abstract")
			#print paragraph 
			text  +=paragraph
			break
	f.close()
	with open(filename, 'w+') as f:
	    f.write(text)
	f.close()


# 	if number % 3 == 1:
# 		array1 += [paragraph]
# 	elif number % 3 == 2:
# 		array2 += [paragraph]
# 	elif number % 3 == 0:
# 		array3 += [paragraph]
# #print filename
# x=0
# with open(filename) as f:
# 	for line in f:
# 		if x==1:
# 			print ("terminus")
# 			print line 
# 			break 
# 		if "Abstract" not in line :
			
# 			print line
# 		else:
# 			print ("on the Abstract")
# 			print line 
# 			x=1
			

   
    # file_path = os.path.abspath(filename)
    # print(file_path )
    # os.chdir(abs_file_path+"/Output")
    # outputName = filename.split(",")[0];
    # print outputName + "txt"
    # print os.getcwd() + " 2"
    # subprocess.call(["pdftotext", file_path,str(os.getcwd()+"/"+outputName+".txt"),"-layout"])
    # os.chdir(abs_file_path)
    # print os.getcwd() + " 3"



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