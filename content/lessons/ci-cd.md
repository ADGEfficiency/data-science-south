---
title: CI/CD
summary: TODO
---

## Why Continuous Integration?

Continuous Integration (CI) is a software engineering technique where changes to a codebase are tested automatically.

Automated testing allows teams to detect and fix problems before they are merged into branches that deploy infrastructure to the cloud.

CI is based around testing Git branches, commonly on pull requests, before code is merged from one branch to another.  

It's also common to run tests after two branches have been merged, or on push to a branch.

## Continuous Integration in GitHub Actions

GitHub Actions is a CI/CD (Continuous Integration/Continuous Deployment) provider that integrates directly with GitHub.

Github Actions is configured by putting `lang:shell-session:yaml` files into the `lang:shell-session:.github/workflows` folder of a Github repository.

`lang:shell-session:.github/workflows/test.yaml` is a CI workflow that runs on every pull request to the `lang:shell-session:main` branch.

It sets up a Python environment, installs dependencies, and then runs tests using the Python library `pytest`:

```yaml
fn:.github/workflows/test.yaml
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
          with:
            python-version: 3.10.6

        - run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pytest tests
```

## Why Continuous Deployment?

Continuous Deployment (CD) is a software engineering technique where changes to a codebase are deployed automatically.

Automated deployments allows teams to deploy infrastructure to the cloud reliably, without any manual work.

CD is based around deploying Git branches, commonly after code is merged or pushed from one branch to another.

## Continuous Deployment in GitHub Actions

GitHub Actions is a CI/CD (Continuous Integration/Continuous Deployment) provider that integrates directly with GitHub.

Github Actions is configured by putting `yaml` files into the `.github/workflows` folder of a Github repository.

`.github/workflows/deploy.yaml` is a CI workflow that runs on every push to the `main` branch.

It sets up Node & Python environments, installs dependencies, and then deploys a CDK app to AWS:

```yaml
fn:.github/workflows/deploy.yaml
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
          with:
            node-version: '18'

        - run: |
            npm install aws-cdk-lib@2.75.0

        - uses: actions/setup-python@v4
          with:
            python-version: 3.10.6

        - run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        - run: |
            cdk deploy --require-approval never
          env:
            AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
            AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```
