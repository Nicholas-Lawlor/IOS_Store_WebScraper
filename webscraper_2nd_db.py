from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import re
import time
from datetime import timedelta

# Create your table
start_time = time.monotonic()
db = sqlite3.connect('app_info_urldata2.db')
cursor = db.cursor()

sql_command = '''CREATE TABLE IF NOT EXISTS app_info_urldata2 (
	id integer PRIMARY KEY AUTOINCREMENT,
    app_name text,
    app_url text,
    company_name text,
    develper_website_link text,
    age text,
    category text,
    price text,
    in_app_purchases text,
    rating_avg text,
    rating_count text,
    description text,
    version text,
    latest_version_date text,
    compatibility text,
    size text,
    app_support text,
    privacy_policy_url text,
    HTTP_status text,
    data_used_to_track_user text,
    data_linked_to_user text,
    data_not_linked_to_user text,
    data_not_collected text,
    no_details_provided text
)
'''

cursor.execute(sql_command)
 
# Commit the changes to the database
db.commit()



# working
def app_title(soup):
    global app_name
    for x in soup.findAll("h1",{"class":"product-header__title app-header__title"}):
        for span in soup.findAll("span",{"class":"badge badge--product-title"}):
            span.decompose()
        app_name = x.text
        #print(app_name)
    return app_name

    # works
def provider_link(soup):
    providerurl = ""
    try :
        link =soup.find(class_="product-header__identity app-header__identity")
        for a in link.find_all('a', href=True):
            providerurl   = (a['href'])
    except:
        providerurl = "Error"
    #print(provider_link)
    return providerurl
    
#works
def provider(soup):
    cat = soup.find(class_="information-list information-list--app medium-columns l-row")
    try :
        provider = cat.find('dt', string='Provider').find_next_siblings('dd')
        provider = provider[0].text.strip()
        #print(provider)
    except:
        #print("Privider wrong")
        provider = "Error"
    return provider

# works
def size(soup):
    cat = soup.find(class_="information-list information-list--app medium-columns l-row")
    try :
        size = cat.find('dt', string='Size').find_next_siblings('dd')
        size = size[0].text.strip()
        #print(size)
    except:
        #print("size wrong")
        size = "Error"
    return size

# works
def category(soup):
    cat = soup.find(class_="information-list information-list--app medium-columns l-row")
    try :
        category = cat.find('dt', string='Category').find_next_siblings('dd')
        category = category[0].text.strip()
        #print(category)
    except:
        #print("category wrong")
        category = "Error"
    return category

    # works
def age(soup):
    cat = soup.find(class_="information-list information-list--app medium-columns l-row")
    try :
        age = cat.find('dt', string='Age Rating').find_next_siblings('dd')
        age = age[0].text.strip()
        #print(age)
    except:
        #print("age wrong")
        age = "Error"
    return age

    # works
def price(soup):
    cat = soup.find(class_="information-list information-list--app medium-columns l-row")
    try :
        price = cat.find('dt', string='Price').find_next_siblings('dd')
        price = price[0].text.strip()
        #print(price)
    except:
        #print("price wrong")
        price = "Error"
    return price

def app_info(soup):
    # working
    try :
        app_info = soup.find_all(class_="small-hide medium-show")
        app_info =soup.find(class_="section__description").text.strip()
        #print(app_info)
    except:
        #print("app_info wrong")
        app_info = "Error"
    return app_info

    # working
def avg_rating(soup):
    try:
        avg_rating = soup.find(class_="we-customer-ratings__averages").text.strip()
        #print(avg_rating)
    except:
        avg_rating = "No Average Rating"
    #print(avg_rating)
    return avg_rating


    #working
def rating(soup):
    try:
        rating = soup.find(class_="we-customer-ratings__count small-hide medium-show").text.strip()
        #print(rating)
    except:
        rating = "No Rating"
    #print(rating)
    return rating


    # working 
def version(soup):
    version_date = soup.find(class_="l-row whats-new__content")
    try:
        version = version_date.find('p').getText()
        #print(version)
    except:
        version = "none"
    #print(version)
    return version

    # working
def vers_date(soup):
    version_date = soup.find(class_="l-row whats-new__content")
    try:
        vers_date = version_date.find('time').getText() 
        #print(vers_date)
    except:
        vers_date = "none"
    #print(vers_date)
    return vers_date

    # working
def in_app_purch(soup):
    try:
        cat = soup.find(class_="information-list information-list--app medium-columns l-row")
        in_app_purch = cat.find('dt', string='In-App Purchases').find_next_siblings('dd')
        in_app_purch = in_app_purch[0].text.strip()
        #print(in_app_purch)
    except:
        in_app_purch = "None"  
    #print(in_app_purch)
    return in_app_purch






    #working extract iphone
def ver_phone(soup):
    cat = soup.find(class_="information-list information-list--app medium-columns l-row")
    try:
        x = cat.find('dt', string='Compatibility').find_next('dd')
        dl_data = x.find("dt")
        #print (dl_data.string)

        dl_data = x.find("dd")
        for dlitem in dl_data:
            dlitem = dlitem.string
        # print (dlitem)
    except:
        #print("app_info wrong")
        dlitem = "Error" 
    return dlitem
    


def link(soup):
    # works
    privacy_policy = "No Privacy Policy"
    app_support_link = "No app Support link "
    link =soup.find(class_="inline-list inline-list--app-extensions")
    try:
        for a in link.find_all('a', href=True):
            #print(a.text.strip())
            test = a.text.strip()
            if test == "App Support":
                app_support_link = (a['href'])
            elif test == "Privacy Policy":
                privacy_policy = (a['href'])
    except:
        print("ERORR")


    #print(" app sup",app_support_link)
    #print(" app pol",privacy_policy)
    return app_support_link,privacy_policy

def link_check(privacy_policy_link):
    if privacy_policy_link == "No Privacy Policy":
        result= "No Privacy Policy Link"
    else:
        try :
            #print("i am here")
            privacy_policy_url = privacy_policy_link
            #page = requests.get(privacy_policy_url)
            page = requests.get(privacy_policy_url, timeout=10)
            page.status_code
            result =page.status_code
            #print("i am done")
            #print(result)
        except:
            result = "unkown Error"
            #print(result)
    return result

    
    

#list_url =["https://apps.apple.com/ie/app/go-nowe-miasto-nad-pilic%C4%85/id1574961647","https://apps.apple.com/ie/app/f3-crossroads-il/id1562088347","https://apps.apple.com/ie/app/face-emojis-2-sticker-pack/id1465897354"]

sqliteConnection = sqlite3.connect('urldb.db')
cursor2 = sqliteConnection.cursor()
sqlite_select_query = """SELECT * from links"""
cursor2.execute(sqlite_select_query)
list_url = cursor2.fetchall()
#print("Total rows are:  ", len(list_url))

#url = "https://apps.apple.com/ie/app/facebook/id284882215"



#cat = soup.find(class_="information-list information-list--app medium-columns l-row")
countapp = 1
for urls in list_url :

    if countapp % 100 == 0 :
        end_time = time.monotonic()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("-------------------------------",timedelta(seconds=end_time - start_time),"--------------------------")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    if countapp >= 529907 :
       # print("----------------------------------START------------------------------------------------")
        
        countapp += 1
        if countapp % 10 == 0:
            print("----------------------------------+ ",countapp," +---------------------------------------------")
        url = urls[0]
        #print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        
        
        # works
        app_name  = app_title(soup)
        #print(app_name)

        providerlink = provider_link(soup)
        #print(providerlink)

        provider_n = provider(soup)
        #print(provider_n)

        app_size = size(soup)
        #print(app_size)

        category_n = category(soup)
        #print(category_n)

        age_user = age(soup)
        #print(age_user)

        app_price = price(soup)
        #print(app_price)

        info_app = app_info(soup)
        #print(info_app)

        rating_avg = avg_rating(soup)
        #print(rating_avg)

        app_rating = rating(soup)
        #print(app_rating)

        app_version = version(soup)
        #print(app_version)

        app_version_date = vers_date(soup)
        #print(app_version_date)

        purch_in_app = in_app_purch(soup)
        #print(purch_in_app)

        # working 
        try:
            NDP =""
            DUTY =""
            DNLU =""
            DLU =""
            DNC =""
            listTags=[]
            listTags.append(soup.find('div', {"class": "app-privacy__card"}))
            for i in listTags[0].find_next_siblings('div', {"class": "app-privacy__card"}):
                listTags.append(i)    
            for i in listTags:
            

                try:
                    #print(i.findChild('h3').text.strip())
                    c = i.findChild('h3').text.strip()
                    if c == "Data Used to Track You" :
                        #print(c)
                        new =i.text.strip()
                        #print(new)       
                        DUTY = new.replace(c, "")
                        #print(new_string)
                    elif c == "Data Not Linked to You" :
                        #print(c)
                        new =i.text.strip()
                        #print(new)       
                        DNLU = new.replace(c, "")
                    elif c == "Data Linked to You" :
                        #print(c)
                        new =i.text.strip()
                        #print(new)       
                        DLU = new.replace(c, "")
                    elif c == "Data Not Collected" :
                        #print(c)
                        new =i.text.strip()
                        #print(new)       
                        DNC = new.replace(c, "")
                    elif c == "No Details Provided" :
                        #print(c)
                        new =i.text.strip()
                        #print(new)       
                        NDP = new.replace(c, "")
                    else :
                        print("++++++++++++++++++++++")

                except:
                    print("error")

                #print(DUTY)
                #print(DNLU)
                #print(DLU)
                #print(DNC)
                #print(NDP)
        except:
            NDP =""
            DUTY =""
            DNLU =""
            DLU =""
            DNC =""
            print("error")

        phone_ver = ver_phone(soup)
        #print(phone_ver)

        link_app_support, privacy_policy_link = link(soup)
        #print(link_app_support)
        #print(privacy_policy_link)

        link_pricacy_policy = link_check(privacy_policy_link)
        #print(link_pricacy_policy)
        
        # Insert your list into the table
        db = sqlite3.connect('app_info_urldata2.db')
        cursor = db.cursor()
        cursor.execute("INSERT INTO app_info_urldata2 (app_name,app_url,company_name,develper_website_link,age,category,price,in_app_purchases,rating_avg,rating_count,description,version,latest_version_date,compatibility,size,app_support,privacy_policy_url,HTTP_status,data_used_to_track_user,data_linked_to_user,data_not_linked_to_user,data_not_collected,no_details_provided) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (app_name, url, provider_n, providerlink, age_user, category_n, app_price, purch_in_app, rating_avg
        , app_rating, info_app, app_version, app_version_date, phone_ver, app_size, link_app_support, privacy_policy_link, link_pricacy_policy
        , DUTY, DLU, DNLU, DNC, NDP,))
        # Commit and close
        db.commit()
        db.close()
        #print("----------------------------------END------------------------------------------------")
        cursor2.close()
    else:
        countapp +=1

