INSERT INTO books (id, title, author_id, published_year, price)
VALUES
(9788072522392, 'Jak drahé je zdarma?', 1, 2009, 215),
(9788087950173, 'Jak jsme se stali kolonií', 2, 2015, 220),
(9788022209236, 'Nepodľahnite alzheimeru', 3, 2018, 250), 
(978808660649,'Jak žít a nezbláznit se', 4, 2006, 150),
(9788076960145, 'Nesmyslnost: Jak je možné, že racionálně uvažující lidé uvěří neracionálním „pravdám“?', 1, 2024, 249)

INSERT INTO authors (id,first_name,last_name,country)
VALUES
(1, 'Dan', 'Ariely', 'USA'),
(2,'Ilona', 'Švihlíková', 'Česká republika'),
(3,'Dale', 'Bredesen','USA')

SELECT * FROM books WHERE published_year > 2010

SELECT * FROM books ORDER BY price

SELECT title, authors.first_name, authors.last_name FROM books INNER JOIN authors ON books.author_id = authors.id 