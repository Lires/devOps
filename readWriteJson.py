#!/usr/bin/python python
import json

def readJson(fileName):
    with open(fileName,"r") as f:
        jsonData=json.load(f)
    f.close()
    #print(str(jsonData["birthdays"]))
    return jsonData["birthdays"]

def lookupBirthday(jsonData):
    birthdayToLookup=input("\n\n>>> Who's birthday do you want to look up? ")

    for data in jsonData:
        if(str(data["name"])==birthdayToLookup):
            print("{name}'s birthday is {theBirthdayDate}".format(name=str(data["name"]),theBirthdayDate=str(data["birthday"])))

def appendDetails(fileName,birthdayData,dataToAppend):
    dataToAppend={}

    #Append
    birthdayData.append(dataToAppend)
    
    #dump() will write Python data to a file-like object. We use this when we want to serialize our Python data to an external JSON file.
    with open(fileName, 'w') as f:
        json.dump(birthdayData, f,indent=4)
    f.close()

def insertWrite(birthdayData,fileName):
    #Insert/Write
    print(">>> Lets insert birthday details to the json file...")
    
    insertDetails=True
    while insertDetails==True:
        stopInsert=input("\n\n>>>>STOP INSERT(Y/N)? ")
        if(stopInsert=="Y" or stopInsert=="y"):
            insertDetails=False
        nameToInsert=input("\n\n>>> Name: ")
        birthdayToInsert=input(">>> Birthday: ")

        dataToAppend={"name":nameToInsert,"birthday":birthdayToInsert}

        #dumps() will write Python data to a string in JSON format. This is useful if we want to use the JSON elsewhere in our program, 
        # or if we just want to print it to the console to check that it’s correct.
        print("\n\n\nWill write the following to the file: "+str(json.dumps(dataToAppend)))

        #Call the append function
        appendDetails(fileName,birthdayData,dataToAppend)

def showBirthdays(fileName,jsonData):
    print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
    for data in jsonData:
        name=str(data["name"])
        print(str(name))
        birthday=str(data["birthday"])
        
def deleteBirthday(fileName):
    
    with open(fileName) as f:
        birthdays=json.load(f)
    f.close()

    #print("----->"+str(birthdays))

    birthdayDateToDelete=input("  >>>INSERT BIRTHDAY DATE TO DELETE: ")

    count=0
    for birthdayDetail in birthdays["birthdays"]:
        if(birthdayDetail["birthday"]==birthdayDateToDelete):
            print("     +DELETING!")
            #Delete entry
            birthdays["birthdays"].pop(count)
        count=count+1

    #Save changes
    with open(fileName,"w") as f:
       json.dump(birthdays,f)
    f.close()

def startUp():
    #File name
    fileName="birthdays.json"

    #Read
    jsonData=readJson(fileName)

    #Call show birthdays
    showBirthdays(fileName,jsonData)

    #Call lookup method(second read)
    lookupBirthday(jsonData)

    #Call insert method
    #insertWrite(jsonData,fileName)

    #Delete
    deleteBirthday(fileName)


if __name__=="__main__":
    startUp()