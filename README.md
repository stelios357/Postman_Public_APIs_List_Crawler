# Postman_Public_APIs_List_Crawler

**1. Steps to Run the Code:** <br /> 

       a. Run the following in cmd : pip install -r requirements.txt
       b. Compile and Run api_crawler.py
       c. Enter Your MySQL hostname, username, password and an existing database name.
    
    

 **2. Details of all the tables and their schema:**<br /> 
 
    a. No command required to create the tables.
    b. There are two tables : api_entires and category with the following table schema:
 
 
**api_entries:**<br /> 
               
                | Field             |: Type         :|: Null |: Key |: Default :| Extra |
                +-------------+------------+------+-----+---------+-------+
                | API               :|: text         :| YES  :|     :| NULL    :|       :|
                | Description       :|: text         :| YES  :|     :| NULL    :|       :|
                | Auth              :|: text         :| YES  :|     :| NULL    :|       :|
                | HTTPS             :|: tinyint(1)   :| YES  :|     :| NULL    :|       :|
                | Cors              :|: text         :| YES  :|     :| NULL    :|       :|
                | Link              :|: text         :| YES  :|     :| NULL    :|       :|
                | Category          :|: text         :| YES  :|     :| NULL    :|       :|
                +-------------+------------+------+-----+---------+-------+
       7 rows in set (0.03 sec)
       
**category:** <br /> 

                     +-------+------+------+-----+---------+-------+
                     | Field | Type | Null | Key | Default | Extra |
                     +-------+------+------+-----+---------+-------+
                     | 0     | text | YES  |     | NULL    |       |
                     +-------+------+------+-----+---------+-------+
                     1 row in set (0.00 sec)

**Number of entries in the table: 300** <br /> 

                        +----------+
                        | count(*) |
                        +----------+
                        |      300 |
                        +----------+
                        
                 1 row in set (0.00 sec)

**3. Done from ???Points to achieve???:** <br />

    a. Your code should follow concept of OOPS 
    b. Support for handling authentication requirements & token expiration of server
    c. Support for pagination to get all data 
    d. Crawled all API entries for all categories and stored it in a database 

**4. Not done from ???Points to achieve???:**<br />

    a. Develop work around for rate limited server 

**5. Improve if given more days:**<br />

    a. Develop work around for rate limited servers. 
    b. Better Exception handling. 
