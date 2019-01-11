import sys
try:
    if sys.version[0] == '2':
	    reload(sys)
	    sys.setdefaultencoding("utf-8")
	
except NameError:
    try:
        from importlib import reload  # Python 3.4+

    except ImportError:
        from imp import reload  # Python 3.0 - 3.3
    reload(sys)
import xml.etree.cElementTree as ET

class Xml_Layout:


	def __init__(self,name):

		self.name = ET.Element(name)

	def insert(self,content,contentName):

		ET.SubElement( self.name, contentName).text = content

	def close(self):

		self.content = ET.ElementTree(self.name)

	def write(self,path):

		self.content.write(path)
