---
title: CI/CD
description: Automation techniques for testing & deploying infrastructure driven by changes to code.
date: 2024-12-07
competencies:
- "Software Engineering"
---

## Why Learn CI/CD?

CI/CD is a safety net for developers working in teams. It helps reduce human error by automating two key development workflows - testing and deployment.

Learning CI/CD will allow you to:

- **Avoid breaking production unnecessarily** - CI checks that code passes tests before merging, avoiding deploying known breaking changes.
- **Avoid human error** - CD deploys code with a pipeline that requires no manual input.
- **Get more from your Git repositories** - both CI and CD run based on changes to Git branches, allowing you to make your code changes do things like deploy to production.

A well engineered CI/CD system offers repeatable, low maintenance deployments.  It's a crucial part of working with others - with CI you know that both your and your colleagues code has passed tests, and that deployments are done consistently across the entire team.

## Continuous Integration

Continuous Integration (CI) is a software engineering technique where changes to a codebase are tested automatically before merging code and deploying to environments like dev or prod. 

Testing allows teams to detect and fix problems before they are merged into branches that deploy infrastructure to the cloud.

CI is based around testing Git branches, commonly on pull requests, run before code is merged from one branch to another.  These tests are often run when a pull request is open.  Each commit to the branch will kick off testing of the updated code.

It's common to run tests again after a branch has been merged, to ensure that the codebase is still working as expected.

### Continuous Integration in GitHub Actions

GitHub Actions integrates directly with GitHub.

Github Actions is configured with `yaml` files into the `.github/workflows` folder of a GitHub repository.

The file `.github/workflows/test.yaml` below is a CI workflow that runs on every pull request to the `main` branch:

```yaml { title = ".github/workflows/test.yaml" }
name: test

on:
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
        - uses: actions/checkout@v3

        - uses: actions/setup-python@v4
          name: setup a python environment
          with:
            python-version: 3.10.6

        - name: install dependencies and run tests
          run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pytest tests
```

In Github Actions, pipelines will automatically be setup when the YAML file is put into the `.github/workflows` folder in a GitHub repository.

### Continuous Integration in Azure DevOps

Azure DevOps also uses pipelines defined in `yaml` to define CI workflows.

Below is an example of a CI pipeline that runs on every pull request to the `main` branch:

```yaml
trigger:
- main

pr:
- main

jobs:
- job: test
  pool:
    vmImage: 'ubuntu-latest'

  steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.10.6'
      addToPath: true

  - script: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
      pytest tests
    displayName: 'Install dependencies and run tests'
```

In Azure Devops, pipelines will not automatically run when the YAML file is created.  You need to setup the pipeline through the Azure Devops web interface after adding the YAML file to your Azure Devops respository.

## Continuous Deployment

Continuous Deployment (CD) is a software engineering technique where changes to a codebase are deployed automatically.

Automated deployments allows teams to deploy infrastructure to the cloud automatically, without any manual work.  Manual deployments come with the non-zero risk of human error, and cost of developer time.

CD is based around deploying Git branches, commonly after code is merged or pushed from one branch to another. CD should only occur after CI tests have passed.

### Continuous Deployment in GitHub Actions

`.github/workflows/deploy.yaml` is a CD workflow that runs on every push to the `main` branch:

```yaml { title = ".github/workflows/deploy.yaml" }
name: deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
        - uses: actions/checkout@v3

        - uses: actions/setup-node@v2
          name: setup node
          with:
            node-version: '18'

        - run: |
            npm install aws-cdk-lib@2.75.0

        - uses: actions/setup-python@v4
          name: setup a python environment
          with:
            python-version: 3.10.6

        - name: install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        - name: deploy with python
          run: |
            python deploy.py
          env:
            AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
            AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

The environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are set from secrets in the GitHub repository.  These secrets are usually added manually via the GitHub web interface.

### Continuous Deployment in Azure DevOps

Below is an example of a CD pipeline that runs on every push to the `main` branch:

```yaml
trigger:
- main

jobs:
- job: deploy
  pool:
    vmImage: 'ubuntu-latest'

  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.10.6'
      addToPath: true

  - script: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
    displayName: 'Install Python dependencies'

  - script: |
      python deploy.py
    displayName: 'Deploy with Python'
    env:
      CLIENT_ID: $(CLIENT_ID)
      CLIENT_SECRET: $(CLIENT_SECRET)
      TENANT_ID: $(TENANT_ID)
```

The environment variables `CLIENT_ID`, `CLIENT_SECRET` and `TENANT_ID` are set from variables in the Azure Devops pipeline. These secrets are usually added manually via the Azure Devops web interface.
