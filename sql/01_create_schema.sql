CREATE SCHEMA IF NOT EXISTS lab;

DROP TABLE IF EXISTS lab.customers CASCADE;

CREATE TABLE lab.customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    city VARCHAR(100),
    signup_date DATE NOT NULL,
    customer_segment VARCHAR(50) NOT NULL,
    CONSTRAINT ck_segment_valid CHECK (customer_segment IN ('Retail', 'Professional', 'SME', 'Student'))
);