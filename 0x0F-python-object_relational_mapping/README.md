# 0x0F. Python - Object-relational mapping

## Description
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

<br />

## Install and activate venv
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```
## Install MySQLdb module version 2.0.x
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```
## Install SQLAlchemy module version 1.4.x
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
<br />

## Table of Contents
Files | Description
----- | -----------
[0-select_states.py](./0-select_states.py) | lists all states from the database hbtn_0e_0_usa
[1-filter_states.py](./1-filter_states.py) | lists all states with a name starting with N from the database hbtn_0e_0_usa
[2-my_filter_states.py](./2-my_filter_states.py) | displays all values in the states table of hbtn_0e_0_usa where name matches the argument
[3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | same as file 2-my_filter_states.py but safe from SQL injection
[4-cities_by_state.py](./4-cities_by_state.py) | lists all cities from the database hbtn_0e_4_usa
[5-filter_cities.py](./5-filter_cities.py) | lists all cities of state giving as argument, using the database hbtn_0e_4_usa

## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)
