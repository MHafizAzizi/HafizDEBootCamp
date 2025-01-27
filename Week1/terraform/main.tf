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