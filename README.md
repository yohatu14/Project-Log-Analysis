# Full Stack Web Developer Nanodegree - Udacity
## Project Logs Analysis 
In this project I explore basic concepts regarding python, relational databases, using SQL database with queries and views, interacting with a live database both from the command line and from code.
## Prerequisites
I used for creation and runing:
* Install VirtualBox 3 as a virtualizer for Unix operating system. You can download in this link https://www.virtualbox.org/wiki/Downloads
* User Vagrant as the command line utility for managing the lifecycle of virtual machines, runing in the terminal "vagrant up", next "vagrant ssh".You can install with this instructions https://www.vagrantup.com/docs/installation/ 
* Install Python 2.7.12 as an interpreted, object-oriented programming language inside the virtual machine. You can download here https://www.python.org/downloads/release/python-2712/
* Download data with database "news" in the link https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)
To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:
    psql — the PostgreSQL command line program
    -d news — connect to the database named news which has been set up for you
    -f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file.

##Basic concepts
###Query
A query is a request for data or information from a database table or combination of tables. 
##View
A view is a virtual table based on the result-set of an SQL statement.
##Relational Database (RDB) 
Is a collective set of multiple data sets organized by tables, records and columns

#Solution
##Views
First run this directly on the database:
* create view viewarticlesauthor as select  articles.title, authors.name, articles.slug from articles, authors where articles.author = authors.id;
* create view countlog as select count(*) as count, path from log group by path;
* create view allrequests as select date(time) as date, count(*) as count from log group by date(time);
* create view errorrequests as select date(time) as date, count(*) as count from log where status <> '200 OK' group by date(time);

##Questions
run project.py in the virtual machine
###1. What are the most popular three articles of all time?
###Query
select viewarticlesauthor.title, countlog.count as numvisits from viewarticlesauthor, countlog  where countlog.path = concat('/article/', viewarticlesauthor.slug) order by countlog.count desc limit 3;

###2. Who are the most popular article authors of all time?
###Query
select viewarticlesauthor.name, sum(countlog.count) as numvisits from viewarticlesauthor, countlog  where countlog.path = concat('/article/', viewarticlesauthor.slug) group by viewarticlesauthor.name order by viewarticlesauthor.name desc;

###3. On which days did more than 1% of requests lead to errors?
###Query
select allrequests.date, (CAST(ROUND(((errorrequests.count * 1.0) / allrequests.count), 4) AS FLOAT))*100 as valuepercent from allrequests,errorrequests where allrequests.date = errorrequests.date and (((errorrequests.count * 1.0) / allrequests.count ) > 0.01) ORDER BY valuepercent DESC;


##References 
* Udacity https://www.udacity.com/
* w3schools.com https://www.w3schools.com/ 
* Techopedia https://www.techopedia.com# Project-Log-Analysis
