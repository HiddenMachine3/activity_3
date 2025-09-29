# Activity 3

![Pytest](https://github.com/HiddenMachine3/activity_3/actions/workflows/pytest_tests.yml/badge.svg)

![Pylint](https://github.com/HiddenMachine3/activity_3/actions/workflows/pylint.yml/badge.svg)

![SonarQube](https://github.com/HiddenMachine3/activity_3/actions/workflows/sonarqube.yml/badge.svg)

![Secrets Scan](https://github.com/HiddenMachine3/activity_3/actions/workflows/secrets_scan.yml/badge.svg)

![GCR Deploy](https://github.com/HiddenMachine3/activity_3/actions/workflows/gcr_deploy.yml/badge.svg)

url of hosted version : https://activity-3-670473745035.asia-south1.run.app/




# DevSecOps CI/CD Pipeline Project

This project demonstrates a basic DevSecOps pipeline using GitHub Actions to automate code quality, testing, and security checks for a simple Python application. The application was containerized and deployed on google cloud run.

## Objective

The primary goal is to showcase an understanding of DevSecOps principles by integrating automated security and quality gates directly into the CI/CD pipeline to help in identifying and mitigating issues early in the development lifecycle

## Application Overview

The project is a simple calculator web app made with Streamlit. It performs basic arithmetic operations (addition, subtraction, multiplication).

-   `streamlit_app.py`: The main application file.
-   `funcs.py`: Contains the core logic for the calculator functions.
-   `test_main.py`: Unit tests for the functions in `funcs.py`.

## CI/CD and Security Setup

The CI/CD pipeline is configured using GitHub Actions and is defined in the `.github/workflows/` directory. It consists of the following automated jobs:

1.  **Linting (`pylint.yml`)**:
    -   **Trigger**: Runs on every push.
    -   **Action**: Uses `pylint` to analyze the Python code for styling errors, potential bugs, and code smells.

2.  **Unit Testing (`pytest_tests.yml`)**:
    -   **Trigger**: Runs on pushes and pull requests to the `main` branch.
    -   **Action**: Executes the unit tests using `pytest` to validate that the core functions work as expected.

3.  **Static Code Analysis (`sonarqube.yml`)**:
    -   **Trigger**: Runs on pushes and pull requests to the `main` branch.
    -   **Action**: Utilizes SonarCloud for Static Application Security Testing (SAST). It scans the code for security vulnerabilities, bugs, and code quality issues, providing a detailed analysis report.

4.  **Secret Scanning (`secrets_scan.yml`)**:
    -   **Trigger**: Runs on every push and pull request.
    -   **Action**: Uses `Gitleaks` to scan the repository's history for any hardcoded secrets or sensitive credentials. This helps prevent accidental exposure of secrets.

5.  **Continuous Deployment (`gcr_deploy.yml`)**:
    -   **Trigger**: Runs on every push to the `main` branch.
    -   **Action**: Automates the deployment of the application to Google Cloud Run. It builds the Docker image, pushes it to Google Container Registry, and deploys the new version.


## Challenges and Assumptions

### Challenges
-   **Google Cloud Deployment**: Setting up the automated deployment required creating a service account with the correct permissions (IAM roles) was a bit of a pain. Outdated guides and rarity of upto date info on how to integrate this in github actions was a bit of a challenge, but with a bit of trial and error, it was possible. 

### Assumptions
-   The project has already been hosted on GitHub, and GitHub Actions is the chosen CI/CD platform.
-   A SonarCloud account has been created and linked to the GitHub repository.
-   The necessary secrets (`SONAR_TOKEN`, `GCP_SA_KEY`) have been configured in the repository's "Secrets and variables" settings for the Actions to use. The `GITHUB_TOKEN` is automatically provided by GitHub.
-   A Google Cloud service account has been created and its JSON key is stored in the `GCP_SA_KEY` secret. The service account has been granted the following IAM roles to allow it to build and deploy the application:
    -   Artifact Registry Reader
    -   Artifact Registry Writer
    -   Service Account User
    -   Service Usage Admin
    -   Cloud Build Editor
    -   Cloud Run Admin