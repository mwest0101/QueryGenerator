import re
import tkinter as tk
from common.SnakeToCamel import SnakeToCamel


class EventManager:
	def __init__(self, gui,gc,fh):
		self.gui = gui
		# self.text_box2 = text_box2
		self.inText=""
		self.outText=""
		self.gc=gc
		self.fh=fh
		self.repAll=False
		self.contKey=0
		self.contVal=0
		self.inArray=[]
		self.outArray=[]
		self.currentKey=""
  
	def resetCounters(self):
		self.contKey=0
		self.contVal=0
        
	def getOneKey(self,inc=0):
		self.contKey+=1
		valReturn=self.inArray[self.contKey-1+inc]
		
		# print ("---->contador:",self.contKey," ",len(self.inArray)-1)
		if self.contKey==(len(self.inArray)-1):
			self.contKey=0
		return valReturn

	def getContKey(self):
		return self.contKey

	def getOneVal(self,inc=0):
		self.contVal+=1
		valReturn=self.outArray[self.contVal-1+inc]
		
		if self.contVal==(len(self.inArray)-1):
			self.contVal=0
		return valReturn

	def getContVal(self):
		return self.contVal

	def strReplaces(self,key="",value=""):
		strResult=""		
		# print(key," - ",value)
		
		tempStr = ""
		if(self.currentKey!=key):
			self.resetCounters()
   
			
		if key=="fn": 
			strResult = strResult +"\n_______________________"+"\n"	
			strResult = strResult +"[[[ "+value.upper()+" ]]]\n"
			# strResult = strResult +"-----------------------------------"
			# strResult += value
		else:
			strResult = value
		# if "HEAD" in key: 
		# 	strResult = strResult +value+"\n"

		# if "BODY" in key: 
		# 	strResult = strResult +value+"\n"
   
		# if "FOOT" in key: 
		# 	strResult = strResult +value+"\n"	
		
		if "|smaTableName|" in strResult:			
			strResult = strResult.replace("|smaTableName|", self.gc.dictTp["global"]["sets"]["smaTableName"])		
			# print("Entre")


		if "|bigTableName|" in strResult:			
			strResult = strResult.replace("|bigTableName|", self.gc.dictTp["global"]["sets"]["bigTableName"])	

		if "|id|" in strResult:			
			strResult = strResult.replace("|id|", self.gc.dictTp["global"]["ifNoDefinedId"]["id"])		


		if "|vId|" in strResult:			
			strResult = strResult.replace("|vId|", self.gc.dictTp["global"]["ifNoDefinedId"]["vId"])	

		if "(--all:" in strResult:	
			strResult = strResult.replace("(--all:", "")	
			if "|key|" in strResult:			
				strResult = strResult.replace("|key|", self.getOneKey())	
			
			if "|val|" in strResult:			
				strResult = strResult.replace("|val|", self.getOneVal())	
    
		if "(--all_wid:" in strResult:
			strResult = strResult.replace("(--all_wid:", "")				
			if "|key|" in strResult:			
				strResult = strResult.replace("|key|", self.getOneKey(1))	
			
			if "|val|" in strResult:			
				strResult = strResult.replace("|val|", self.getOneVal(1))	
    
		if "|sep_in:" in strResult:			        
			match = re.search(r'\|sep_in:([^|]+)\|', strResult)
			charSep = match.group(1) if match else None			
			strResult = re.sub(r'\|sep_in:[^|]+\|', charSep, strResult)
				

		# Imprimir los resultados

		
		# if "(--rep_all:" in strResult:		
		# 	self.repAll=True
		# 	strResult = strResult.replace("(--rep_all:", "")	
		# 	strResult = strResult.replace("))", "")	
		# 	print(self.inArray)
		# 	self.outArray
		# 	if("|key|" in strResult):
		# 		for data in self.inArray:
		# 			strResult+=strResult.replace("|key|",data)+"\n"
		# 			if()
  
   
		
		print(key," - ",strResult)


		strResult=strResult+"\n"
		# self.gui.text_box2.insert('end',strResult)
		
		self.currentKey=key
		return strResult

	def replaceText(self,dataArray):
		strResult=""
		key=""
		value=""
		for key,value in dataArray:				
			lineResult=self.strReplaces(key,value)
			
			self.gui.text_box2.insert('end',lineResult)
			strResult=strResult+lineResult
   
		return strResult	
	def clearStr(self,strIn):
		if "\n\n" in strIn:
      
			strIn=strIn.replace("\n\n","\n")
			strIn=strIn.replace("\n\0","")
			strIn=strIn.strip()
			self.clearStr(strIn)
		
		return strIn
	def splitTextArea(self,strIn):
		arrayClean=[]
		if "," in strIn:
			inArray = strIn.split(',')
		else:
			inArray = strIn.split('\n')
		for data in inArray:
			arrayClean.append(data.strip())

		return arrayClean

	def splitAndConvert(self):
		stc = SnakeToCamel()
		self.inText = self.gui.text_box1.get("1.0", tk.END)	
		
		self.inText=self.clearStr(self.inText)
		self.inArray = self.splitTextArea(self.inText)
		# print("========================================") 	  
		# print(self.inArray) 	  
		# print("========================================") 	  
		self.outText=""		  
		self.gui.text_box2.delete("1.0", tk.END)	

		self.outArray=stc.convert(self.inArray)
		print("========================================")
		print (self.inArray)
		print("========================================")
		print (self.outArray)

	def convertText(self):
		
		self.splitAndConvert()	
		self.gc.getConfAndParams(self.inArray,self.outArray)
		partialDict=self.gc.loadPartialDict()
		inArrayStr = self.gc.loadStringSelected(partialDict)
		inArrayStr = self.gc.repeatStrs(inArrayStr)
		self.fh.insertHead(self.gc)
  
		strArrayConc=""
		for i  in range(len(self.inArray)):
			strArrayConc+="<b>"+self.inArray[i]+ "</b> = " +self.outArray[i]+"\n"
   
		strResult=self.replaceText(inArrayStr)
  		
		strResultHtml = strResult.replace("\n","</br>\n")				
		strResultHtml = strResultHtml.replace("_______________________</br>","</td></tr><tr><td>\n")				
		strResultHtml =	strResultHtml .replace("[[[","<h2>")
		strResultHtml =	strResultHtml .replace("]]]","</h2>")
		strResultHtml = strResultHtml.replace("</br></br>","</br>\n")	
		strResultHtml = strResultHtml.replace("</br>\n</br>","</br>\n")	
     
		self.fh.insertRow(strArrayConc.replace("\n","</br>\n"),strResultHtml)
		self.fh.insertFoot()
	    
		self.fh.printTable()
		# self.gc.showConfiguration()
		

	def copiar_texto(self):
		inText = self.text_box1.get("1.0", tk.END)	   # Obtener todo el texto del primer Text box
		self.text_box2.delete("1.0", tk.END)			# Limpiar el segundo Text box
		self.text_box2.insert(tk.END, inText) 
	