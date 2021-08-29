#!/usr/bin/env python
# coding: utf-8

# In[35]:


"""Link : https://docs.google.com/document/d/1xACnZnnBc4u704WQ3lFl1ICMFTVgmUuR6S7n4IPoyxo/edit"""


# In[36]:


import requests
import pandas as pd
import time
from time import sleep
from pandas.io import sql
from sqlalchemy import create_engine


# In[37]:


def getToken():
    url = "https://public-apis-api.herokuapp.com/api/v1/auth/token"
    payload={}
    headers = {}
    sleep(10)
#---------Support for handling authentication requirements & token expiration of server here:------------------"""   
    try:
        r = response = requests.request("GET", url, headers=headers, data=payload)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print()
        print ("Http Error:",errh)
        print('Handling the error please wait!')
        tok = getToken()
        print('Error handled!!')
        print()
        return tok
    except requests.exceptions.ConnectionError as errc:
        print()
        print ("Error Connecting:",errc)
        print('Handling the error please wait!')
        tok = getToken()
        print('Error handled!!')
        print()
        return tok
    except requests.exceptions.Timeout as errt:
        print()
        print ("Timeout Error:",errt)
        print('Handling the error please wait!')
        tok = getToken()
        print('Error handled!!')
        print()
        return tok
    except requests.exceptions.RequestException as err:
        print()
        print ("OOps: Something Else",err)
        print('Handling the error please wait!')
        tok = getToken()
        print('Error handled!!')
        print()
        return tok
        
    tokenn = response.json()
    #print(tokenn['token'])
    return  "Bearer " + tokenn['token']
    


# In[38]:


def getCategories():
    token = getToken()
    categories_name = []
    url = 'https://public-apis-api.herokuapp.com/api/v1/apis/categories?page=1'
    payload={}
    headers = { "Authorization": token}
    response = requests.request("GET", url, headers=headers, data=payload)
    categories_info = response.json()
    categories_name = []
    
#----------------SUPPORT FOR PAGING HERE : --------------------"""
    
    for i in range(1, int(categories_info['count']/len(categories_info['categories']))+2):
        url = 'https://public-apis-api.herokuapp.com/api/v1/apis/categories?page=' + str(i)
        payload={}
        headers = { "Authorization":token}
        response = requests.request("GET", url, headers=headers, data=payload)
        categories_info = response.json()
        categories_name += categories_info['categories']
        #print(categories_name)
    return categories_name


# In[39]:


def get_listofApi():
    i = 0
    d ={}
    categories_name = getCategories()
    print()
    print('There are ' + str(len(categories_name)) + ' categories:')
    print(categories_name)
    print()
    print()
    for category in categories_name:
        token = getToken()
        print(i, end = '. ')
        i += 1
        print()
        print('-------------------------------------------------------------')
        print()
        print('Current categgory : ' + category)
        url = "https://public-apis-api.herokuapp.com/api/v1/apis/entry?page=1&category=" + category
        payload={}
        headers = {"Authorization": token}
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
        except Exception as e:
            print(e)
        temp = response.json()
        try:
            table = temp['categories']
            temp =  pd.DataFrame(table)
            print(temp.head())
            d[category] = temp
        except Exception as e:
            print(e, 'pass')
        sleep(10)
    return d, categories_name


# In[43]:


def createTable(hostname, dbname, uname, pwd):
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))
    api, categories = get_listofApi()
    categories = pd.DataFrame(categories)
    api_keys = list(api.keys())
    ind = 0
    while len(api[api_keys[ind]]) == 0:
        ind += 1
    final_df = api[api_keys[ind]]
    print(ind)
    for categ in api_keys[ind+1:]:
        if len(api[categ]) > 0:
            final_df.reset_index()
            now = api[categ]
            now.reset_index()
            final_df = pd.concat([final_df, now], axis = 0)
    l = 0
    for categ in api_keys:
            l += len(api[categ])
#-----------------------Crawled all API entries for all categories and stored it in a database---------------------"""
    
    final_df.to_sql('api_entries', engine, index=False)
    categories.to_sql('category', engine, index=False)
    print()
    print('RUN SUCCESFULLY COMPLETE!!')
    print('Table has total ' + str(l) + ' entries.')
    print('Saved tables to database : ' + dbname + "with table name api_entries , category." )


# In[42]:


def main():
    print("Hey the program is staring please create a database in mysql.")
    print('Please provide the following i/p for your databse:')
    print("Your mysql hostname : (usually localhost)")
    hostname = input()
    print("Your mysql user_name :")
    uname= input()
    print("Password to your" + uname + "mysql user:")
    pwd= input()
    print("Your mysql DataBase name where you want to store the scraped tables :")
    dbname= input()
    print()
    print('This program will take some time to run. Please be patient and let the program crawl the API tables for you. The tables will be stored in your mysql database.')
    createTable(hostname, dbname, uname, pwd)


# In[33]:


if __name__ == "__main__":
    main()

