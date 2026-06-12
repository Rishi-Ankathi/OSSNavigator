# OSSNavigator

OSSNavigator (Open Source Contribution & Learning Navigator) is a platform designed to help developers understand unfamiliar open-source repositories and reduce the barriers to making meaningful contributions.

## Problem

Many developers want to contribute to open source but struggle with:

* Understanding large and unfamiliar codebases
* Navigating complex repository structures
* Identifying where to start learning
* Finding contribution opportunities that match their skills

As repositories grow, the onboarding process becomes increasingly difficult for new contributors.

## Solution

OSSNavigator aims to simplify repository exploration and contribution onboarding by analyzing repository information and presenting it in a structured and accessible way.

The project focuses on helping contributors answer questions such as:

* What does this repository contain?
* How is the project organized?
* Which modules are important?
* Where should I start learning?
* Which areas of the repository are relevant to a specific contribution?

## Current Features

### Repository Metadata Analysis

Retrieve repository information using the GitHub REST API:

* Repository name
* Owner
* Description
* Primary language
* Stars
* Forks

### Repository Structure Analysis

Analyze repository contents and extract:

* Root-level directories
* Root-level files
* Repository organization overview

## Tech Stack

* Python
* FastAPI
* GitHub REST API
* Pydantic
* Requests

## Project Structure

```text
OSSNavigator/
│
├── practice/
│   ├── fastapi_basics/
│   ├── database_basics/
│   └── github_api_basics/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   └── github_services.py
│   ├── models/
│   │   └── repo_models.py
│   └── database/
│       └── database.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Rishi-Ankathi/OSSNavigator.git
cd OSSNavigator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

### Open API Documentation

```
http://127.0.0.1:8000/docs
```

## Future Scope

* Recursive repository structure traversal
* Repository file analysis
* Contributor profiling
* Repository learning paths
* Issue exploration and matching
* Contribution guidance
