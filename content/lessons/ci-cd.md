---
title: CI/CD
summary: Essential techniques for automatically testing & deploying changes to code.
competencies:
- "Software Engineering"
---

## Why Learn CI/CD?

- **Amplify benefits of tests** - tests allow you to test for incorrectness and improve code with confidence.
- **Repeatable, low maintenance deployments** - deploy code using consistent, re-runnable pipelines.

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

        # 
        - name: install dependencies and run tests
          run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pytest tests
```

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

        - name: run cdk deploy with environment variables
          run: |
            cdk deploy --require-approval never
          env:
            AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
            AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```
