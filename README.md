# Postman_Public_APIs_List_Crawler
Steps to Run the Code:
Compile and Run api_crawler.py
Enter Your MySQL hostname, username, password and an existing database name.
Details of all the tables and their schema:
No command required to create the tables. 
There are two tables : api_entires and categories with the following table schema:
api_entries:
+-------------+------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+-------------+------------+------+-----+---------+-------+
| API               | text         | YES  |     | NULL    |       |
| Description | text         | YES  |     | NULL    |       |
| Auth             | text         | YES  |     | NULL    |       |
| HTTPS         | tinyint(1) | YES  |     | NULL    |       |
| Cors             | text         | YES  |     | NULL    |       |
| Link              | text         | YES  |     | NULL    |       |
| Category      | text         | YES  |     | NULL    |       |
+-------------+------------+------+-----+---------+-------+
7 rows in set (0.03 sec)

categories:



Number of entries in the table: 300

+----------+
| count(*) |
+----------+
|      300 |
+----------+
1 row in set (0.00 sec)

Done from “Points to achieve”:
Your code should follow concept of OOPS
Support for handling authentication requirements & token expiration of server
Support for pagination to get all data
Crawled all API entries for all categories and stored it in a database

Not done:
Develop work around for rate limited server	

Improve if given more days:
Develop work around for rate limited servers.
Better Exception handling.
