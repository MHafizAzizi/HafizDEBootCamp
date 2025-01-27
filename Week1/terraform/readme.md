# Terraform

## 1.3.1 - Terraform Primer

Terraform?
  - Infrastructure as a Code (IaC)
  - Can define both cloud & on-prem resources in human-readable configuration files that can be version, reuse & share

Advantages?
  - Easy to ensure resources are removed
  - Easy to collaborate
  - Reproducibility

What Terraform Does Not
  - Doesnt manage & update code on infrastructure
  - Cant change immutable resources
  - Cant manage resources not defined in Terraform file


Terraform Provider
  - Code that allow Terraform to communicate to manage resources on
    - AWS
    - Azure
    - GCP
    - Kubernetes
    - Among others...

Key Command
```init``` - retrieve the providers based on the used resources
```plan``` - display what actions that will be taken
```apply``` - applying the action in the ```.tf``` files
```destroy``` - remove everything defined in the tf files

1.3.2 Terraform Basics

Prerequisite
  - GCP Account
  - Terraform


GCP Account
  - Create a Project (keep in mind of the project id, can find in the dashboard)
  - Create Service Account
    - IAM & Admin
      - Create Service Accoount
        - GCP Bucket - Storage Admin
        - Bigquery - Bigquery Admin
        - Compute Engine - Compute Admin
      - Edit Permission
        - ```Edit Principal```
        - Can add or remove permission

Authorization Key
  - GCP Authorization Key is a JSON or P12 that has the credential for a service account. 
  - Used to authenticate GCP service accounts for managing GCP resources & interacting with GCP API
  - Navigate to your Service Account, then ```Manage Keys```
    - Add Key > Create New Key > JSON Key
    - The key will be saved to your computer
    - PLEASE TAKE NOTE YOUR JSON KEY, CAN DELETE AND RECREATE ANYTIME


