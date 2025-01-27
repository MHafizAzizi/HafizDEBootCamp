# Terraform

## 1.3.1 - Terraform Primer

**Terraform?**
  - Infrastructure as a Code (IaC)
  - Can define both cloud & on-prem resources in human-readable configuration files that can be version, reuse & share

**Advantages?**
  - Easy to ensure resources are removed
  - Easy to collaborate
  - Reproducibility

**What Terraform Does Not**
  - Manage & update code on infrastructure
  - Change immutable resources
  - Manage resources not defined in Terraform file


**Terraform Provider**
  - Code that allow Terraform to communicate to manage resources on
    - AWS
    - Azure
    - GCP
    - Kubernetes
    - Among others...

**Key Command**
```init``` - retrieve the providers based on the used resources
```plan``` - display what actions that will be taken
```apply``` - applying the action in the ```.tf``` files
```destroy``` - remove everything defined in the tf files

## 1.3.2 Terraform Basics

**Prerequisite**
  - GCP Account
  - Terraform


**GCP Account**
  - Create a Project (keep in mind of the project id, can find in the dashboard)
  - ```Create Service Account```
    - ```IAM & Admin```
      - Create Service Accoount
        - GCP Bucket - Storage Admin
        - Bigquery - Bigquery Admin
        - Compute Engine - Compute Admin
      - Edit Permission
        - ```Edit Principal```
        - Can add or remove permission

**Authorization Key**
  - GCP Authorization Key is a JSON or P12 that has the credential for a service account. 
  - Used to authenticate GCP service accounts for managing GCP resources & interacting with GCP API
  - Navigate to your ```Service Account```, then ```Manage Keys```
    - ```Add Key``` > ```Create New Key``` > ```JSON Key```
    - The key will be saved to your computer
    - **PLEASE TAKE NOTE YOUR JSON KEY, CAN DELETE AND RECREATE ANYTIME**
- Adding the key into the environment variable
	- ```export GOOGLE_CREDENTIALS="path_to_file/file.json"```

**Terraform Main. Tf**
- ```main.tf``` is a Terraform config files thatll let us config the settings and providers that we need, which in this case is GCP
- [Hashicorp Google Cloud Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- Copy the ```Use Provider``` inside the ```tf```

```
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.11.0"
    }
  }
}

provider "google" {
  # Configure your project & region here
	project = 'project_id'
	region = 'region'
}
```

**Initialise the Project**
```terraform init``` - this initialise a working directory containing the config files & install plugins for the required providers, Google provider in this case, which is a code that connect to the GCP

```.terraform folder``` - contain subcategories & files related to the initialisation & plug in management
```.terraform.lock.hcl folder``` - lock file that records a list of provider plugins & their version as hashes




