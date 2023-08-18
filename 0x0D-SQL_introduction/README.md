<p align="center">
      <a href="https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-course-photos.s3.amazonaws.com/34/3819b0a78a424a82ede83dc0cfad4f/Querying-Databases-with-SQL.jpg?auto=format%2Ccompress&dpr=1">
        <img src="https://coursera-course-photos.s3.amazonaws.com/34/3819b0a78a424a82ede83dc0cfad4f/Querying-Databases-with-SQL.jpg?auto=format%2Ccompress&dpr=1" alt="Querying Databases with SQL" width="400" height="400">
    </a>
</p>

<br />

## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=28&pause=1000&repeat=false&width=435&lines=SQL+-+Introduction(%3A )](https://git.io/typing-svg)

<br />

# Install MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
## Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
## For Windows subsystem for linux(WSL) user
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
<br />

## Author

    - Youssef Ahmed Bakier


