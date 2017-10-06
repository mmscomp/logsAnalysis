#!/usr/bin/python2

import sys
import psycopg2
import traceback
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine


# Dictionary to convert date
datestyle = {'01': 'January', '02': 'February', '03': 'March', '04': 'April',
             '05': 'May', '06': 'June', '07': 'July', '08': 'August',
             '09': 'September', '10': 'October', '11': 'November',
             '12': 'December'}
try:

    # Connect to database, should use own password
    con = psycopg2.connect(database='news', user='matt', password='abcde',
                           host='127.0.0.1', port=5432)

    # Create a cursor to execute queries
    cursor = con.cursor()

    # SQL for question 1
    cursor.execute("""Select title, count(path) as views from articles, log
                      where articles.slug = substring(log.path, 10)
                      GROUP BY articles.title ORDER BY views DESC limit 3""")

    # Fetch date from the database in the form of a list of tuples
    rows = cursor.fetchall()

    # Open file to write data to
    with open('report.txt', 'w') as f:
        f.write("1. What are the most popular three articles of all time?\n\n")
        for x in rows:
            st = u'\u2022'.encode('utf-8') + " " + x[0] + " -- " + \
                 str(x[1]) + " views\n"

            f.write(st)
    f.close()

    # Run a select statemwnt for question 2
    cursor.execute("""SELECT name, count(path) as views from authors,
                      articles, log where authors.id = articles.author
                      and articles.slug = substring(log.path,10) GROUP
                      BY authors.name ORDER BY views DESC""")
    lines = cursor.fetchall()

    # open the same file to append the result of above query
    with open('report.txt', 'a') as f:
        f.write("\n 2. Who are the most popular article authors of" +
                " all time?\n\n")
        for x in lines:
            line = u'\u2022'.encode('utf-8') + " " + x[0] + " -- " + \
                   str(x[1]) + " views\n"
            f.write(line)
    f.close()

    # Run a select sql statement for question 3
    cursor.execute("""Select to_char(time, 'FMMonth, FMDD, YYYY'), round(pererror::decimal, 2) from(Select time::timestamp::date,
                      (occ/total::float)*100 perError from (Select time::
                       timestamp::date, count(*) total, sum(case when status =
                       '200 OK' then 0 else 1 end) occ  from log GROUP BY
                       time::timestamp::date) foo) boo where pererror > 1""")
    times = cursor.fetchall()

    # Open the file again to append the result from the third query
    with open('report.txt', 'a') as f:
        f.write("\n 3. On which days did more than 1% of requests lead to" +
                "errors?\n\n")
        for x in times:
            day = u'\u2022'.encode('utf-8') + " " + \
                  datestyle[str(x[0])[5:7]] + \
                  " " + str(x[0])[8:] + ", " + str(x[0])[:4] + " -- " + \
                  str(round(x[1], 1)) + "% errors\n"
            f.write(day)
    f.close()
    cursor.close()
    con.close()

except psycopg2.Error as err:
    print "Unable to connect"
    print err
    print err.pgcode
    print err.pgerror
    print traceback.format_exc()
