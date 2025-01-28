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

- Workflow known as Flows in Kestra
- Declared in YAML
- Works with any language

**Kestra Properties**
- ```id``` name of flow
- ```namespace``` environment for the flow
- ```tasks``` list of tasks to execute in your flow

**Input**
```kestra

inputs:
    - id: variable_name
      type: STRING
      defaults: example_string

{{ inputs.variable_name }}
```
**Output**
```{{ outputs.task_id.vars.output_name }}```

**Triggers**

```kestra
triggers:
    - id:hour_trigger
      type: io.kestra.core.models.triggers.types.Schedule
      cron: 0 * * *
```
### 2.2.2.2 Learn the Fundamentals of Kestra

```kestra

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

```kestra
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

### 2.2.2.4 Pass Data Between Tasks with Outputs

## 2.2.3 - ETL Pipelines with Postgres in Kestra

[Dataset](https://github.com/DataTalksClub/nyc-tlc-data/releases)
- Main task to create a workflow to process the data each month and added into a table that combines it
- Workflow
  - Extract Data from the repo
  - load into a table in postgres db
  - combine into a main table
  - Transform the data, merge into a table

FLOW

```kestra
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
      - wget -q0- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{{inputs.taxi}}/{{render(vars.file)}}.gz | gunzip > {{render(var.file)}}
```


## 2.2.4 - Manage Scheduling and Backfills with Postgres in Kestra
## 2.2.5 - Orchestrate dbt Models with Postgres in Kestra
## 2.2.6 - ETL Pipelines in Kestra Google Cloud Platform - Kestra
## 2.2.7 - Manage Schedules and Backfills with BigQuery in Kestra
## 2.2.8 - Orchestrate dbt Models with BigQuery in Kestra
## 2.2.9 - Deploy Workflows to the Cloud with Git in Kestra