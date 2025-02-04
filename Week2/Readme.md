# Kestra

## 2.2.1 - Workflow Orchestration Introduction

Kestra
- All in One Automation & Orchestration Platform
    - ETL/ELT
    - API Orchestration
    - Scheduled & Event Driven Workflow
    - Batch Data Pipeline
    - Interactive Conditional Input
- Can be done with No Code, Low Code or Full Code
- Can be written in any programming language, versatility
- Monitoring all workflow & Executions

## 2.2.2 - Learn Kestra

### [2.2.2.1 Getting Started with Kestra](https://www.youtube.com/watch?v=a2BZ7vOihjg)

Running Kestra Using Docker

```docker
docker run --pull=always --rm -it -p 8080:8080 --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp kestra/kestra:latest server local
```

OR running the kestra & postgres database using the [docker compose](https://kestra.io/docs/installation/docker-compose)

```yaml
volumes:
  postgres-data:
    driver: local
  kestra-data:
    driver: local

services:
  postgres:
    image: postgres:latest
    volumes:
      - postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: kestra
      POSTGRES_USER: kestra
      POSTGRES_PASSWORD: k3str4
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGRES_USER}"]
      interval: 30s
      timeout: 10s
      retries: 10

  kestra:
    image: kestra/kestra:latest
    pull_policy: always
    # Note that this setup with a root user is intended for development purpose.
    # Our base image runs without root, but the Docker Compose implementation needs root to access the Docker socket
    # To run Kestra in a rootless mode in production, see: https://kestra.io/docs/installation/podman-compose
    user: "root"
    command: server standalone
    volumes:
      - kestra-data:/app/storage
      - /var/run/docker.sock:/var/run/docker.sock
      - /tmp/kestra-wd:/tmp/kestra-wd
    environment:
      KESTRA_CONFIGURATION: |
        datasources:
          postgres:
            url: jdbc:postgresql://postgres:5432/kestra
            driverClassName: org.postgresql.Driver
            username: kestra
            password: k3str4
        kestra:

          server:
            basicAuth:
              enabled: false
              username: "admin@kestra.io" # it must be a valid email address
              password: kestra
          repository:
            type: postgres
          storage:
            type: local
            local:
              basePath: "/app/storage"
          queue:
            type: postgres
          tutorial-flows:
            enabled: false
          tasks:
            tmpDir:
              path: /tmp/kestra-wd/tmp
          url: http://localhost:8080/
    ports:
      - "8080:8080"
      - "8081:8081"
    depends_on:
      postgres:
        condition: service_started
```

- Workflow known as Flows in Kestra
- Declared in YAML
- Works with any language

**Kestra Properties**
- ```id``` name of flow
- ```namespace``` environment for the flow
- ```tasks``` list of tasks to execute in your flow

**Input**
```yaml

inputs:
    - id: variable_name
      type: STRING
      defaults: example_string

{{ inputs.variable_name }}
```
**Output**
```{{ outputs.task_id.vars.output_name }}```

**Triggers**

```yaml
triggers:
    - id:hour_trigger
      type: io.kestra.core.models.triggers.types.Schedule
      cron: 0 * * *
```
### 2.2.2.2 Learn the Fundamentals of Kestra

```yaml

id: getting_started_video
namespace: dev

tasks:
  - id:hello_world
    type: io.kestra.core.tasks.log.Log
    message: Hello World!
```
3 Main Properties 
```id``` - unique identifier for the flow
```namespace``` - environment for the tasks to run in
```tasks``` - actions itll take place, had its own identifier
  - ```id```
  - ```type```
  - ```message```
  - ```description```

Other Properties

```description```
```labels```
  - ```owner```
  - ```project```


### 2.2.2.3 Pass Data Into Your Workflows with Inputs

- with using input, can simplify the workflow

```yaml
inputs:
  - id:user
    type: STRING
    defaults: Hafiz

tasks:
  - id:hello
    type: io.kestra.core.tasks.log.Log
    message: Hello there, {{ inputs.user }}
```
- when executed, itll ask for the user name, which indicated from the ```inputs``` and ```id:user```

## 2.2.3 - ETL Pipelines with Postgres in Kestra

[Dataset](https://github.com/DataTalksClub/nyc-tlc-data/releases)
- Main task to create a workflow to process the data each month and added into a table that combines it
- Workflow
  - Extract Data from the repo
  - load into a table in postgres db
  - combine into a main table
  - Transform the data, merge into a table

FLOW

```yaml
id: postgres_taxi
namespace: zoomcamp

inputs:
 - id: taxi
   type: SELECT
   displayName: Select the Taxi Type
   values: ['yellow','green']
   defaults: 'yellow'

 - id: year
   type: SELECT
   displayName: Select Year
   values: ['2019','2020']
   defaults: '2019'

 - id: month
   type: SELECT
   displayName: Select Month
   values: ['01','02', '03','04','05','06','07','08','09','10','11','12']
   defaults: '01'

variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"
  staging_table: "public.{{inputs.taxi}}_tripdata_staging"
  table: "public.{{inputs.taxi}}_tripdata"
  data: "{{outputs.extract.outputFiles[inputs.taxi ~ '_tripdata_' ~ inputs.year ~ '-' ~ inputs.month ~ '.csv'}}"

tasks:
  - id: set_label
    type: io.kestra.plugin.core.execution.Labels
    labels:
      file: "{{render(vars.file)}}"
      taxi: "{{inputs.taxi}}"

  - id: extract
    type: io.kestra.plugin.scripts.shell.Commands
    outputFiles:
      - "*.csv"
    taskRunner:
      type: io.kestra.plugin.core.runner.Process
    commands:
      - wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{{inputs.taxi}}/{{render(vars.file)}}.gz | gunzip > {{render(vars.file)}}
```


## 2.2.4 - Manage Scheduling and Backfills with Postgres in Kestra
## 2.2.5 - Orchestrate dbt Models with Postgres in Kestra

- Using dbt with Kestra for data transforming after extracting
- More details on dbt in week 4
- Quick glimpse on how cbt works in Kestra


## 2.2.6 - ETL Pipelines in Kestra Google Cloud Platform - Kestra

- Take the existing ETL pipeline & move to GCS & BigQuery
- ```06_gcp_taxi.yaml```
- in the current pipeline, extract data from csv file, instead of adding into postgres, we're upload csv into datalake or in this case the GCS bucket
- simple store the data in the cloud to be ready to use
- afterward, use BigQuery automatically use the csv file & create table from it 
- then can start the processing, cleaning data and start the queries 
- Requirement for the GCP BigQuery:
  - Service Account
  - GCP Project Id
  - GCP Location
  - GCP Bucket Name

```yaml
inputs:
  - id: taxi
    type: SELECT
    displayName: Select taxi type
    values: [yellow, green]
    defaults: green

  - id: year
    type: SELECT
    displayName: Select year
    values: ["2019", "2020"]
    defaults: "2019"
    allowCustomValue: true # allows you to type 2021 from the UI for the homework 🤗

  - id: month
    type: SELECT
    displayName: Select month
    values: ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    defaults: "01"
```
```inputs``` - basic input that we want to get when executing the flow

```yaml
variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"
  gcs_file: "gs://{{kv('GCP_BUCKET_NAME')}}/{{vars.file}}"
  table: "{{kv('GCP_DATASET')}}.{{inputs.taxi}}_tripdata_{{inputs.year}}_{{inputs.month}}"
  data: "{{outputs.extract.outputFiles[inputs.taxi ~ '_tripdata_' ~ inputs.year ~ '-' ~ inputs.month ~ '.csv']}}"
```
```variables``` - defining the variable of the flow

- for the Task section, first we need to set label and extract the data that we want to get,

```yaml
tasks:
  - id: set_label
    type: io.kestra.plugin.core.execution.Labels
    labels:
      file: "{{render(vars.file)}}"
      taxi: "{{inputs.taxi}}"

  - id: extract
    type: io.kestra.plugin.scripts.shell.Commands
    outputFiles:
      - "*.csv"
    taskRunner:
      type: io.kestra.plugin.core.runner.Process
    commands:
      - wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{{inputs.taxi}}/{{render(vars.file)}}.gz | gunzip
```
- then upload to our Bucket storage

```yaml
tasks:
  - id: upload_to_gcs
    type: io.kestra.plugin.gcp.gcs.Upload
    from: "{{render(vars.data)}}"
    to: "{{render(vars.gcs_file)}}"
```

```yaml
tasks:
  - id: bq_green_tripdata
    runIf: "{{inputs.taxi == 'green'}}"
    type: io.kestra.plugin.gcp.bigquery.Query
    sql: |
      CREATE TABLE IF NOT EXISTS `{{kv('GCP_PROJECT_ID')}}.{{kv('GCP_DATASET')}}.green_tripdata`
      (
          unique_row_id BYTES OPTIONS (description = 'A unique identifier for the trip, generated by hashing key trip attributes.'),
          filename STRING OPTIONS (description = 'The source filename from which the trip data was loaded.'),      
          VendorID STRING OPTIONS (description = 'A code indicating the LPEP provider that provided the record. 1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.'),
          lpep_pickup_datetime TIMESTAMP OPTIONS (description = 'The date and time when the meter was engaged'),
          lpep_dropoff_datetime TIMESTAMP OPTIONS (description = 'The date and time when the meter was disengaged'),
          store_and_fwd_flag STRING OPTIONS (description = 'This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka "store and forward," because the vehicle did not have a connection to the server. Y= store and forward trip N= not a store and forward trip'),
          RatecodeID STRING OPTIONS (description = 'The final rate code in effect at the end of the trip. 1= Standard rate 2=JFK 3=Newark 4=Nassau or Westchester 5=Negotiated fare 6=Group ride'),
          PULocationID STRING OPTIONS (description = 'TLC Taxi Zone in which the taximeter was engaged'),
          DOLocationID STRING OPTIONS (description = 'TLC Taxi Zone in which the taximeter was disengaged'),
          passenger_count INT64 OPTIONS (description = 'The number of passengers in the vehicle. This is a driver-entered value.'),
          trip_distance NUMERIC OPTIONS (description = 'The elapsed trip distance in miles reported by the taximeter.'),
          fare_amount NUMERIC OPTIONS (description = 'The time-and-distance fare calculated by the meter'),
          extra NUMERIC OPTIONS (description = 'Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges'),
          mta_tax NUMERIC OPTIONS (description = '$0.50 MTA tax that is automatically triggered based on the metered rate in use'),
          tip_amount NUMERIC OPTIONS (description = 'Tip amount. This field is automatically populated for credit card tips. Cash tips are not included.'),
          tolls_amount NUMERIC OPTIONS (description = 'Total amount of all tolls paid in trip.'),
          ehail_fee NUMERIC,
          improvement_surcharge NUMERIC OPTIONS (description = '$0.30 improvement surcharge assessed on hailed trips at the flag drop. The improvement surcharge began being levied in 2015.'),
          total_amount NUMERIC OPTIONS (description = 'The total amount charged to passengers. Does not include cash tips.'),
          payment_type INTEGER OPTIONS (description = 'A numeric code signifying how the passenger paid for the trip. 1= Credit card 2= Cash 3= No charge 4= Dispute 5= Unknown 6= Voided trip'),
          trip_type STRING OPTIONS (description = 'A code indicating whether the trip was a street-hail or a dispatch that is automatically assigned based on the metered rate in use but can be altered by the driver. 1= Street-hail 2= Dispatch'),
          congestion_surcharge NUMERIC OPTIONS (description = 'Congestion surcharge applied to trips in congested zones')
      )
      PARTITION BY DATE(lpep_pickup_datetime);
```
```bq_green_tripdata``` - this task will help create a main table for the green taxi with correct schema & partitioning for the uploaded csv files
- create a main table to merge all of the csv files together 

```yaml
tasks:
  - id: bq_green_table_ext
    runIf: "{{inputs.taxi == 'green'}}"
    type: io.kestra.plugin.gcp.bigquery.Query
    sql: |
      CREATE OR REPLACE EXTERNAL TABLE `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}_ext`
      (
          VendorID STRING OPTIONS (description = 'A code indicating the LPEP provider that provided the record. 1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.'),
          lpep_pickup_datetime TIMESTAMP OPTIONS (description = 'The date and time when the meter was engaged'),
          lpep_dropoff_datetime TIMESTAMP OPTIONS (description = 'The date and time when the meter was disengaged'),
          store_and_fwd_flag STRING OPTIONS (description = 'This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka "store and forward," because the vehicle did not have a connection to the server. Y= store and forward trip N= not a store and forward trip'),
          RatecodeID STRING OPTIONS (description = 'The final rate code in effect at the end of the trip. 1= Standard rate 2=JFK 3=Newark 4=Nassau or Westchester 5=Negotiated fare 6=Group ride'),
          PULocationID STRING OPTIONS (description = 'TLC Taxi Zone in which the taximeter was engaged'),
          DOLocationID STRING OPTIONS (description = 'TLC Taxi Zone in which the taximeter was disengaged'),
          passenger_count INT64 OPTIONS (description = 'The number of passengers in the vehicle. This is a driver-entered value.'),
          trip_distance NUMERIC OPTIONS (description = 'The elapsed trip distance in miles reported by the taximeter.'),
          fare_amount NUMERIC OPTIONS (description = 'The time-and-distance fare calculated by the meter'),
          extra NUMERIC OPTIONS (description = 'Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges'),
          mta_tax NUMERIC OPTIONS (description = '$0.50 MTA tax that is automatically triggered based on the metered rate in use'),
          tip_amount NUMERIC OPTIONS (description = 'Tip amount. This field is automatically populated for credit card tips. Cash tips are not included.'),
          tolls_amount NUMERIC OPTIONS (description = 'Total amount of all tolls paid in trip.'),
          ehail_fee NUMERIC,
          improvement_surcharge NUMERIC OPTIONS (description = '$0.30 improvement surcharge assessed on hailed trips at the flag drop. The improvement surcharge began being levied in 2015.'),
          total_amount NUMERIC OPTIONS (description = 'The total amount charged to passengers. Does not include cash tips.'),
          payment_type INTEGER OPTIONS (description = 'A numeric code signifying how the passenger paid for the trip. 1= Credit card 2= Cash 3= No charge 4= Dispute 5= Unknown 6= Voided trip'),
          trip_type STRING OPTIONS (description = 'A code indicating whether the trip was a street-hail or a dispatch that is automatically assigned based on the metered rate in use but can be altered by the driver. 1= Street-hail 2= Dispatch'),
          congestion_surcharge NUMERIC OPTIONS (description = 'Congestion surcharge applied to trips in congested zones')
      )
      OPTIONS (
          format = 'CSV',
          uris = ['{{render(vars.gcs_file)}}'],
          skip_leading_rows = 1,
          ignore_unknown_values = TRUE
      );
```
```bq_green_table_ext``` - is a staging table where it will store the csv files temporarily and then load from there into the main table
- will have few properties compared to the main table, use the data from the csv file

```yaml
tasks:
  - id: bq_green_table_tmp
    runIf: "{{inputs.taxi == 'green'}}"
    type: io.kestra.plugin.gcp.bigquery.Query
    sql: |
      CREATE OR REPLACE TABLE `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}`
      AS
      SELECT
        MD5(CONCAT(
          COALESCE(CAST(VendorID AS STRING), ""),
          COALESCE(CAST(lpep_pickup_datetime AS STRING), ""),
          COALESCE(CAST(lpep_dropoff_datetime AS STRING), ""),
          COALESCE(CAST(PULocationID AS STRING), ""),
          COALESCE(CAST(DOLocationID AS STRING), "")
        )) AS unique_row_id,
        "{{render(vars.file)}}" AS filename,
        *
      FROM `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}_ext`;
```
```bq_green_table_tmp``` - will add unique values for the csv file before merging into the main table

```yaml
  - id: bq_green_merge
    runIf: "{{inputs.taxi == 'green'}}"
    type: io.kestra.plugin.gcp.bigquery.Query
    sql: |
      MERGE INTO `{{kv('GCP_PROJECT_ID')}}.{{kv('GCP_DATASET')}}.green_tripdata` T
      USING `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}` S
      ON T.unique_row_id = S.unique_row_id
      WHEN NOT MATCHED THEN
        INSERT (unique_row_id, filename, VendorID, lpep_pickup_datetime, lpep_dropoff_datetime, store_and_fwd_flag, RatecodeID, PULocationID, DOLocationID, passenger_count, trip_distance, fare_amount, extra, mta_tax, tip_amount, tolls_amount, ehail_fee, improvement_surcharge, total_amount, payment_type, trip_type, congestion_surcharge)
        VALUES (S.unique_row_id, S.filename, S.VendorID, S.lpep_pickup_datetime, S.lpep_dropoff_datetime, S.store_and_fwd_flag, S.RatecodeID, S.PULocationID, S.DOLocationID, S.passenger_count, S.trip_distance, S.fare_amount, S.extra, S.mta_tax, S.tip_amount, S.tolls_amount, S.ehail_fee, S.improvement_surcharge, S.total_amount, S.payment_type, S.trip_type, S.congestion_surcharge);
```
```bq_green_merge``` - merge into the main table

- The same exact tasks will be run for the yellow taxi data

## 2.2.7 - Manage Schedules and Backfills with BigQuery in Kestra

- Adding Schedules and Backfills for previous years
- ```06_gcp_taxi_scheduled.yaml```
- only difference with ```06_gcp_taxi.yaml``` is that its added a trigger function, replacing input for this flow
- trigger function means that itll basically run the flow automatically based on the time & date that we want

```yaml
variables:
  file: "{{inputs.taxi}}_tripdata_{{trigger.date | date('yyyy-MM')}}.csv" #replacing inputs with trigger function that will trigger based on the execution date
  gcs_file: "gs://{{kv('GCP_BUCKET_NAME')}}/{{vars.file}}"
  table: "{{kv('GCP_DATASET')}}.{{inputs.taxi}}_tripdata_{{trigger.date | date('yyyy_MM')}}"
  data: "{{outputs.extract.outputFiles[inputs.taxi ~ '_tripdata_' ~ (trigger.date | date('yyyy-MM')) ~ '.csv']}}"
```

```yaml
triggers: # added trigger function that will automatically start the workflow
  - id: green_schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 9 1 * *" # cron schedule, it will run on 9 a.m. on the 1st day of each month
    inputs:
      taxi: green

  - id: yellow_schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 9 1 * *"
    inputs:
      taxi: yellow
```


## 2.2.8 - Orchestrate dbt Models with BigQuery in Kestra
## 2.2.9 - Deploy Workflows to the Cloud with Git in Kestra (Optional)

- Learn how to deploy Kestra to cloud using GC & using git sync plugin to sync everything together
- 50 min install kestra to Cloud
  - how to setup storage in gcs
  - how to use google compute engine to run
  - setup postgres for storing data in kestra
- moving from dev to prod
  - dev - local environment
  - prod - new one in google
  - can use github action to sync one from another 
  - github repo to take data been push from local instance to git
  - sync to cloud on schedule
- Git plugin
  - 2 group of tasks (sync and push)
  - on local dev, use push for flows & namespace files