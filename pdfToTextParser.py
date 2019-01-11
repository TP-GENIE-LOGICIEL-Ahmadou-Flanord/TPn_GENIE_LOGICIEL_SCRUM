
#!/usr/bin/python2.7
# coding=utf-8



import subprocess
import os
import sys
from txt_layout import *
from xml_layout import *

# path = 'Papers'
# script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
# script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
# abs_file_path = os.path.join(script_dir, path)



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


# extraction de la bibliographie 
def getBiblio(path):
	parse = ""
	fich = open(path,'r')
	cond = False
	for ligne in fich.readlines():
		if("\x0c408" in ligne):
			break
		if(cond):
			parse += ligne
		if(ligne[0]=="R" and ligne[1]=="e" and ligne[2]=="f" and ligne[3]=="e" and ligne[4]=="r" and ligne[5]=="e" and ligne[6]=="n" and ligne[7]=="c" and ligne[8]=="e" and ligne[9]=="s"):
			cond = True
		elif(ligne[0]=="R" and ligne[1]=="E" and ligne[2]=="F" and ligne[3]=="E" and ligne[4]=="R" and ligne[5]=="E" and ligne[6]=="N" and ligne[7]=="C" and ligne[8]=="E" and ligne[9]=="S"):
			cond = True
		elif("References" in ligne):
			cond = True	
	fich.close()
	return Parser(parse);

# extraction des autheurs et de leurs adresses 
def getAut(path):
	parse = ""
	fich = open(path,'r')
	cond = False
	nb = 0;
	for ligne in fich.readlines():
		nb += 1
		if(len(ligne.split()) == 2):
			nb += 1
		if ("Abstract" in ligne or "ABSTRACT" in ligne):
			break;
		if(ligne == "\n" or nb > 2 ):
			cond = True
		if(cond and ligne != " \n"):
			parse += ligne
	fich.close()
	return Parser(parse);

# extraction de l'introduction 
def getIntro(path):
	parse = ""
	fich = open(path,'r')
	cond = False
	cond2 = False
	cond3 = False
	prequel = False
	for ligne in fich.readlines():
		if ("Abstract" in ligne or "ABSTRACT" in ligne):
			prequel = True
		if (prequel):
			if (cond==False and (cond2==False and (cond3==False))):
				if (ligne=="1\n" or ligne=="1 Introduction\n"):
					 cond = True
				elif (ligne[0]=="1" and ligne[1]=="."):
					cond2 = True
				elif (ligne[0]=="I" and ligne[1]=="."):
					cond3 = True
			if (cond and (ligne=="2\n" or (ligne=="2\n" or (ligne[0]=="2" and (ligne[1]==" "))))):
				break
			if (cond2 and (ligne[0]=="2" and ligne[1]==".")):
				break
			if (cond3 and (ligne[0]=="I" and ligne[1]=="I")):
				break
			if (cond==True or cond2==True or cond3==True):
				parse += ligne
	fich.close()
	return Parser(parse)

# extraction de la conclusion 
def getConclu(path):
	parse = ""
	fich = open(path,'r')
	cond = False
	for ligne in fich.readlines():
		if ("Conclusion" in ligne or "CONCLUSION" in ligne or "Conclusions" in ligne or "CONCLUSIONS" in ligne):
			for i in range(0,6):
				if (ligne[i]=="C"):
					cond = True
		if (ligne[0]=="A" and ligne[1]=="c" and ligne[2]=="k" and ligne[3]=="n"):
			break
		if (ligne[0]=="A" and ligne[1]=="C" and ligne[2]=="K" and ligne[3]=="N"):
			break
		if (cond and ("REFERENCES" in ligne or "References" in ligne)):
			break
		if (cond and ligne!="\n"):
			parse += ligne
	fich.close()
	return Parser(parse)

# extraction du corps 
def getCorps(path):	 								# cette fonction est composee de la condition
	parse = ""									# d'arret de getIntro et de la condition de
	fich = open(path,'r')								# de depart modifiee de getConclu et de la 
	cond = False									# condition de depart de getDiscu
	cond2 = False
	cond3 = False
	prequel = False
	cond4 = False
	arret = False
	for ligne in fich.readlines():
		if ("Abstract" in ligne or "ABSTRACT" in ligne):
			prequel = True
		if (prequel):
			if (cond==False and (cond2==False and (cond3==False))):
				if (ligne=="1\n" or ligne=="1 Introduction\n"):
					 cond = True
				elif (ligne[0]=="1" and ligne[1]=="."):
					cond2 = True
				elif (ligne[0]=="I" and ligne[1]=="."):
					cond3 = True
			if (cond and (ligne=="2\n" or (ligne=="2\n" or (ligne[0]=="2" and (ligne[1]==" "))))):
				cond4 = True
			if (cond2 and (ligne[0]=="2" and ligne[1]==".")):
				cond4 = True
			if (cond3 and (ligne[0]=="I" and ligne[1]=="I")):
				cond4 = True
		if ("Conclusion" in ligne or "CONCLUSION" in ligne or "Conclusions" in ligne or "CONCLUSIONS" in ligne):
			for i in range(0,6):
				if (ligne[i]=="C"):
					arret = True
		if (arret):
			break
		if (". Discussion" in ligne):
			break
		if (cond4 and ligne!="\n"):
			parse += ligne
	fich.close()
	return Parser(parse)

# extraction de la discussion 
def getDiscu(path):
	parse = ""
	fich = open(path,'r')
	cond = False
	arret = False
	for ligne in fich.readlines():
		if (". Discussion" in ligne):
			cond = True
		if ("Conclusion" in ligne or "CONCLUSION" in ligne or "Conclusions" in ligne or "CONCLUSIONS" in ligne):
			for i in range(0,6):
				if (ligne[i]=="C"):
					arret = True
		if (arret):
			break
		if (cond and ligne!="\n"):
			parse += ligne
	fich.close()
	return Parser(parse)

# Conversion du fichier pdf d'origine entier en texte
def CONVERT(file_path,filename):
	#file_path = os.path.abspath(filename)
	os.chdir(file_path+"/CONVERT")
	outputName = filename.split(".")[0];
	print (" **** CONVERT ****  : " + outputName )
	subprocess.call(["pdftotext", file_path,str(os.getcwd()+"/"+outputName+".txt"),"-layout"])


#Creer un dossier ( s'il n'existe pas encore)
def makeDir(dirname):
	try:
		os.stat(dirname)
	except:
		os.mkdir(dirname)  


# transformation du pdf selectionne
def splitText(abs_file_path,layout,filename,parsePath,mode):
	nom=filename.split('.')[0]
	#file_path = os.path.abspath(filename)
	path = abs_file_path + parsePath
	
	ficPath = abs_file_path+"/CONVERT/"+nom+".txt"
	
	writeToFile(abs_file_path,layout,ficPath,filename,mode) 
	if mode == "-x":
		xmlpath = path+"/"+nom+".xml"
		layout.write(xmlpath) # on cree le fichier .xml avec le layout
	else:
		writeText(path, nom+".txt", layout.content) 


# remplissage du layout choisi avec les donnees
def writeToFile(layout,file,filename,mode):

	if ( mode == "-x"):
		layout.insert(filename,"preamble")
		layout.insert(getTitle(file),"titre")
		layout.insert(getAut(file),"auteur")
		layout.insert(getAbstract(file),"abstract")
		layout.insert(getIntro(file),"introduction")
		layout.insert(getCorps(file),"corps")
		layout.insert(getConclu(file),"conclusion")
		layout.insert(getBiblio(file),"biblio")
		layout.close()

	elif ( mode == "-t"):
		layout.insert(filename)
		layout.insert(" **************** -TITRE- **************** ")
		layout.insert(getTitle(file))
		layout.insert(" **************** -AUTEURS/ADRESSES- **************** ")
		layout.insert(getAut(file))
		layout.insert(" **************** -ABSTRACT- **************** ")
		layout.insert(getAbstract(file))
		layout.insert(" **************** -INTRODUCTION- **************** ")
		layout.insert(getIntro(file))
		layout.insert(" **************** -CORPS- **************** ")
		layout.insert(getCorps(file))
		layout.insert(" **************** -CONCLUSION- **************** ")
		layout.insert(getConclu(file))
		layout.insert(" **************** -DISCUSSION- **************** ")
		layout.insert(getDiscu(file))
		layout.insert(" **************** -BIBLIOGRAPHIE- **************** ")
		layout.insert(getBiblio(file))


 # ecriture du nouveau parse texte
def writeText(path,fichier,content):

	fic = open(path+"/"+fichier,"w+")
	fic.write(content);
	fic.close()


def select(pdf_path):
    selec = []
    print "###  Veuillez choisir les fichiers pdf a transformer ###"
    print "###                oui/o/y/yes - non/n/no            ###"
    for pdf in os.listdir(pdf_path):
        ext = pdf.split('.')[-1]
        if(ext == "pdf"): # verification si c'est bien un fichier pdf
            print "\n=> "+pdf
            valid=raw_input("")
            if("oui" in valid or "o" in valid or "y" in valid or "yes" in valid):
                selec.append(pdf)
    return selec

# Notre PdftoText
def pdfToTextParser(mode):
	parsePath = "/PARSE"

	if(mode == "-t"):
		print (" layout 2")
		layout = Txt_Layout()
		parsePath+="_txt"
	elif mode == "-x":
		print (" layout 1")
		layout = Xml_Layout("article")
		parsePath+="_xml"
	else:
		print ("Erreur cette option n'existe pas")
		return
	pdf_path=raw_input("Veuillez entrer le chemin du dossier contenant les pdfs : ")
	if os.path.exists(pdf_path):
		abs_file_path=pdf_path
		os.chdir(abs_file_path)
		# Creer le dossier CONVERT
		makeDir(pdf_path+"/CONVERT")
		
		listPdf=select(pdf_path)
		makeDir(pdf_path+parsePath)

		# execution du Parsing
		for filename in os.listdir(abs_file_path):
			if filename not in listPdf:
				continue

			if os.path.isdir(filename)== False :
				CONVERT(pdf_path,filename)
				splitText(pdf_path,layout,filename,parsePath,mode)
				os.chdir(abs_file_path)
	else:
		print "Le repertoire "+pdf_path+" n'existe pas !"
		return
    
	

   


################################# MAIN #################################
if __name__ == '__main__':
	if (len(sys.argv)<=1):
	    pdfToTextParser("-x")
	else:
		pdfToTextParser(sys.argv[1])
   

