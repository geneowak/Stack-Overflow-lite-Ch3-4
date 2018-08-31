# StackOverflow-lite

[![Build Status](https://travis-ci.com/geneowak/Stack-Overflow-lite-Ch3-4.svg?branch=tests_for_api)](https://travis-ci.com/geneowak/Stack-Overflow-lite-Ch3-4)
[![Coverage Status](https://coveralls.io/repos/github/geneowak/Stack-Overflow-lite-Ch3-4/badge.svg?branch=tests_for_api)](https://coveralls.io/github/geneowak/Stack-Overflow-lite-Ch3-4?branch=tests_for_api) 
[![Maintainability](https://api.codeclimate.com/v1/badges/38f513cdfe1984e4be8a/maintainability)](https://codeclimate.com/github/geneowak/-StackOverflow-lite/maintainability)

## Description

Stack Overflow-lite is a platform where users can create accounts to questions and answer some question.
This is a project assignment being done in Andela Cohort 11 boot camp

## Features

1. Users can create an account and log in.
2. Users can post questions.
3. Users can delete the questions they post.
4. Users can post answers.
5. Users can view the answers to questions.
6. Users can accept an answer out of all the answers to his/her question as the preferred answer.
7. Users can comment on an answer or a question.
8. Users can view all questions he/she has ever asked on the platform via their profile.
9. Users can search for questions on the platform.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. The project is not yet finished so it can not yet be deployed as a fully working system.

### Prerequisites

What things you need to install the software

* Python

### Installing

A step by step series of examples that tell you how to get a development env running

To deploy this application follow the following steps

* Clone the project from git hub
* Install python onto your system. You can installation instructions [here...](https://realpython.com/installing-python/)
* Create a python virtual environment in the root of the folder of the application and activate it.
* Install all the libraries in the **"requirements.txt"** file. You may find this [link](http://flask.pocoo.org/docs/1.0/installation/) helpful for setting up the virtual environment and flask.
* Navigate to the root of the project and execute the application by running a command "python run.py"

Once the application starts running. Then you can proceed to test the application using postman. The application by default runs on port 5000
. If everything is done right you will see a url like http://127.0.0.1:5000/ can be used to access the application through a browser.

These are the endpoints that are currently available

|__Type__| __Endpoint__ | __What the endpoint does__ |
|------|-------------|------------|
|GET|  /api/v1/questions       | Fetch all questions     |
|GET| /api/v1/questions/\<int:questionId\>        | Fetch a specific question |
|POST|  /api/v1/questions       | Add a question     |
|POST|  /api/v1/answers       | Get answers     |
|GET|  /api/v1/questions/\<int:questionId\>/answers       | Add an answer     |
|POST|  /api/v1/questions/\<int:questionId\>/comments       | Add a comment to a question     |
|POST|  /api/v1/answers/\<int:answerId\>/comments        | Add a comment to an answer     |
|GET|  /api/v1/comments        | Get comments     |

## Running the tests

Tests can be run by running the command below at the root of the project directory

```
if not installed run "pip install pytest" to install pytest
then "pytest" to run the test
```

You can also get the test coverage by running the command below. This requires you to have installed pytest.
After installing pytest install the following

```
pip install pytest-cov
pip install pytest-xdist
```

Then navigate to the root of your directory and run the following commands

```
py.test --cov=API API/tests/
```

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - Python web framework used

## Versioning

URL Versioning has been used to version this applications endpoint

We are currently working on version:1
