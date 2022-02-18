
USE w3schools;


# select
# insert
# delete
# update

SELECT * FROM customers;

-- SELECT CustomerName, City, ContactName
-- FROM customers;

-- INSERT INTO customers (CustomerName, ContactName, Address, City, PostalCode, Country)
-- VALUES ('Cardinal', "TOM B.", "Skagen 21", 'Stavanger', '4006', 'Norway');


# SELECT WHERE

-- SELECT * FROM customers WHERE Country = 'Mexico'; -- where mexico
-- SELECT * FROM customers WHERE Country = 'Argentina'; -- Where 

-- SELECT * FROM customers WHERE City = 'Berlin';
-- SELECT * FROM customers WHERE Country = 'Mexico' OR  Country = 'Argentina';

-- SELECT * FROM customers WHERE NOT Country = 'Mexico';
-- SELECT * FROM customers WHERE Country != 'Mexico';

-- SELECT * FROM customers WHERE CustomerID = 51;


# SELECT WHERE LIKE

SELECT * FROM customers 
WHERE CustomerName LIKE '%a%';
-- ANA  SI
-- JUAN NO
 
 
# where between
-- SELECT * FROM products;

-- select * from products 
-- where Price 
-- between 10 and 20;

# UPDATE
SELECT * FROM customers;

update customers 
set CustomerName = 'Maria'
where CustomerId = 92;

 

