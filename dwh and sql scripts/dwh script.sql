CREATE TABLE DIM_SALES (
    order_id text PRIMARY KEY,
    status varchar(200) ,
    sales_channel varchar(200),
    sku varchar(200),
    category varchar(200),
    qty int,
    currency varchar(200),
    paid_amount numeric
);

INSERT INTO DIM_SALES (order_id, status, sales_channel, sku, category ,qty , currency , paid_amount)
SELECT order_id, status, sales_channel, sku, category ,qty , currency , paid_amount
FROM staging_sales
ON CONFLICT (order_id) DO NOTHING;


CREATE TABLE DIM_BEHAVIOR (
    customer_age int PRIMARY KEY,
    gender varchar(50),
    purchase_frequency varchar(500),
    browsing_frequency varchar(500),
    product_search_method varchar(500),
    rating_accuracy text
);


INSERT INTO DIM_BEHAVIOR (age ,
    gender ,
    purchase_frequency ,
    browsing_frequency ,
    product_search_method ,
    rating_accuracy )
SELECT age ,
    gender ,
    purchase_frequency ,
    browsing_frequency ,
    product_search_method ,
    rating_accuracy
FROM staging_behavior
ON CONFLICT (age) DO NOTHING;

select * from dim_behavior


CREATE TABLE DIM_DELIVERY (
    delivery_id text PRIMARY KEY,
    agent_age int,
    agent_rating numeric ,
    area varchar(200)
);


INSERT INTO DIM_DELIVERY (
    id ,
    agent_age ,
    agent_rating ,
    area )
SELECT id ,
    agent_age ,
    agent_rating ,
    area 
FROM staging_delivery

select * from DIM_DELIVERY ;


CREATE TABLE fact_table (
  sales_index text PRIMARY KEY,
    order_id text REFERENCES DIM_SALES(order_id),
    sales_date text,
    id text REFERENCES DIM_DELIVERY(id),
    age int REFERENCES DIM_BEHAVIOR(age)
 );


--columns names are the same from the raw tables to the staging tables while inserting data
--making data type of columns in staging tables and dim and act tables the same would make insertion of data more smooth

INSERT INTO fact_table (
  sales_index,
  order_id,
  sales_date,
  id,
  age
)
-- Replace NULL with 'NA' (or adjust the value as needed)
SELECT 
  COALESCE(staging_sales.sales_index, 'NA'),  
  staging_sales.order_id,
  staging_sales.sales_date,
  staging_delivery.order_id,
  staging_behavior.age
FROM staging_sales 
FULL OUTER JOIN staging_delivery 
  ON staging_sales.order_id = staging_delivery.order_id
FULL OUTER JOIN staging_behavior 
  ON staging_sales.category = staging_behavior.category
-- Ensure no duplicate insertions based on primary key (if necessary)
WHERE staging_sales.sales_index IS NOT NULL
ON CONFLICT (sales_index) DO NOTHING;


SELECT * FROM fact_table


---creating average and sum columns for nermuical values for visulation on BI






