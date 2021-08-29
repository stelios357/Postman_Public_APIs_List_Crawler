# Postman_Public_APIs_List_Crawler

**1. Steps to Run the Code:**<br /> 
    a. Compile and Run api_crawler.py<br /> 
    b. Enter Your MySQL hostname, username, password and an existing database name.<br /> 
    
    

 **2. Details of all the tables and their schema:**<br /> 
    a. No command required to create the tables. <br /> 
    b. There are two tables : api_entires and categories with the following table schema:<br /> 
                 api_entries:<br /> 
               
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

**categories:** <br /> 

    c. Number of entries in the table: 300

                        +----------+
                        | count(*) |
                        +----------+
                        |      300 |
                        +----------+
                        1 row in set (0.00 sec)
<br /> 
**3. Done from “Points to achieve”:** <br />
      a. Your code should follow concept of OOPS <br />
      b. Support for handling authentication requirements & token expiration of server <br />
      c. Support for pagination to get all data <br />
      d. Crawled all API entries for all categories and stored it in a database <br />
<br /> 
**4. Not done:**
      a. Develop work around for rate limited server <br />	
<br /> 
**5. Improve if given more days:**
      a. Develop work around for rate limited servers. <br />
      b. Better Exception handling. <br />
