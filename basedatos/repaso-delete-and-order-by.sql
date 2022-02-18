# Repaso

# SELECT 
# INSERT 
# UPDATE

# WHERE
# LIKE - NOT - OR - AND
# BETWEEN

use w3schools;

-- Select * FROM Customers where Country = "Peru";

-- Select * from Customers where ContactName LIKE '%ed%';

-- select * from Products  where Price between 10 AND 25;

-- select *  FROM Products LIMIT 5;

-- INSERT INTO customers (CustomerName, ContactName, Address, City, PostalCode, Country)
-- VALUES ('Juaquin', 'Ozuna', 'Jr Las Gardenias', 'Lima', '15003', 'Peru');

-- UPDATE Customers set ContactName = 'Osuna Del Rio' where CustomerID=94;

Select * FROM Customers  ;

# DELETE

DELETE FROM Customers WHERE CustomerID IN (93, 94);

select count(*) from Customers;

# order by

Select * FROM Customers  ORDER BY Country; # ASC | DESC
Select * FROM Customers  ORDER BY CustomerID DESC;

















