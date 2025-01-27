terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.17.0"
    }
  }
}

provider "google" {
  # Configure your project & region here
	project = "dezoom-449006"
	region = "us-central1"
}

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

# resource "google_bigquery_dataset" "demo-dataset" {
#   dataset_id = "demo-dataset-dezoom-449006"
#   location   = "US"
# }