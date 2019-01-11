
#!/usr/bin/python2.7
# coding=utf-8


import subprocess
import os
from txt_layout import *
path = 'Papers'
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
abs_file_path = os.path.join(script_dir, path)


# transforme le texte parse
def Parser(texte):
	texte.replace("\n"," ")
	texte.replace("\f"," ")
	split_chars = ["\x0c","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
	texte = texte.encode('string_escape')
	for c in split_chars:
		texte = texte.replace( c.encode('string_escape') , "" )
	texte = texte.decode('string_escape')
	return texte


# Title extract
def getTitle(file):
    parse = ""
    fich = open(file,'r')
    nb = 1
    cond = False
    for ligne in fich.readlines():
        if(len(ligne.split()) == 2):
            nb += 1
        if((ligne != "\n" or cond) and nb < 3):
            if(not "VOL." in ligne and not "401" in ligne and not "(2007)" in ligne and not "www." in ligne and ligne != "\n"):
                parse += ligne
                nb += 1
            else:
                cond = True
        else:
            break

    fich.close()
    return Parser(parse);

# extraction de l'abstract du pdf
def getAbstract(path):
	cond = False
	parse = ""
	fich = open(path,'r')
	for ligne in fich.readlines():
		if ("Introduction" in ligne or "INTRODUCTION" in ligne):
			break;
		if (cond):
			parse+=ligne
		if ("Abstract" in ligne or "ABSTRACT" in ligne):
			parse  += ligne
			cond = True;

	fich.close()
	return Parser(parse);



# Conversion du fichier pdf d'origine entier en texte
def CONVERT(filename):
	file_path = os.path.abspath(filename)
	os.chdir(abs_file_path+"/CONVERT")
	outputName = filename.split(".")[0];
	print "outputName :" + outputName
	subprocess.call(["pdftotext", file_path,str(os.getcwd()+"/"+outputName+".txt"),"-layout"])


#Creer un dossier ( s'il n'existe pas encore)
def makeDir(dirname):
	try:
		os.stat(abs_file_path+dirname)
	except:
		os.mkdir(abs_file_path+dirname)  


# transformation du pdf selectionne
def splitText(filename):
	nom=filename.split('.')[0]
	file_path = os.path.abspath(filename)
	path = abs_file_path + "/PARSE"
	layout = Txt_Layout()
	ficPath = abs_file_path+"/CONVERT/"+nom+".txt"
	
	print os.getcwd() + " 2"
	fic =str(os.getcwd()+"/"+nom+".txt")
	writeToFile(layout,ficPath,filename) 

	writeText(path, nom+".txt", layout.content) 


# remplissage du layout choisi avec les donnees
def writeToFile(layout,file,filename):

	layout.insert(filename)
	layout.insert(" **************** -TITRE- **************** ")
	layout.insert(getTitle(file))
	layout.insert(" **************** -ABSTRACT- **************** ")
	layout.insert(getAbstract(file))


 # ecriture du nouveau parse texte
def writeText(path,fichier,content):

	fic = open(path+"/"+fichier,"w+")
	fic.write(content);
	fic.close()


# Notre PdftoText
def pdfToTextParser():

	
	
	os.chdir(abs_file_path)
	
	# Creer le dossier CONVERT
	makeDir("/CONVERT")

	# Creer le dossier PARSE
	makeDir("/PARSE")

	parsePath = "/PARSE"

	# execution du Parsing
	for filename in os.listdir(abs_file_path):

		if os.path.isdir(filename):
			continue

		CONVERT(filename)
		splitText(filename)
		os.chdir(abs_file_path)

   


################################# MAIN #################################
if __name__ == '__main__':
	pdfToTextParser()
   

