from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import re

#url = "https://apps.apple.com/ie/genre/ios-books/id6018"
url = "https://apps.apple.com/ie/genre/ios-food-drink/id6023?letter=M&page=35"

#url = f"https://apps.apple.com/ie/genre/ios-productivity/id6007?letter=A&page=1#page"
#      https://apps.apple.com/ie/genre/   ios-games   /id6014  ?letter=A   &page=65#page
# url2 = "https://apps.apple.com/ie/genre/ios-{catName[0]}?letter={alphabet[0]}&page={i}#page "
# array to go through a-z and # apps
alphabet = ['*','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# request URL
page = requests.get(url)
page.status_code
p =page.status_code
# get html from url
doc = BeautifulSoup(page.text, "html.parser")
# Create your table
db = sqlite3.connect('urldb.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS links (url VARCHAR(100))''')
# get category class from html 
cat = doc.find(class_= "list column first")
catName=[]
# get category name and id 
for a in cat.find_all('a', href=True):
    yourList   = (a['href'])
    # get category name + id
    #print(yourList[36:65])
    catList = yourList[36:65] 
    catName.append(catList)
# remove books wont need data
catName.remove("books/id6018")
catName.remove("business/id6000")
catName.remove("catalogues/id6022")
catName.remove("developer-tools/id6026")
catName.remove("education/id6017")
catName.remove("entertainment/id6016")
catName.remove("finance/id6015")

print(catName)
app_list_array=[]

'''
# does not get id DONT USE
for tag in cat:

    catName.append(tag.text.strip())
for i in range(len(catName)):
    
    catName[i] = catName[i].lower()
    catName[i] = catName[i].replace(" &", "")
    catName[i] = catName[i].replace(" ", "-")
    print(catName[i])
catName.remove("books")
'''
'''
 3 loops 
 first loop goes through category name 
 second loop goes through alphabet reset third loop
 third loop  which contain two loops while and for 
 the while loop boolean will end when it loops through all pages for each letter in the alphabet array
 the for loop while extraxt all app url to be stored in the database
 loops
'''
continue_alph = False
for xx in catName:
    for yy in alphabet :

        i = 1
        z = 1
        if yy =="M" and continue_alph != True:
            continue_alph = True
            i = 35
            z = 35

        if continue_alph == True:
            print()
            finished = False

            app_list_array=[]
            while finished == False:
                print("Start")
                url3 = f"https://apps.apple.com/ie/genre/ios-{xx}?letter={yy}&page={z}#page"
                print("here i am              ",url3)
                page = requests.get(url3)
                doc = BeautifulSoup(page.text, "html.parser")
                num_list = doc.find(class_="list paginate")
                check_app_list = doc.find(id="selectedcontent")
                first_child = check_app_list.find("ul")
                print("-------------------------")
                print(first_child.findChild())
                print("-------------------------")
                if(first_child.findChild() == None):
                    finished = True

                #print(num_list)
                if num_list is None:
                    url2 = f"https://apps.apple.com/ie/genre/ios-education/id6017?letter={yy}"
                    page = requests.get(url2)
                    doc = BeautifulSoup(page.text, "html.parser")
                    app_list = doc.find(id="selectedcontent")
                    for a in app_list.find_all('a', href=True):
                        yourList   = (a['href'])

                    #print (x,yourList)
                    # Insert your list into the table
                    db = sqlite3.connect('urldb.db')
                    cursor = db.cursor()
                    cursor.execute("INSERT INTO links (url) VALUES(?)", (yourList,))

                    # Commit and close
                    db.commit()
                    db.close()

                    print("done")
                    # print(i)
                    finished = True
                else:
                    for tag in num_list:
                        # print(tag)
                        if (tag.text.strip() == "Next"):
                            if i > z :
                                finished = True

                            i = z
                            i +=1
                            z +=1
                            url3 = f"https://apps.apple.com/ie/genre/ios-{xx}?letter={yy}&page={z}#page"
                        elif (tag.text.strip() == "Previous"):
                            print("asdfghjkl;qwertyuiop")
                        else:
                                
                            print("tag type")
                            print(tag.text.strip())
                            print(" ")
                            z = str(int(tag.text.strip()))
                            z = int(str(z))
                            if (z >= i):
                                url2 = f"https://apps.apple.com/ie/genre/ios-{xx}?letter={yy}&page={z}#page"
                                page = requests.get(url2)
                                doc = BeautifulSoup(page.text, "html.parser")
                                # get app url
                                app_list = doc.find(id="selectedcontent")
                                for a in app_list.find_all('a', href=True):
                                    yourList   = (a['href'])

                                    # Insert your list into the table
                                    db = sqlite3.connect('urldb.db')
                                    cursor = db.cursor()
                                    cursor.execute("INSERT INTO links (url) VALUES(?)", (yourList,))
                                    # Commit and close
                                    db.commit()
                                    db.close()

                    if (tag.text.strip() != "Next"):
                        z+=1
                        url2 = f"https://apps.apple.com/ie/genre/ios-education/id6017?letter={yy}&page={z}#page"
                        page = requests.get(url2)
                        doc = BeautifulSoup(page.text, "html.parser")
                        app_list = doc.find(id="selectedcontent")
                        for a in app_list.find_all('a', href=True):
                            yourList   = (a['href'])

                        #print (x,yourList)
                                # Insert your list into the table
                        db = sqlite3.connect('urldb.db')
                        cursor = db.cursor()
                        cursor.execute("INSERT INTO links (url) VALUES(?)", (yourList,))

                        # Commit and close
                        db.commit()
                        db.close()

                        print("done")
                        # print(i)
                        finished = True
