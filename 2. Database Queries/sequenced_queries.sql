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
DELETE FROM categories;

-- section 4
select * from users; 
ALTER TABLE users ADD CONSTRAINT unique_cnic UNIQUE (cnic);
ALTER TABLE users ADD UNIQUE(cnic);
alter table users drop column photo_url;

-- section 5
select * from users;
select	*from Person_Categories;
insert into users(name,cnic,date_of_birth)
values
("ali",("123"),("2005-06-11"));
delete from users;



-- section 6
SELECT u.id AS id, u.name AS NAME, u.cnic as CNIC, COUNT(pc.category_id) AS number_in_categories
FROM users u
LEFT JOIN person_categories pc ON u.id = pc.user_id
GROUP BY u.id, u.name, u.cnic;
