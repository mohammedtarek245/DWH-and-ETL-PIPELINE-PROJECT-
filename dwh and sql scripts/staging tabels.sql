CREATE TABLE staging_sales (
    index TEXT,
    Order_ID TEXT,
    Date timesatmp,
    Status varchar(200),
    Fulfilment  varchar(200),
    Sales_Channel varchar(200),
    SKU varchar(200),
    Category varchar(200),
    Size varchar(200),
    ASIN varchar(200),
    Qty int,
    Currency varchar(200),
    Amount numeric
);

CREATE TABLE staging_delivery (
    Order_ID varchar(200),
    Agent_Age int ,
    Agent_Rating numeric,
    Order_Date date,
    Order_Time TEXT,
    Area varchar(200),
    Category  varchar(200)
);

CREATE TABLE staging_behavior (
    Timestamp Timestamp,
    Age int ,
    Gender varchar(200),
    Purchase_Frequency varchar(200),
    Purchase_Categories varchar(200),
    Browsing_Frequency varchar(200),
    Product_Search_Method varchar(200),
    Personalized_Recommendation_Frequency  varchar(200),
    Rating_Accuracy TEXT
);

