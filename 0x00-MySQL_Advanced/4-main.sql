-- Add 5 orders
SELECT * FROM items;
SELECT * FROM orders;

SELECT "--";

INSERT INTO orders (item_name, number) VALUES ('item 1', 2);
INSERT INTO orders (item_name, number) VALUES ('item 0', 1);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;

SELECT "--";

INSERT INTO orders (item_name, number) VALUES ('item 3', 5);
INSERT INTO orders (item_name, number) VALUES ('item 2', 7);
INSERT INTO orders (item_name, number) VALUES ('item 0', 2);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;