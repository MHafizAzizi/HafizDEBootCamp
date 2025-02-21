# Week 4 Analytics Engineering

## 4.1.1 Analytics Engineering Basics

**What is Analytics Engineering?**

- Observe the recent advancements in the data field
- Cloud Data Warehouse (BigQuery, Snowflake, Redshift) reduced storage & computing costs
- ETL have been simplified with tools like FiveTran or Stitch
- SQL-first tools like Looker introduced version control system to data workflow
- BI tools (Mode) enable self-service analytics
- Data Governance changed the way data teams work & how stakeholders consume data.

- This causes a gap in the roles within the data team.

**Roles in a Data Team**

- The traditional data teams consists or:-
- Data Engineer - preparing & maintaining the necessary infrastructure for the data team
- Data Analyst - utilise the data stored in the infrastructure to answer questions & solve problems
- But recent developments has showed that Data Scientists & Data Analysts are increasingly writing code, but more importantly they aren't meant to be software engineers & not received training for that purpose
- As well as for DE, although skilled in software engineering, lack training on how the data will actually be used by the business & users
- This is where analytics engineer comes in to bridge the gap


**Tooling**

- Analytics Engineer may work with various tools such as loading tools such as FiveTran or Stitch, which also used by DE
- Data Storing tasks maybe involved such as using Cloud Data Warehouse, which are also shared with DE
- Additionally, Analytics Engineer are also focuses on implementing good data modelling practices with tools like dbt or Dataform
- As well as handling data presentation using BA tools like Google Data Studio

**Data Modelling Concepts**
- Recap the ETL, ELT difference
- ETL - Extract, Transform, Load into DW
- ELT - Extract, Load, Transform
- ETL takes longer to load since we're need to transform the data first, but more stable & compliant data
- ELT is faster & flexible since the data already loaded inside DW
- Take advantage of Cloud DW due to reduced storage & computing costs, we can afford the load all of our data into DW & transform in there

- Learning the Kimball's Dimensional Modeling concept
- Main objective - deliver understandable data to business user & also achieving fast query performance
- Unlike third normal form (3NF), the dimension modeling doesn't prioritise eliminate data redundancy, instead prioritise user's understanding of the data & query performance
- To dive deeper, Bill Inmon & Data Vault are other approaches

**Elements of Dimensional Modeling**
- Mainly involve two types of tables,
	- Facts Table
	  - Contain measurement, metrics or facts
	  - Corresponds to business process
	  - Verbs
	- Dimensional Tables
	  - Corresponds to a business entity
	  - provides context to a business
	  - Nouns

- Imagine the Kimball's Dimensional modelling is a kitchen
	- Restaurant - Data Warehouse, ETL Process
	- Pantry - Staging area, where raw data are contained and not meant to be exposed to everyone
	- Kitchen - Processing Area, making data models from the raw data, focusing on efficiency and ensuring standards are being followed when making the data models
	- Dining Area - Presentation Area, we present out transformed data to the stakeholders

