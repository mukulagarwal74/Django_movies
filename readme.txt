Dump the data from sqlite to json for postgresql
Create a data base in postgresql local server
Make the changes to the setting.py file mention the database name as same as the in postgresql
delete the previous migrations
run : python manage.py makemigrations
if all good then 
run : python manage.py migrate
if all good then, you can see the changes in the database
