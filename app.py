from utils.CsvEngine import CsvEngine
from utils.JsonEngine import JsonEngine

def submitAnotherName():
    more = input("\n Enter a new name if you so wish to. \t")
    csvConsole.writeRow([more, "moringa", "2021+{}".format(len(more))], 1)
    again = input("Added {0}. Press Y to add another row".format(more))
    if("y" in again.lower()):
        submitAnotherName()

print("Hello and welcome to the console.")
print("We've got sample data saved here. \nWould you like to test my smarts?")
proceed = input("\nPress Y to proceed or N to quit.")

if("y" in proceed.lower()):
    print("\n\n\nWill it be the csv file or the json one for today?")
    datachoice = input("Press C to for csv and j for json\t")
    if("c" in datachoice.lower()):
        # not a bug but an unneccessary argument was originally placed in the classes' constructors i.e the testfilename
        csvConsole = CsvEngine("data/userdataset.csv", "unnecessary")
        csvConsole.writeRow(["username","school","year"], 1)
        print("\npssst.... we've populated a new dataset file for you to play with. ")
        username = input("\nWhat's your name? We'd like to write it first to the document\t")
        if(len(username) > 0):
            csvConsole.writeRow([username, "moringa", "2021"], 1)
            submitAnotherName()
            print("Here's all your data\n\n")
            allCsvData = csvConsole.readLines(1)
            for row in allCsvData:
                print(row)
            print("That was really nice!\n")
            deleteUs = input("Delete the file? Press D.")
            if("d" in deleteUs.lower()):
                csvConsole.destroyDocument()
        
    elif("j" in datachoice.lower()):
        jsonConsole = JsonEngine("data/userdataset.json", "unnecessary")
        print("\npssst.... we've populated a new dataset file for you to play with. ")
        username = input("\nWhat's your name? We'd like to write it to the document\t")
        nuInptData = { "name": username, "age": len(username)/2, "city": "Kenya"}
        jsonConsole.writeRow(nuInptData, 1)
        print("Here's all your data\n\n")
        alljsonData = jsonConsole.readLines(1)
        print(alljsonData)
        print("\n\nThat was really nice!\n")
        deleteUs = input("Delete the file? Press D.")
        if("d" in deleteUs.lower()):
            jsonConsole.destroyDocument()
        
            
    else:
        print("\n.......bye bye. ;)")
else:
    print("\n\t\tGoodbye. ;)")

