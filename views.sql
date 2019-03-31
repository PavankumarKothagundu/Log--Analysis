CREATE VIEW lg_artcs as SELECT replace(path,'/article/','') as slug, count(*) as views
FROM log
WHERE path<>'/' AND status ='200 OK' GROUP BY path;

CREATE VIEW lg_aths AS
SELECT articles.slug, COUNT(log.id) AS views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.slug
ORDER BY views desc;

CREATE VIEW lg_to AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LgCt
FROM log
GROUP BY Date;

CREATE VIEW lg_fi AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErCt
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;
