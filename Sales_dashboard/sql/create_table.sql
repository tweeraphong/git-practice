CREATE DATABASE IF NOT EXISTS sales_db;

USE sales_db;

CREATE TABLE IF NOT EXISTS sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    product VARCHAR(50),
    region VARCHAR(50),
    quantity INT,
    price INT,
    revenue FLOAT
);