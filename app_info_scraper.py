from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import re

url = "https://apps.apple.com/ie/app/facebook/id284882215"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
# page.status_code
# p =page.status_code

cat = soup.find(class_="information-list information-list--app medium-columns l-row")

# working
for x in soup.findAll("h1",{"class":"product-header__title app-header__title"}):
    for span in soup.findAll("span",{"class":"badge badge--product-title"}):
        span.decompose()
    print(x.text)

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

# working
avg_rating = soup.find(class_="we-customer-ratings__averages").text.strip()
print(avg_rating)

#working
rating = soup.find(class_="we-customer-ratings__count small-hide medium-show").text.strip()
print(rating)

# working 
version_date = soup.find(class_="l-row whats-new__content")
version = version_date.find('p').getText()
print(version)
vers_date = version_date.find('time').getText() 
print(vers_date)

# working
in_app_purch = cat.find('dt', string='In-App Purchases').find_next_siblings('dd')
print(in_app_purch[0].text.strip())

# working 
listTags=[]
listTags.append(soup.find('div', {"class": "app-privacy__card"}))
for i in listTags[0].find_next_siblings('div', {"class": "app-privacy__card"}):
    listTags.append(i)    
for i in listTags:
    try:
        #print(i.findChild('h3').text.strip())
        c = i.findChild('h3').text.strip()
        print(c)
        new =i.text.strip()
        #print(new)       
        new_string = new.replace(c, "")
        print(new_string)
    except:
        print("error")

#working extract iphone
x = cat.find('dt', string='Compatibility').find_next('dd')
dl_data = x.find("dt")
print (dl_data.string)

dl_data = x.find("dd")
for dlitem in dl_data:
    print (dlitem.string)
# works
link =soup.find(class_="inline-list inline-list--app-extensions")
for a in link.find_all('a', href=True):
    print(a.text.strip())
    test = a.text.strip()
    if test == "App Support":
        app_support_link = (a['href'])
    elif test == "Privacy Policy":
        privacy_policy = (a['href'])

print(" app sup",app_support_link)
print(" app pol",privacy_policy)

privacy_policy_url = privacy_policy
page = requests.get(privacy_policy_url)
page.status_code
p =page.status_code
print(p)


'''
dt_data = cat.find_all("dt")
for dtitem in dt_data:
    print (dtitem.string)

dl_data = cat.find_all("dd")
for dlitem in dl_data:
    print (dlitem.string)



'''


    

'''
children = li.findChildren("span" , recursive=False)
for child in children:
    print(child).text.strip()
'''
'''
Application name        -- done -- 
App Url                 -- done -- 
Company name            -- done -- 
Develper Website link   -- done --
Age                     -- done -- 
Category                -- done -- 
Price                   -- done -- 
In app purchases        -- done -- 
Rating Avg.             -- done --
Rating Count            -- done --
Description             -- done --
Version                 -- done --
Latest Version date     -- done --
Compatibility           -- done -- 
Size                    -- done -- 
App Support             -- done --
Privacy Policy URL      -- done --
HTTP Status             -- done -- 
Data used to track user -- done --
Data linked to user     -- done --
Data not linked to user -- done --
Data not collected      -- done --
No details provided     -- done --

'''
