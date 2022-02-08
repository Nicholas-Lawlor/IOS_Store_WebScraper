
from bs4 import BeautifulSoup
import requests

url = "https://apps.apple.com/ie/genre/ios-business/id6000"
# array to go through a-z and # apps
alphabet = ['#','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# request URL
page = requests.get(url)
page.status_code
doc = BeautifulSoup(page.text, "html.parser")

# search through class id to get catagories dont need sub catogories as we will be using aplhabet
#cat = doc.find("div",{"id" : "genre-nav"}).find("ul").find("li")
cat = doc.find(class_= "list column first")
catName=[]
catArray =[]

for tag in cat:
    catName.append(tag.text.strip())
    #print(tag.text.strip())




i = 0
# need to extract category make it lower case
# get rid of spaces and & symbol and replace with - 
# This will be used with aplphabet array to allow to go through app a-z URLs 
for i in range(len(catName)):
    catName[i] = catName[i].lower()
    catName[i] = catName[i].replace(" &", "")
    catName[i] = catName[i].replace(" ", "-")

print(catName[25])

for x in catName:
    print(x)

list = doc.find_all("div",{"id" : "selectedgenre"})


result = cat.find("a")
#print(result.attrs)


'''
# an array of all categories   -- done
for a in cat.find_all('a', href=True):
    catArray.append(a['href'])
'''









'''
x = []
for a in cat[0].find_all('a', href=True):
    x.append(a['href'])

list = doc.find_all("div",{"id" : "selectedgenre"})




print(x)

i = 1
page = requests.get(cat[0])
list = page.find_all("div",{"id" : "selectedgenre"})

for b in list[0].find_all('a', href=True):
    y.append(b['href'])

print(y)
    #print ("Found the list:", b['href'])

   # print ("Found the cat:", a['href'])
    #print(litag.text)
#print(result)
   # for b in list[0].find_all('a', href=True):
   #     print ("Found the list:", b['href'])
'''
