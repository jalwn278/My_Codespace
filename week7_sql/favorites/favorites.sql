check the database
SELECT * FROM shows ORDER BY title;
SELECT * FROM genres ORDER BY genre;

update the table
UPDATE shows SET title = "Avatar: The Last Airbender" WHERE title LIKE "Avatar%";
and so on

after cleaning if i want to select some data and join it with genres it will be easier
such as SELECT title FROM shows WHERE id IN (SELECT show.id FROM genres WHERE genre = "comedy");
SELECT title, COUNT(*) AS n FROM shows GROUP BY title ORDER BY n DESC LIMIT 10;
