#!/usr/bin/env python


import psycopg2

# Leading 3 articles


def Lead_Articles():
    con = psycopg2.connect(
          dbname="news", user='vagrant', password='vagrant')
    cr = con.cursor()
    cr.execute(qr1)
    sols = cr.fetchall()
    ct = 1
    for rslt in sols:
        numbr = '(' + str(ct) + ') "'
        tl = rslt[0]
        views = '"' + str(rslt[1]) + " views"
        print(numbr + tl + views)
        ct = ct+1

# Greatest Article Authors


def Great_Authors():
    con = psycopg2.connect(
          dbname="news", user='vagrant', password='vagrant')
    cr = con.cursor()
    cr.execute(qr2)
    sols = cr.fetchall()
    ct = 1
    for rslt in sols:
        numbr = '(' + str(ct) + ') "'
        tl = rslt[0]
        views = '"Authors' + str(rslt[1]) + " views"
        print(numbr + tl + views)
        ct = ct+1

# Days Leading to errors


def Lganyl_err():
    con = psycopg2.connect(
          dbname="news", user='vagrant', password='vagrant')
    cr = con.cursor()
    cr.execute(qr3)
    sols = cr.fetchall()
    for rslt in sols:
        print(' On ' + str(rslt[0]) + '===>' + '%.1f' % rslt[1] + '% errors\n')


print(" \n  *What are the most leading three articles of all time ?")
qr1 = ''' SELECT title, views FROM lg_artcs INNER JOIN articles ON
    articles.slug = lg_artcs.slug ORDER BY views desc LIMIT 3; '''
Lead_Articles()

print("\n  **Who are the greatest article authors of all time ?")
qr2 = '''
    SELECT lg_aths.name, sum(lg_artcs.views) AS views
            FROM lg_aths, lg_artcs
            WHERE lg_aths.slug = lg_artcs.slug
            GROUP BY name ORDER BY views desc;
    '''
Great_Authors()

print("\n ***Days on which more than 1% of requests lead to errors ?")
qr3 = '''
    SELECT lg_fi.date, round(100.0*erct/lgct,2) as percent
            FROM lg_to, lg_fi
            WHERE lg_to.date = lg_fi.date
            AND erct > lgct/100;
    '''
Lganyl_err()
