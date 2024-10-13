/restaurant/menu/1
/restaurant/booking/



Running server log

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 13, 2024 - 18:23:26
Django version 5.1.1, using settings 'littlelemon.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[13/Oct/2024 18:23:32] "GET /restaurant/ HTTP/1.1" 200 3249
[13/Oct/2024 18:23:32] "GET /restaurant/static/css/style.css HTTP/1.1" 200 4040
[13/Oct/2024 18:23:32,547] - Broken pipe from ('127.0.0.1', 49351)
[13/Oct/2024 18:23:32] "GET /restaurant/static/img/logo.png HTTP/1.1" 304 0
[13/Oct/2024 18:23:32] "GET /restaurant/static/img/favicon.ico HTTP/1.1" 200 15086
[13/Oct/2024 18:23:32,633] - Broken pipe from ('127.0.0.1', 49356)


Database logs

mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 9.0.1 Homebrew

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use littlelemon
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select * from booking;
+----+----------+--------------+----------------------------+
| id | name     | no_of_guests | bookingdate                |
+----+----------+--------------+----------------------------+
|  1 | booking1 |            4 | 2024-10-10 18:00:00.000000 |
|  2 | booking2 |           10 | 2024-10-10 19:00:00.000000 |
+----+----------+--------------+----------------------------+
2 rows in set (0.00 sec)

mysql> 