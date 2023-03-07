# End-to-End Machine Learning Project, CI/CD Pipeline, and Deployment
 
 In this project, we will discuss the steps involved in creating an end-to-end machine learning project, setting up a CI/CD pipeline, and deploying the application. We will start by discussing Git and GitHub repositories, followed by the setup.py file in Python.
 
 ## Git and GitHub Repositories
 
 Git is a version control system that allows developers to keep track of changes made to their code over time. GitHub is a web-based platform that allows developers to store and manage their Git repositories.
 Hope you have installed git and acount in both both git and github.
 for download git refer [this]([https://git-scm.com/downloads])
 To get started, you will need to create a new repository on GitHub. Once you have created your repository, you can clone it to your local machine using the following command:
 
 
 ```Git clone from repository
 git clone <repository-url>
 ```

```
git add .
git commit -m "commit message"
git push origin main
```
add .gitignore file  for not pushing unusefull things in github
due to change in code from your local directoy use this in your terminal
```
git pull
```
It is important to commit your changes frequently and provide descriptive commit messages to keep track of changes made to the code.
Please, refer to [git documentation]([https://git-scm.com/docs]) for more information.

## Setup.py File in Python

The setup.py file is used to specify the details of your Python project, such as its name, version, and dependencies. It is used by tools such as pip to install your project and its dependencies.
* crete a python file and add code acording to above repo

## requirements.txt
it contains all required libraries  and a '-e .' to automaticaly trigger setup.py
after making all changes add and commit your changes.
