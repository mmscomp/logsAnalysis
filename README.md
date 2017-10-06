# Logs Analysis
Source code for reporting data from a news database

# Installation
Install python 2.7.12, Virtual Machine (VM) box, and Vagrant
Download VM configuration from https:/github.com/udacity/fullstack-nanodegree-vm. 

# Run the VM
Change to downloaded directory. This contains VM files.
To make vagrant online, run 'vagrant up'.
With vagrant ssh, do update and upgrade.
This will install required files including psycopg2 for database connection
Change to shared vagrant directory.

# Run the program
Put 'newsdata.sql' file into the vagrant directory.
Run 'psql -d news -f newsdata.sql' (w/o the quotes)  to load the data.
This will connect to the postgres server and create tables with data after
executing the SQL commands on the newsdata.sql file.

Besides required files, there is one python file - report.py.

This file can be run by typing 'python report.py' on the terminal.
For successful connection to database server  appropriate password must be used.

Successful execution of the program produces a text file - report.txt,
which contains the answers to the questions regarding the news database.
