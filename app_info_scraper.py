from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import re

url = "https://apps.apple.com/ie/app/a-b-cabs/id1151761230"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
page.status_code
p =page.status_code

cat = soup.find(class_="information-list information-list--app medium-columns l-row")


# works
link =soup.find(class_="product-header__identity app-header__identity")
for a in link.find_all('a', href=True):
    provider_link   = (a['href'])

print(provider_link)

#works
provider = cat.find('dt', string='Provider').find_next_siblings('dd')
print(provider[0].text.strip())

# works
size = cat.find('dt', string='Size').find_next_siblings('dd')
print(size[0].text.strip())


# not working extract all only need iphone
x = cat.find('dt', string='Compatibility').find_next_sibling('dd')
#print(x.text.strip())
#print(type(x))
#print (x.find(text="Compatibility:").findNext('dd').contents[0])
#print(x)


# works
category = cat.find('dt', string='Category').find_next_siblings('dd')
print(category[0].text.strip())


# works
age = cat.find('dt', string='Age Rating').find_next_siblings('dd')
print(age[0].text.strip())



# works
price = cat.find('dt', string='Price').find_next_siblings('dd')
print(price[0].text.strip())

# working
app_info = soup.find_all(class_="small-hide medium-show")
app_info =soup.find(class_="section__description").text.strip()
print(app_info)

# not working extract date and version need to seperate
version = soup.find(class_="l-row whats-new__content")
print(version.text.strip())
'''
dt_data = cat.find_all("dt")
for dtitem in dt_data:
    print (dtitem.string)

dl_data = cat.find_all("dd")
for dlitem in dl_data:
    print (dlitem.string)


--------- not working extracts span tag and h1 only need h1 -------
app_name = soup.select('h1', {'class' : 'product-header__title app-header__title'})[0].text.strip()
#app_name = soup.select('h1.product-header__title app-header__title')[0].text.strip()
print(app_name)
print(x.text.strip())
'''



'''
Application name        -- not done -- 
App Url                 -- done -- 
Company name            -- done -- 
Develper Website link   -- done --
Age                     -- done -- 
Category                -- done -- 
Price                   -- done -- 
In app purchases 
Rating Avg.
Rating Count
Description             -- done --
Version 
Latest Version date 
Compatibility           -- not done -- 
Size                    -- done -- 
App Support             -- not done --
Privacy Policy URL
HTTP Status
Data used to track user
Data linked to user
Data not linked to user
Data not collected
No details provided

'''
