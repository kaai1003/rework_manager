-- Active: 1736716074336@@127.0.0.1@5432@rework_db
CREATE TABLE users (
    id VARCHAR PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    usercard VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    role VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reference (
    id VARCHAR PRIMARY KEY,
    ref VARCHAR NOT NULL,
	project VARCHAR NOT NULL,
	famille VARCHAR NOT NULL,
    car_type VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    id VARCHAR PRIMARY KEY,
	project VARCHAR NOT NULL,
	famille VARCHAR NOT NULL,
    car_type VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lines (
    id VARCHAR PRIMARY KEY,
	project VARCHAR NOT NULL,
	famille VARCHAR NOT NULL,
    line INT NOT NULL,
    car_type VARCHAR NOT NULL,
    superviseur VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE failures (
    id VARCHAR PRIMARY KEY,
	failure VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE process (
    id VARCHAR PRIMARY KEY,
	process VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reworktables (
    id VARCHAR PRIMARY KEY,
	nr_table INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reworkers (
    id VARCHAR PRIMARY KEY,
	name VARCHAR NOT NULL,
    matricule VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reworkdetails (
    id VARCHAR PRIMARY KEY,
    usercard VARCHAR NOT NULL,
    ref VARCHAR NOT NULL,
	project VARCHAR NOT NULL,
	famille VARCHAR NOT NULL,
    car_type VARCHAR NOT NULL,
    line INT NOT NULL,
    superviseur VARCHAR NOT NULL,
    prod_date TIMESTAMP NOT NULL,
    reworkcard VARCHAR NOT NULL,
    reworkfailure VARCHAR NOT NULL,
    failuredetails VARCHAR NOT NULL,
    processfailure VARCHAR NOT NULL,
    reworktable INT NOT NULL,
    reworker VARCHAR NOT NULL,
    quality VARCHAR DEFAULT NULL,
    status VARCHAR NOT NULL,
    reworkduration FLOAT DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);