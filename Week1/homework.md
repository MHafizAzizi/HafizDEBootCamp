Q1

docker pull python:3.12.8

docker run -it --entrypoint=bash python:3.12.8

pip --version

ANSWER = 24.3.1

Q2

ANSWER = db:5432

Q3

```SQL

WITH trip_categories AS (
    SELECT 
        CASE 
            WHEN trip_distance <= 1 THEN '0-1 miles'
            WHEN trip_distance > 1 AND trip_distance <= 3 THEN '1-3 miles'
            WHEN trip_distance > 3 AND trip_distance <= 7 THEN '3-7 miles'
            WHEN trip_distance > 7 AND trip_distance <= 10 THEN '7-10 miles'
            ELSE 'Over 10 miles'
        END AS distance_category,
        COUNT(*) AS trip_count
    FROM green_trip
    WHERE 
        lpep_pickup_datetime >= '2019-10-01' 
        AND lpep_pickup_datetime < '2019-11-01'
    GROUP BY 
        CASE 
            WHEN trip_distance <= 1 THEN '0-1 miles'
            WHEN trip_distance > 1 AND trip_distance <= 3 THEN '1-3 miles'
            WHEN trip_distance > 3 AND trip_distance <= 7 THEN '3-7 miles'
            WHEN trip_distance > 7 AND trip_distance <= 10 THEN '7-10 miles'
            ELSE 'Over 10 miles'
        END
)
SELECT 
    string_agg(trip_count::text, ';' ORDER BY 
        CASE distance_category
            WHEN '0-1 miles' THEN 1
            WHEN '1-3 miles' THEN 2
            WHEN '3-7 miles' THEN 3
            WHEN '7-10 miles' THEN 4
            ELSE 5
        END
    ) AS result
FROM trip_categories;

```
ANSWER = 104830;198995;109642;27686;35201

Q4

```SQL
SELECT DATE(lpep_pickup_datetime) AS pickup_day,
       MAX(trip_distance) AS longest_distance
FROM green_trip
GROUP BY pickup_day
ORDER BY longest_distance DESC
LIMIT 1;
```
ANSWER = 2019-10-31

Q5

```SQL
SELECT 
    taxi_zone."Zone" AS pickup_zone,
    SUM(green_trip."total_amount") AS total_amount
FROM green_trip
INNER JOIN taxi_zone ON green_trip."PULocationID" = taxi_zone."LocationID"
WHERE green_trip."lpep_pickup_datetime"::date = '2019-10-18'
GROUP BY taxi_zone."Zone"
HAVING SUM(green_trip."total_amount") > 13000
ORDER BY total_amount DESC;
```

ANSWER = East Harlem North, East Harlem South, Morningside Heights

Q6

```SQL
SELECT 
    drop_off_zone."Zone" AS dropoff_zone,
    MAX(green_trip."tip_amount") AS max_tip
FROM green_trip
JOIN taxi_zone AS pickup_zone ON green_trip."PULocationID" = pickup_zone."LocationID"
JOIN taxi_zone AS drop_off_zone ON green_trip."DOLocationID" = drop_off_zone."LocationID"
WHERE 
    pickup_zone."Zone" = 'East Harlem North' AND
    green_trip."lpep_pickup_datetime" BETWEEN '2019-10-01' AND '2019-10-31'
GROUP BY drop_off_zone."Zone"
ORDER BY max_tip DESC
LIMIT 1;
```

ANSWER = JFK AIRPORT

Q7 

terraform init, terraform plan -auto-apply, terraform rm
