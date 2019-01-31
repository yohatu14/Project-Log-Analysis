#!/usr/bin/env python
import psycopg2
import bleach
from datetime import datetime
dbname = "news"


def connectdb():
    try:
        db = psycopg2.connect(database=dbname)
        c = db.cursor()
    except psycopg2.Error as e:
        print("Error trying to connect database")
        
    query1 = """select viewarticlesauthor.title, countlog.count
    as numvisits from viewarticlesauthor, countlog
    where countlog.path = concat('/article/', viewarticlesauthor.slug)
    order by countlog.count desc limit 3;"""
    query2 = """select viewarticlesauthor.name, sum(countlog.count)
    as numvisits from viewarticlesauthor, countlog
    where countlog.path = concat('/article/', viewarticlesauthor.slug)
    group by viewarticlesauthor.name order by viewarticlesauthor.name desc;"""
    query3 = """select allrequests.date,
    (CAST(ROUND(((errorrequests.count * 1.0) /
    allrequests.count), 4) AS FLOAT))*100
    as valuepercent from allrequests,errorrequests
    where allrequests.date= errorrequests.date
    and (((errorrequests.count * 1.0) /
    allrequests.count ) > 0.01) ORDER BY valuepercent DESC;"""
    runquery1(c, query1)
    runquery2(c, query2)
    runquery3(c, query3)
    db.close()


def runquery1(c, query):
    try:
        c.execute(query)
        result = c.fetchall()
        count = 1
        resultfinal = ""
        print "What are the most popular three articles of all time?"
        for i in result:
            resultfinal = '"' + i[0] + '" --- ' + str(i[1]) + " views"
            print(resultfinal)
            count += 1
    except psycopg2.Error as e:
        print("Error trying to run query1")


def runquery2(c, query):
    try:
        c.execute(query)
        result = c.fetchall()
        count = 1
        resultfinal = ""
        print "Who are the most popular article authors of all time?"
        for i in result:
            resultfinal = '"' + i[0] + '" --- ' + str(i[1]) + " views"
            print(resultfinal)
            count += 1
    except psycopg2.Error as e:
        print("Error trying to run query2")


def runquery3(c, query):
    try:
        c.execute(query)
        result = c.fetchall()
        count = 1
        resultfinal = ""
        print "On which days did more than 1% of requests lead to errors?"
        for i in result:
            objDate = datetime.strptime(str(i[0]), '%Y-%m-%d')
            date = datetime.strftime(objDate, '%b %d, %Y')
            resultfinal = date + " -- " + str(i[1]) + "% errors"
            print(resultfinal)
            count += 1
    except psycopg2.Error as e:
        print("Error trying to run query3")

if __name__ == "__main__":
    connectdb()
