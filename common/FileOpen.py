
from datetime import datetime

class FileOpen():
	def __init__(self, filename):
		self.fileName = filename
		self.dataToInsert=""
		
		# self.contRow=0
		self.gc=0
  
	def insertFile(self,str):
		# print (self.config)
		self.file = open(self.fileName, 'a+')
		self.file.write(str)
		self.file.close()
  
	def insertHead(self,gc):
		self.gc=gc
		self.dataInsert=""
		fecha_hora_actual = datetime.now()    	
		fecha_hora_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
		self.dataInsert+="<style>\n"
		self.dataInsert+="tr:nth-child(even) {background-color: #E0E0E0;\n"
		self.dataInsert+="td{text-align:left;vertical-align:top}\n"
		self.dataInsert+="th{text-align:center;}\n"
		self.dataInsert+="</style>\n\n"
		self.dataInsert+="<table  class=\"allQuery\" border=1 width=80% >\n"
		self.dataInsert+="<tr>"
		self.dataInsert+="<th>Date/Time</th>"
		self.dataInsert+="<th>Is First id</th>"
		self.dataInsert+="<th>id</th>"
		self.dataInsert+="<th>Var Id</th>"
		self.dataInsert+="<th>TableName</th>"
		self.dataInsert+="<th>Short Table Name</th>"		
		self.dataInsert+="</tr>\n"
  
		self.dataInsert+="<tr>"
		self.dataInsert+="<td>"+fecha_hora_formateada+"</td>"
		self.dataInsert+="<td>"+self.gc.dictTp["global"]["sets"]["smaTableName"]+"</td>"
		self.dataInsert+="<td>"+self.gc.dictTp["global"]["ifNoDefinedId"]["id"]+"</td>"
		self.dataInsert+="<td>"+self.gc.dictTp["global"]["ifNoDefinedId"]["vId"]+"</td>"
		self.dataInsert+="<td>"+self.gc.dictTp["global"]["sets"]["bigTableName"]+"</td>"
		self.dataInsert+="<td>"+self.gc.dictTp["global"]["sets"]["smaTableName"]+"</td>"		
		self.dataInsert+="</tr>\n"
  
  
	def insertRow(self,col1,col2):
		self.dataInsert+="<tr>"
		self.dataInsert+="<td colspan=2>"+col1+"</td>"
		self.dataInsert+="<td colspan=4><table class=\"oneQuery\" border=1 width=100% ><tr><td>\n"+col2+"</td><tr></table></td>"  
		self.dataInsert+="</tr>"
		# self.contRow+=1
    
	# def insertRow(self,col1):
	# 	self.dataInsert+="<tr>"
	# 	self.dataInsert+="<td>"+col1+"/td>"		
	# 	self.dataInsert+="</tr>"
	# 	self.contRow+=1

	def insertFoot(self):	
		self.dataInsert+="</table>\n<br/><br/>\n"
  		
		
	def printTable(self):
		# self.dataInsert = self.dataInsert.replace("((controw))", str(self.contRow))
		self.insertFile(self.dataInsert)
  