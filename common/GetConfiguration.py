
import tkinter as tk
import json


class GetConfiguration():
	def __init__(self,tp):
		self.arrayValues=""
		self.tp=tp
		self.arrayLanguajes=[]
		self.arrayDatabases=[]
		self.arrayFunctions=[]
     
		self.dictTp=tp.getStr()
	
	def getStr(self):
		# print (self.config)
		return self.config

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
   
	def showConfiguration(self):
		print(self.dictTp["global"]["sets"]["key"])
		print(self.dictTp["global"]["sets"]["val"])
		print(self.dictTp["global"]["sets"]["keys"])
		print(self.dictTp["global"]["sets"]["vals"])
		print(self.dictTp["global"]["sets"]["bTabName"])
		print(self.dictTp["global"]["sets"]["sTabName"])
		print(self.dictTp["global"]["sets"]["sep"])
		print(self.dictTp["templates"])
  
	def loadLangaujes(self):
		for keyLanguaje in self.dictTp["templates"]:	
			self.arrayLanguajes.append(keyLanguaje)		
		return self.arrayLanguajes
	
	def loadDatabases(self,keyTemplate):
		for key in self.dictTp["templates"][keyTemplate] :	
			self.arrayDatabases.append(key)		
		return self.arrayDatabases

	def loadFunctions(self,keyTemplate,keyDatabases):
		self.arrayFunctions.append("All")
		for key in self.dictTp["templates"][keyTemplate][keyDatabases] :	
			self.arrayFunctions.append(key)		
		return self.arrayFunctions
  			
  		
  
	def getConfAndParams(self,gui,inArray,outArray):
		if(self.dictTp["global"]["sets"]["key"]=="((sourceValue))"):
			self.dictTp["global"]["sets"]["key"]=inArray
		else:
			self.dictTp["global"]["sets"]["key"]=outArray
   
		if(self.dictTp["global"]["sets"]["keys"]=="((sourceValues))"):
			self.dictTp["global"]["sets"]["keys"]=inArray
		else:
			self.dictTp["global"]["sets"]["keys"]=outArray
   
		if(self.dictTp["global"]["sets"]["val"]=="((targetValue))"):
			self.dictTp["global"]["sets"]["val"]=outArray
		else:
			self.dictTp["global"]["sets"]["val"]=inArray
   
		if(self.dictTp["global"]["sets"]["vals"]=="((targetValues))"):
			self.dictTp["global"]["sets"]["vals"]=outArray
		else:
			self.dictTp["global"]["sets"]["vals"]=inArray
   
		if(self.dictTp["global"]["sets"]["bTabName"]=="((bigTableName))"):
			self.dictTp["global"]["sets"]["bTabName"]=gui.text_tablename.get("1.0", tk.END) 
		if(self.dictTp["global"]["sets"]["sTabName"]=="((smaTableName))"):
			self.dictTp["global"]["sets"]["sTabName"]=gui.text_shorttablename.get("1.0", tk.END) 
		
		# print("Parametros a combobox");
		
  
		
		""" print(key)
			for key2 in self.dictTp["templates"][key]:		
				self.arrayDatabases.append(key2)
				print(key2)	
				for key3 in self.dictTp["templates"][key][key2]:			
					self.arrayFunctions.append(key3) """
		
		print(self.arrayLanguajes)	
#  		print(self.arrayDatabases)				
# 		print(self.arrayFunctions)
			
		# print(self.dictTp)
	