variable "project" {
    description = "Project"
    default = "dezoom-449006"
}

variable "region" {
    description = "Project Region"
    default = "us-central1"
}

variable "location" {
    description = "Project Location"
    default = "US"
}

variable "bq_dataset_name" {
    description = "BigQuery dataset name"
    default = "demo_dataset_dezoom_449006"
}

variable "gcs_bucket_name" {
    description = "My Storage Bucket Name"
    default = "terraform-demo-dezoom-449006"
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"
}