## Log Analysis Project
By PAVANKUMAR KOTHAGUNDU

--> This Project is a part of the Udacity Full Stack Web Developer Nanodegree

## Project Description
The project requires students to create and use SQL queries that would fetch results from a large database of a news website.This reporting tool is a Python program using the psycopg2 module to connect to the database.The code requirements suggest the use of only one single query to answer each request.It gives the results of the following queries:
1. What are the most popular three articles of all time.
2. Who are the most popular article authors of all time.
3. Days on which more than 1% of requests lead to errors.

## Project Content
This project contains the following files:
1. LogAnalysis_Udacity.py - This is the main python file that we need to run to obtain the output.
2. newsdata.sql - It is a database file
--> Download this file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. outPut.txt - This file shows the how the result will be obtained.
4. views.sql - It consists of views
5. README.md - Consists of instructions to run.

## Project Requirement Tools
1. Python
2. Postgresql
3. Vagrant (You can download it [here](https://www.vagrantup.com/))
4. VirtualBox (You can download it [here](https://www.virtualbox.org/wiki/Downloads))

## Running of Project
1. First install Vagrant
2. Then install VirtualBox
3. Initialize the vagrant using this command: $ vagrant init ubuntu/xenial64
4. Launch the Vagrant using the following command: $ vagrant up
5. Login to the VirtualMachine using the following command: $ vagrant ssh
6. Exit from current directory $ cd ..
7. Again exit from the directory $ cd ..
8. Change directory path to vagrant $ cd vagrant
9. Update ubunut version using command: $ sudo apt-get update

--> Now we need to install postgresql by following these steps:
10. Install postgresql using the command: sudo apt-get install postgresql
11. Connect to postgres database using the command: psql su - postgres

--> Now we have to install some modules to run the python file
--> We need to follow these steps:
12. Import psycopg2 module to connect database using the command: $ pip install psycopg2
13. Create super user vagrant using this command: $ create user vagrant with superuser createrole createdb replication bypassrls;
14. Create news database using the command: $ create database news;
15. Change ownership of database using this command: $ alter database news owner to vagrant;
16. Exit the current running status using command: $ \q
17. Logout from the current user using command: $ logout
18. Load the data in local database using the command: $ psql -d news -f newsdata.sql
19. Run python LogAnalysis_udacity.py

--> Finally we will get output as in outPut.txt file.