#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: Jackie Munguia, changed on August 8, added data to a dictonary and gave the option to delete keys.
# JMunguia, 2022.08.11, Edited file 
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {} #This is the empty dictionary 
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        print('loading data from file')
        objFile = open(strFileName, 'r')
        for row in objFile:
              lstRow = row.strip().split(',')
              dicRow = {
                  'id': int(lstRow[0]), 
                  'title': lstRow[1], 
                  'artist': lstRow[2]
              }
              lstTbl.append(dicRow)
        objFile.close()
             
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = {'id': intID,'title': strTitle, 'artist': strArtist}
        print(lstRow)
        print(lstTbl)
        lstTbl.append(lstRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row['id'], row['title'], row['artist'], sep = ', ')
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        strID = input('What entry do you want to delete?: ')
        intID = int(strID)
        
        newLstTbl = []
        for row in lstTbl:
            if row['id'] != intID:
                newLstTbl.append(row)
        
        lstTbl = newLstTbl
        print('Okay, that entry has been deleted.')
        
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row:
                print(item, "->", row[item])
                strRow += str(row[item]) + ","
                #strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            print(strRow)
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

