
import tkinter as tk
import json


class GetConfiguration():
	def __init__(self,tp):
		self.arrayValues=""
		self.tp=tp
		self.gui=""
		# self.arrayLanguajes=[]
		# self.arrayDatabases=[]
		# self.arrayFunctions=[]
		self.selected_templates_value=""
		self.selected_databases_value=""
		self.selected_functions_value=""
		self.dictTp=tp.getStr()
		self.inArray=[]
		self.outArray=[]
		
	
	def getStr(self):
		# print (self.config)
		return self.config

	def setGui(self,gui):
		self.gui=gui
  
	def recorrer_json(self,data, path=""):
		if isinstance(data, dict):
			for key, value in data.items():
				new_path = f"{path}.{key}" if path else key
				self.recorrer_json(value, new_path)
		elif isinstance(data, list):
			for index, item in enumerate(data):
				new_path = f"{path}[{index}]"
				self.recorrer_json(item, new_path)
		else:
			pass
			# print(f"Ruta: {path}, Valor: {data}")
   

  
	def loadLangaujes(self):
		arrayLanguajes=[]
		for keyLanguaje in self.dictTp["templates"]:	
			arrayLanguajes.append(keyLanguaje)		
		return arrayLanguajes
	
	def loadDatabases(self,keyTemplate):
		arrayDatabases=[]
		for key in self.dictTp["templates"][keyTemplate] :	
			arrayDatabases.append(key)		
		return arrayDatabases

	def loadFunctions(self,keyTemplate,keyDatabases):
		arrayFunctions=[]
		arrayFunctions.append("All")
		for key in self.dictTp["templates"][keyTemplate][keyDatabases] :	
			arrayFunctions.append(key)		
		return arrayFunctions

	def loadSelectedGui(self):
		self.selected_templates_value = self.gui.selected_templates_value
		self.selected_databases_value = self.gui.selected_databases_value
		self.selected_functions_value = self.gui.selected_functions_value
		# print(self.selected_templates_value)
		# print(self.selected_databases_value)
		# print(self.selected_functions_value)
  
	def loadPartialDict(self):		
		self.loadSelectedGui()				
		# print("self.selected_functions_value=",self.selected_functions_value)
		if(self.selected_functions_value=="All"):
			partialDict=self.dictTp["templates"][self.selected_templates_value][self.selected_databases_value]
		else:
			partialDict=self.dictTp["templates"][self.selected_templates_value][self.selected_databases_value][self.selected_functions_value]
   
		return partialDict

	def loadStringSelected(self,partialDict):
		arrayKeyAndValue=[]
		if (self.selected_functions_value=="All"):
			arrayKeyAndValue.append(["fn",self.selected_functions_value])
			for key1 in partialDict:	
				arrayKeyAndValue.append(["fn",key1])
				multiPart=partialDict[key1]
				for key2 in multiPart:	
					arrayKeyAndValue.append([key2,multiPart[key2]])
		else:
			# print("fn"," ",self.selected_functions_value)
			for key1 in partialDict:		
				arrayKeyAndValue.append([key1,partialDict[key1]])
		
		return arrayKeyAndValue

	def repeatStrs(self,inArrayStr):
		newArray=[]
		
		# self.inArray
		# self.outArray
		print("___________________________________")
		print("---checkRepat----------------------")
		for key,value in inArrayStr:
			
			print (".",key," - ",value)
			strResult=value	
   
			if "(--all:" in value:						
				# strResult = strResult.replace("(--all:", "")	
				strResult = strResult.replace("--)", "")	
				for element in self.inArray:
					if element!="":
						# print (".",key," - ",value," - ",element)
						newArray.append([key,strResult])
			elif "(--all_wid:" in value:						
				# strResult = strResult.replace("(--all_wid:", "")	
				strResult = strResult.replace("--)", "")	
				cont=0
				for element in self.inArray:					
					if element!="":
						# print (".",key," - ",value," - ",element)
						if(cont==0):
							cont+=1
						else:
							newArray.append([key,strResult])
			else:
				newArray.append([key,strResult])
		print("----------------------------------")
		return newArray
  
	def rsc(self,strResult): 
		return strResult.replace("\n","")

	def getConfAndParams(self,inArray,outArray):
		self.inArray=inArray
		self.outArray=outArray
		
		if(self.dictTp["global"]["sets"]["bigTableName"]=="|bigTableName|"):			
			self.dictTp["global"]["sets"]["bigTableName"]=self.rsc(self.gui.text_tablename.get("1.0", tk.END))
			
		if(self.dictTp["global"]["sets"]["smaTableName"]=="|smaTableName|"):
			self.dictTp["global"]["sets"]["smaTableName"]=self.rsc(self.gui.text_shorttablename.get("1.0", tk.END))
   
		if(self.dictTp["global"]["ifNoDefinedId"]["id"]=="|id|"):
			self.gc.dictTp["global"]["ifNoDefinedId"]["id"]=self.rsc(self.gui.text_fieldId.get("1.0", tk.END))
   
		if(self.dictTp["global"]["ifNoDefinedId"]["vId"]=="|vId|"):
			self.gc.dictTp["global"]["ifNoDefinedId"]["vId"]=self.rsc(self.gui.text_fieldVid.get("1.0", tk.END))




	def showConfiguration(self):		
		print(self.dictTp["global"]["sets"]["keys"])
		print(self.dictTp["global"]["sets"]["vals"])
		print(self.dictTp["global"]["sets"]["bigTableName"])
		print(self.dictTp["global"]["sets"]["smaTableName"])
		print(self.dictTp["global"]["sets"]["sep"])
		print(self.dictTp["templates"])