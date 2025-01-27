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
  - [Terraform](https://developer.hashicorp.com/terraform/install)


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
  - ```echo $GOOGLE_CREDENTIALS``` to verify the key

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

**Resources**
- [Google Cloud Storage Bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket.html)
- [BigQuery](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset)
- [Terraform GitIgnore](https://github.com/github/gitignore/blob/main/Terraform.gitignore) - will exclude some files to be uploaded into github


**Cloud Storage Bucket**
```terraform
resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-demo-dezoom-449006"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1 #day
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
```
```resource``` - (resources) (variable name)
```name``` - globally unique name. Can use a name variation of the bucket
```age``` - day

**BigQuery Dataset**

```terraform
resource "google_bigquery_dataset" "demo-dataset" {
  dataset_id = "demo-dataset-dezoom-449006"
  location   = "US"
}
```
**Terraform Plan**

```terraform plan``` will display the actions that will be taken based from the ```main.tf``` that we just configured 

```terraform
  # google_storage_bucket.demo-bucket will be created
  + resource "google_storage_bucket" "demo-bucket" {
      + effective_labels            = {
          + "goog-terraform-provisioned" = "true"
        }
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "terraform-demo-dezoom-449006"
      + project                     = (known after apply)
      + project_number              = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = {
          + "goog-terraform-provisioned" = "true"
        }
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type          = "AbortIncompleteMultipartUpload"
                # (1 unchanged attribute hidden)
            }
          + condition {
              + age                    = 1
              + matches_prefix         = []
              + matches_storage_class  = []
              + matches_suffix         = []
              + with_state             = (known after apply)
                # (3 unchanged attributes hidden)
            }
        }

      + soft_delete_policy (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }
```

**Terraform Apply**

```terraform apply``` runs the action configured in the ```main.tf```, create a bucket to the Cloud Storage, while creating a ```terraform.tfstate```, which tracks of resources created from the config.

**Terraform Destroy**

```terraform destroy``` views the ```terraform.tfstate``` and check changes to made to delete the resources.
- ```terraform.tfstate.backup``` updated with the current state before the change.
- ```terraform.tfstate``` updated with the state after the change.