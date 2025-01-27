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

## [2.2.1.1 Getting Started with Kestra](https://www.youtube.com/watch?v=a2BZ7vOihjg)

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


## 2.2.2 - Learn Kestra




## 2.2.3 - ETL Pipelines with Postgres in Kestra
## 2.2.4 - Manage Scheduling and Backfills with Postgres in Kestra
## 2.2.5 - Orchestrate dbt Models with Postgres in Kestra
## 2.2.6 - ETL Pipelines in Kestra Google Cloud Platform - Kestra
## 2.2.7 - Manage Schedules and Backfills with BigQuery in Kestra
## 2.2.8 - Orchestrate dbt Models with BigQuery in Kestra
## 2.2.9 - Deploy Workflows to the Cloud with Git in Kestra