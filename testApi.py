#!/usr/bin/env python 
import requests
#from requests.auth import HTTPBasicAuth
import json, base64
import pprint
import getpass
import sys

def extractTokenFromJson(rawTextToken):
	try:
		rawTextToken=json.loads(rawTextToken)
		return rawTextToken["Token"]
	except Exception:
		print("\n\n ######################################### ")
		print("   +ERROR OCCURRED DURING AUTHENTICATION.")
		print(" ######################################### \n\n")

def simplifyViewDevicesInDna(jsonOutput):
	for jsonData in jsonOutput["response"]:
		print("--------------------------------------------")
		print("Device ID --->"+str(jsonData["id"]))
		print("Type of device--->"+str(jsonData["type"]))
		print("Mgmt. IP--->"+str(jsonData["managementIpAddress"]))
		print("Mac Address--->"+str(jsonData["macAddress"]))
		print("--------------------------------------------\n")

def post_basicAuthTokenRetreival(user,password):
	apiUrl="https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

	#EXPILICIT WAY - USIG headers
	#Importante --> Decode it to acsii or utf-8, as python 3 stores it as a BYTE string!!!!
	userCredentials=bytes(user+":"+password,"utf-8")
	userAndPass = base64.b64encode(userCredentials).decode("utf-8")

	#Encoded acsii/utf-8 string
	#print("--->"+str(userAndPass))
	#Setting Headers
	headers = {"Authorization":"Basic "+userAndPass}	
	response=requests.post(apiUrl, headers=headers)

	##EASY WAY
	#Using the HTTPBasicAuth from requests.auth
	#response=requests.post(apiUrl, auth=HTTPBasicAuth(user, password))

	#print(response.text)
	tokenExtracted=extractTokenFromJson(response.text)
	return tokenExtracted

def get_NetworkDevicesFromDna(token):
	apiUrl="https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
	headers={"X-Auth-Token":token}
	response=requests.get(apiUrl,headers=headers)

	#Json load is for files
	#Json loads is for strings
	responseJson=json.loads(str(response.text))
	return responseJson

def delete_DNADevice(deviceId,token):
	apiUrl="https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device/"+str(deviceId)+"?isForceDelete=true"
	headers={"X-Auth-Token":token,"Accept":"application/xml","Content-Type":"application/xml"}

	resultAction=requests.delete(apiUrl,headers=headers)
	print("###########################")
	print("         RESULT            ")
	print("###########################\n\n")
	print("   +Action Result---->"+str(resultAction.text))
	print("   +Action Status---->"+str(resultAction.status_code)+"\n\n\n\n")
	print("###########################")
	print("      FINAL OUTPUT         ")
	print("###########################\n\n")

	#Get devices
	#dnaDevices=get_NetworkDevicesFromDna(token)	
	#simplifyViewDevicesInDna(dnaDevices)

def get_SpecificDNADevice(deviceId,token):
	apiUrl="https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device/"+str(deviceId)
	headers={"X-Auth-Token":token}

	resultAction=requests.get(apiUrl,headers=headers)
	print("###########################")
	print("         RESULT            ")
	print("###########################\n\n")
	print("   +Action Result---->"+str(resultAction.text))
	print("   +Action Status---->"+str(resultAction.status_code)+"\n\n\n\n")

def startMyBadAssApp(xargs):	
	#user="devnetuser"
	#password="Cisco123!"
	#user=input("Username: ")
	#password=getpass.getpass(prompt="PASSWORD:")

	user=xargs[0]
	password=xargs[1]

	tokenRetrieved=post_basicAuthTokenRetreival(user,password)
	print("     TOKEN RECEIVED--->"+str(tokenRetrieved)+" \n\n")

	#Get devices
	dnaDevices=get_NetworkDevicesFromDna(tokenRetrieved)

	#Pretty print dna devices
	#pprint.pprint(dnaDevices)

	simplifyViewDevicesInDna(dnaDevices)

	#deviceId="b120c493-0374-4f8b-986a-337707559e96"
	#delete_DNADevice(deviceId,tokenRetrieved)

	#Get specific device from DNA
	#get_SpecificDNADevice(deviceId,tokenRetrieved)

if __name__=="__main__":
	startMyBadAssApp(sys.argv[1:])




