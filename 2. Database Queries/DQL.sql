select * from admins ;
select * from users; 
select	*from Person_Categories;
select * from elections;
select * from elections_categories;
SELECT * FROM Election_candidates;
select * from email_config;
SELECT * FROM candidate_votes;
SELECT * FROM votes;
SELECT * from categories;


-- This query fetches admin details where the username is "user034" and the password matches exactly (case-sensitive).
select * from admins
where
username ="user034" and 
password = "LetmeIn";

select * from admins where username  = "user034";


-- This query retrieves each user's ID, name, CNIC, and the total number of categories they belong to.
SELECT u.id AS id, u.name AS NAME, u.cnic as CNIC, COUNT(pc.category_id) AS number_in_categories
FROM users u
LEFT JOIN person_categories pc ON u.id = pc.user_id
GROUP BY u.id, u.name, u.cnic;



-- This query retrieves the names of all categories that user with ID 7 is assigned to.
select category_name from categories
where id in ( 
select category_id from person_categories where user_id = 7);


-- This query lists each user's ID, name, CNIC, and a comma-separated list of category names they belong to.
SELECT u.id AS id, u.name AS NAME, u.cnic as CNIC,Group_CONCAT(c.category_name) AS categories
FROM users u
LEFT JOIN person_categories pc ON u.id = pc.user_id
RIGHT JOIN categories c on pc.category_id = c.id
GROUP BY u.id, u.name, u.cnic;


-- This query fetches each election’s ID, title, start and end dates, along with the total number of categories assigned to it.
SELECT 
    e.id AS id, 
    e.title AS Title, 
    e.starting_date AS Start_Date, 
    e.ending_date AS End_Date, 
    COUNT(ec.category_id) AS number_in_categories
FROM elections e
LEFT JOIN elections_categories ec ON e.id = ec.election_id
GROUP BY e.id;



SELECT title,description,starting_date,ending_date from elections;

--  This query retrieves the names of all categories linked to the election with ID 5.
select category_name from categories where id in (select category_id from Elections_Categories where election_id =5);


-- This query returns the ID, name, CNIC, and affiliations of all candidates participating in the election with ID 4.
select ec.id , u.name, u.cnic,ec.affiliations from users u
inner join Election_candidates ec
on u.id = ec.user_id
where ec.election_id = 4;


SELECT * FROM Election_candidates where election_id = 7;

-- A combined list of all ongoing elections for user 13, indicating whether they have voted or not, even accounting for category changes.
SELECT e.display_id AS election_id, e.title, e.starting_date, e.ending_date,CASE WHEN v.user_id IS NOT NULL THEN 'Voted' ELSE 'Not Voted' END AS status FROM elections e
INNER JOIN elections_categories ec ON e.id = ec.election_id INNER JOIN person_categories pc ON ec.category_id = pc.category_id AND pc.user_id = 13
LEFT JOIN votes v ON v.election_id = e.id AND v.user_id = 13
WHERE e.election_status = 1
GROUP BY e.display_id, e.title, e.starting_date, e.ending_date, v.user_id
UNION
-- Part 2: Ongoing elections the user has voted in, even if not in the category anymore
SELECT e.display_id AS id, e.title, e.starting_date, e.ending_date,'Voted' AS status FROM elections e
INNER JOIN votes v ON e.id = v.election_id AND v.user_id = 13
WHERE e.election_status = 1;


select * from elections;

show tables;


-- This query retrieves all elections with their display ID, title, start and end dates,
-- and a human-readable status label based on the election_status code, ordered by the most recently registered first.
SELECT 
    e.display_id AS id,
    e.title AS Title,
    e.starting_date AS Start_Date,
    e.ending_date AS End_Date,
    CASE 
        WHEN e.election_status = 0 THEN 'Not Launched'
        WHEN e.election_status = 1 THEN 'On Going'
        WHEN e.election_status = 2 THEN 'Paused'
        WHEN e.election_status = 3 THEN 'Ended'
        ELSE 'Unknown'
    END AS Status
FROM elections e
ORDER BY e.register_date DESC;

-- These queries fetch details of election 'kod-17' and list its candidates with their vote counts in descending order.
SELECT * FROM elections where display_id = 'kod-17';
SELECT 
    ec.id AS candidate_id,
    u.name AS candidate_name,
    ec.affiliations,
    COUNT(cv.id) AS total_votes
FROM election_candidates ec
INNER JOIN users u ON ec.user_id = u.id
LEFT JOIN candidate_votes cv ON ec.id = cv.candidate_id AND cv.election_id = ec.election_id
WHERE ec.election_id = 17
GROUP BY ec.id, u.name, ec.affiliations
ORDER BY total_votes DESC;


select count(*) as persons from users;
select count(*) as elections from elections;
select count(*) as categories from categories;
select count(*) as elections from elections where election_status = 1;
select count(*) as elections from elections where election_status = 2;



select sender_email,port,password from email_config;

