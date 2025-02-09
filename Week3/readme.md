# Data Warehouse & BigQuery

- [Slide](https://docs.google.com/presentation/d/1a3ZoBAXFk8-EhUsd7rAZd-5p_HpltkzSeujjRGB2TAI/edit#slide=id.p)

## 3.1.1 - Data Warehouse and BigQuery

### OLAP vs OLTP

- OLTP - Online Transaction Processing
    - Mainly for backend services, when there is a need to combine multiple SQL queries and the need to undo any of the changes if they fail
    - Quick update but the data size is small
    - Normalised database design for efficiency
    - Enhanced productivity for end users
    - User example - customer-facing personnel, clerks, online shoppers
- OLAP - Online Analytical Processing
    - Mainly used to store large amounts of data & find hidden insights and commonly used by Data Analysts & Scientists for their analytical tasks
    - Data is refreshed at an interval, the size of the data is much larger than OLTP
    - Denormalised database design
    - Enhanced productivity for Data Analysts & Executives
    - User Example - Data Analysts, Business Analysts & Executives

### Data Warehouse (DW)

- A comprehensive solutions of OLAP for reporting & data analysis.
- Typically comprises of raw data, metadata & summary information
- Can also contains various data sources, such as operating system & flat science system, or maybe an OLTP database
- All of these send their reports to a staging area where it then is used to write the output to a data warehouse.
- DW can be converted into data maps
    - Various users can access the data directly through there data maps.
    - For analysts, using data maps as an interface would be an optimal scenario, but may vary depending on the use case
    - Data Scientists can benefit from it to directly to examine raw data from DW, regardless of whether DW offer access to raw data, summary data or data maps

### BigQuery (BQ)

- Is a DW solution
- Serverless, no need to manage servers or install DB software
- Offer both software & infrastructure that prioritise scalability & high availability
- Can work with a few GB of data & effortlessly scale up to PB with no problem
- Also had Machine Learning, handling geospatial data & conducting business intelligence queries
- Flexibility in storing data
- Usually when the data size grows, we need to expand the machine's storage & compute capabilities
- BQ helps this with separating the compute engine & analysing data on a separate storage platform & is highly advantageous in terms of cost.

**BigQuery Interface**

![BQ Interface](/ss/w3/Screenshot%202025-02-09%20223759.png)

- ```taxi_rides_ny``` is the project, ```nytaxi``` is the dataset, ```external_yellow_tripdata``` is the table

**BQ Costs**
- 2 types of pricing
    - On demand pricing is at 5 usd per 1TB of data processed
    - Flat rate pricing, which is based on the number of pre requested slots at 100 slots for 2000usd/ month


**Table Partitioning**

![Table Partition](/ss/w3/Screenshot%202025-02-09%20225429.png)

- Partition table is divided into partitions, which is this case the raw data on the left side is partitioned based on the ```creation_date``` column, which makes it easier to manage & query the data.

- By dividing the large data into smaller chunks of partition based on the column that we desired, performance can be improved as well as its control costs by reducing the byte numbers read when querying the data.

**Clustering**

![Clustering](/ss/w3/Screenshot%202025-02-09%20230522.png)

- Clustering is another method where we want to further optimising the performance the query & reducing the costs by organizing the data in a table based on the values of the column names.

- In this case, clustering is sorting the data based on the ```tags``` column
- note that clustering can work on top of the partitions

## 3.1.2 - Partitioning and Clustering

**Partition**
- When partition, these are the options when creating a partitioned table,
- Time unit column,
- Ingestion time,
- Integer range partition

## 3.2.1 - BigQuery Best Practices

## 3.2.2 - Internals of Big Query