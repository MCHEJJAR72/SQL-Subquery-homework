1. Get all payments above $6.99 with the Customer's Full Name
sql
SELECT c.first_name, c.last_name, p.amount
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
WHERE p.amount > 6.99;
2. Show all customers names who have made payments over $175 (use subqueries)
sql
SELECT first_name, last_name
FROM customer
WHERE customer_id IN (SELECT customer_id FROM payment
    GROUP BY customer_id
    HAVING SUM(amount) > 175);
3. Which staff member had the most transactions?
sql
SELECT staff_id, COUNT(*) AS transaction_count
FROM payment
GROUP BY staff_id
ORDER BY transaction_count DESC
LIMIT 1;
4. Show all customers who have made a single payment above $6.99 (Use Subqueries)
sql
SELECT c.first_name, c.last_name, p.amount
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
WHERE p.amount > 6.99
AND p.customer_id IN (SELECT customer_id FROM payment
    GROUP BY customer_id
    HAVING COUNT(*) = 1);

List all customers who live in Texas (using JOINs)
Since the customer table schema does not include a specific state column (customer_state seems to represent this), and based on the sample data provided, we'll need to filter based on the customer_state column. However, there are no customers listed as living in Texas (TX) based on the provided data.

Here's how you would typically query for customers in Texas if the data were available:
FROM customer
WHERE customer_state = 'TX';
List all customers that live in Nepal (using the city table)
To find customers living in Nepal, we'll need to join the customer table with the address and city tables, and then filter based on the country name (Nepal).

Here's how you would construct this query:
SELECT c.*
FROM customer c
JOIN address a ON c.address = a.address
JOIN city ci ON a.city = ci.city
JOIN country co ON ci.country_id = co.country_id
WHERE co.country = 'Nepal';