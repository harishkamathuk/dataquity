-- 
-- File: dataquity.sql
-- Description: This SQL file contains the definition and creation of the 'stocks' table.
-- Author: harishkamathuk
-- Date: 2025/01/17
--

-- 
-- Table: stocks
-- Description: This table stores information about stocks.
CREATE TABLE IF NOT EXISTS stocks (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    company_name VARCHAR(255),
    price NUMERIC,
    volume INTEGER,
    market_cap NUMERIC,
    percentage_change FLOAT,
    daily_price_range FLOAT,
    fiftytwo_week_range FLOAT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM stocks;

ALTER TABLE stocks
ADD COLUMN percentage_change FLOAT,
ADD COLUMN daily_price_range FLOAT,
ADD COLUMN fiftytwo_week_range FLOAT;


