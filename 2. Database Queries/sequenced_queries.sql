-- section 1
CREATE DATABASE vosys;
use vosys;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cnic VARCHAR(13) NOT NULL,
    date_of_birth DATE NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(254) UNIQUE,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    photo_url TEXT
);

CREATE TABLE categories (
	-- this table record all the categoris
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE
);

create table Person_Categories (
	id INT AUTO_INCREMENT PRIMARY KEY,
    user_id int not null,
    category_id int not null,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    unique (user_id,category_id)
);

CREATE TABLE Elections (
	election_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description varchar(1000) NOT null,
    register_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    starting_date DATETIME not null, -- 'YYYY-MM-DD HH:MM:SS'
    ending_date DATETIME not null, -- 'YYYY-MM-DD HH:MM:SS'
    election_status varchar(15) not null -- (upcoming, ongoing, ended)
);

create table Elections_Categories ( 
-- this table create relation between election and category. eache election can be set for UNIQUE categories
	id INT AUTO_INCREMENT PRIMARY KEY,
    election_id int not null,
    category_id int not null,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (election_id) REFERENCES Elections(election_id),
    UNIQUE (election_id,category_id)
);

create table Election_candidates (
	Candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id int not null,
    election_id int not null,
    affiliations varchar (100) not null,
    FOREIGN KEY (election_id) REFERENCES Elections(election_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    UNIQUE (user_id, election_id)
);

create table votes(
	vote_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id int not null,
	election_id int not null,
    vote_time DATETIME DEFAULT CURRENT_TIMESTAMP not null,
	FOREIGN KEY (election_id) REFERENCES Elections(election_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    UNIQUE (user_id,election_id)
);

create table Candidate_votes (
	Candidate_vote_id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_id int not null,
    FOREIGN KEY (candidate_id) REFERENCES Election_candidates(Candidate_id),
    vote_time DATETIME DEFAULT CURRENT_TIMESTAMP not null
);


-- section 2
alter table Candidate_votes
add column election_id int not null;

alter table Candidate_votes
add FOREIGN KEY (election_id) REFERENCES Elections(election_id);



CREATE table admins(
	admin_id INT AUTO_INCREMENT PRIMARY KEY,
    Name varchar(100) not null,
    username varchar(100) not null unique,
    password varchar(255) COLLATE utf8mb4_bin not null, -- COLLATE defines how text is compared and sorted in MySQL.
    status varchar(50) default "Active" not null
);

insert into admins(name,username,password)
values
("test","user034","LetmeIn");

select * from admins
where
username ="user034" and 
password = "LetmeIn";
DELETE FROM admins WHERE admin_id = "5";

select * from admins where username  = "user034";
select * from admins ;

update admins 
set status = "Active"
where admin_id =4;

INSERT INTO admins (name,username , password , admin_id) VALUES ( 'kahaf' ,'kahaf',  '123' ,  '1');

-- section 3
ALTER TABLE users RENAME COLUMN user_id TO id;
ALTER TABLE categories RENAME COLUMN category_id TO id;
ALTER TABLE Elections RENAME COLUMN election_id TO id;
ALTER TABLE Election_candidates RENAME COLUMN Candidate_id TO id;
ALTER TABLE votes RENAME COLUMN vote_id TO id;
ALTER TABLE Candidate_votes RENAME COLUMN Candidate_vote_id TO id;
ALTER TABLE admins RENAME COLUMN admin_id TO id;

select * from categories;

-- section 4
select * from users; 
ALTER TABLE users ADD CONSTRAINT unique_cnic UNIQUE (cnic);
ALTER TABLE users ADD UNIQUE(cnic);
alter table users drop column photo_url;

-- section 5
select * from users;
delete from users where id = 10;
select	*from Person_Categories;
insert into users(name,cnic,date_of_birth)
values
("ali",("123"),("2005-06-11"));



-- section 6
SELECT u.id AS id, u.name AS NAME, u.cnic as CNIC, COUNT(pc.category_id) AS number_in_categories
FROM users u
LEFT JOIN person_categories pc ON u.id = pc.user_id
GROUP BY u.id, u.name, u.cnic;

select category_name from categories
where id in ( 
select category_id from person_categories where user_id = 7);

delete from users;
ALTER TABLE users ADD COLUMN key_ VARCHAR(32) NOT NULL;
select * from users;


SELECT u.id AS id, u.name AS NAME, u.cnic as CNIC,Group_CONCAT(c.category_name) AS categories
FROM users u
LEFT JOIN person_categories pc ON u.id = pc.user_id
RIGHT JOIN categories c on pc.category_id = c.id
GROUP BY u.id, u.name, u.cnic;
-- section 7

select * from elections;
select * from elections_categories;
ALTER TABLE elections MODIFY COLUMN election_status INT;

DELETE FROM ELECTIONS;

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
ALTER TABLE Elections
MODIFY COLUMN election_status INT NOT NULL DEFAULT 0;
select category_name from categories where id in (select category_id from Elections_Categories where election_id =5);

update elections 
set election_status =0;

-- section 8 
use vosys;
SELECT * FROM Election_candidates;

select ec.id , u.name, u.cnic,ec.affiliations from users u
inner join Election_candidates ec
on u.id = ec.user_id
where ec.election_id = 4;


SELECT * FROM Election_candidates where election_id = 7;

#section 9
CREATE USER 'vosys_user'@'192.168.148.52' IDENTIFIED WITH mysql_native_password BY '12345';
GRANT ALL PRIVILEGES ON vosys.* TO 'vosys_user'@'192.168.148.52';
FLUSH PRIVILEGES;
DROP USER 'vosys_user'@'192.168.148.52';


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







# section 10
use vosys;
ALTER TABLE Elections 
ADD COLUMN display_id VARCHAR (15) UNIQUE;

delete from elections;
delete from election_candidates;
DELETE from elections_categories;

Select * from elections;

SELECT * FROM candidate_votes;
SELECT * FROM votes;


