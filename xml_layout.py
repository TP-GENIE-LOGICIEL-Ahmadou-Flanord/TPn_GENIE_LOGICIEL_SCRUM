import sys
reload(sys)
sys.setdefaultencoding("utf-8")
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
