BEGIN TRANSACTION;
CREATE TABLE tasks (
	id INTEGER NOT NULL, 
	create_date DATETIME, 
	task_name VARCHAR(80), 
	task_description VARCHAR(240), 
	task_criteria VARCHAR(120), 
	status INTEGER, 
	customer_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(customer_id) REFERENCES customers (id)
);
INSERT INTO `tasks` (id,create_date,task_name,task_description,task_criteria,status,customer_id) VALUES (1,'2015-12-18 00:00:00.000000','app survey','survey of the slydepay app','english,tech survey','active',1),
 (2,'2015-12-18 00:00:00.000000','some other survey','survey of the slydepay app','english,tech survey','active',1),
 (3,'2015-12-18 00:00:00.000000','app survey','survey of the slydepay app','english,tech survey','active',3);
CREATE TABLE forms (
	id INTEGER NOT NULL, 
	label VARCHAR(120), 
	value TEXT, 
	ftype TEXT, 
	condition TEXT, 
	require TEXT, 
	task_id INTEGER, 
	create_date DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(task_id) REFERENCES tasks (id)
);
INSERT INTO `forms` (id,label,value,ftype,condition,require,task_id,create_date) VALUES (1,'do you like the background?','yes','testfield','','',1,'2015-12-18 00:00:00.000000'),
 (2,'is the sidebar too big?','yes','testfield','','',1,'2015-12-18 00:00:00.000000'),
 (3,'do you like the background?','yes','testfield','','',2,'2015-12-18 00:00:00.000000'),
 (4,'is the sidebar too big?','yes','testfield','','',2,'2015-12-18 00:00:00.000000'),
 (5,'do you like the background?','yes','testfield','','',3,'2015-12-18 00:00:00.000000'),
 (6,'is the sidebar too big?','yes','testfield','','',3,'2015-12-18 00:00:00.000000');
CREATE TABLE customers (
	id INTEGER NOT NULL, 
	create_date DATETIME, 
	first_name VARCHAR(80), 
	last_name VARCHAR(80), 
	email VARCHAR(120), 
	password VARCHAR(400), 
	PRIMARY KEY (id)
);
INSERT INTO `customers` (id,create_date,first_name,last_name,email,password) VALUES (1,'2015-12-18 00:00:00.000000','edmond','mensah','primerossgh@gmail.com','password'),
 (2,'2015-12-18 00:00:00.000000','edmond','mensah','primerossgh@gmail.com','password'),
 (3,'2015-12-18 00:00:00.000000','edmond','mensah','primerossgh@gmail.com','password');
CREATE TABLE contributors (
	id INTEGER NOT NULL, 
	first_name VARCHAR(80), 
	last_name VARCHAR(80), 
	email VARCHAR(120), 
	password VARCHAR(120), 
	skill_rating TEXT, 
	create_date DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO `contributors` (id,first_name,last_name,email,password,skill_rating,create_date) VALUES (1,'charles','andor','kwasiamantin@gmail.com','password',NULL,NULL),
 (2,'charles','andor','kwasiamantin@gmail.com','password',NULL,NULL),
 (3,'charles','andor','kwasiamantin@gmail.com','password',NULL,NULL);
CREATE TABLE contributor_task (
	id INTEGER NOT NULL, 
	customer_id INTEGER, 
	task_id INTEGER, 
	contributor_id INTEGER, 
	create_date DATETIME, 
	status VARCHAR(8), 
	PRIMARY KEY (id), 
	FOREIGN KEY(contributor_id) REFERENCES contributors (id)
);
INSERT INTO `contributor_task` (id,customer_id,task_id,contributor_id,create_date,status) VALUES (1,1,1,1,'2015-12-18 00:00:00.000000','active'),
 (2,2,2,2,'2015-12-18 00:00:00.000000','active'),
 (3,3,3,3,'2015-12-18 00:00:00.000000','active');
COMMIT;
