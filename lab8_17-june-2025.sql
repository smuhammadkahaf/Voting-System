use sakila;

select * from actor;

# task 1
CREATE VIEW actor_names AS
SELECT first_name, last_name
FROM actor;
select * from actor_names;

-- task 2
CREATE VIEW customer_contact_info AS
SELECT 
    c.first_name,
    c.last_name,
    a.address,
    a.phone
FROM customer c
JOIN address a ON c.address_id = a.address_id;
select * from customer_contact_info;

-- task 3
CREATE VIEW store_location_info AS
SELECT 
    s.store_id,
    ci.city,
    co.country
FROM store s
INNER JOIN address a ON s.address_id = a.address_id
INNER JOIN city ci ON a.city_id = ci.city_id
INNER JOIN country co ON ci.country_id = co.country_id;
select * from store_location_info;
-- task 4
CREATE VIEW film_titles_and_ratings AS
SELECT title, rating
FROM film;
select * from film_titles_and_ratings;

-- task 5
CREATE VIEW customer_rental_history AS
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    f.title,
    r.rental_date,
    r.return_date
FROM customer c
INNER JOIN rental r ON c.customer_id = r.customer_id
INNER JOIN inventory i ON r.inventory_id = i.inventory_id
INNER JOIN film f ON i.film_id = f.film_id;
SELECT * FROM customer_rental_history;

-- task 6
CREATE VIEW staff_store_info AS
SELECT 
    s.staff_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    st.store_id,
    a.address
FROM staff s
INNER JOIN store st ON s.store_id = st.store_id
INNER JOIN address a ON st.address_id = a.address_id;
SELECT *from staff_store_info;

-- task 7
CREATE VIEW films_in_store AS
SELECT DISTINCT
    i.store_id,
    f.film_id,
    f.title
FROM inventory i
INNER JOIN film f ON i.film_id = f.film_id;
SELECT * FROM films_in_store;

-- task 8
CREATE VIEW customer_total_payments AS
SELECT 
    customer_id,
    SUM(amount) AS total_paid
FROM payment
GROUP BY customer_id;
select * from customer_total_payments;

-- task 9
CREATE VIEW top_five_rented_films AS
SELECT 
    f.film_id,
    f.title,
    COUNT(r.rental_id) AS rental_count
FROM rental r
INNER JOIN inventory i ON r.inventory_id = i.inventory_id
INNER JOIN film f ON i.film_id = f.film_id
GROUP BY f.film_id, f.title
ORDER BY rental_count DESC
LIMIT 5;
SELECT * FROM top_five_rented_films;

-- TASK 10
CREATE VIEW action_films AS
SELECT 
    f.film_id,
    f.title
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action';
SELECT * FROM action_films;