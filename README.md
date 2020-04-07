# Website Project
  As for this project, we build a website for tenants and landords to get and post off-campus housing information 

# Reqirements
* Docker version 19.03.5
* docker-compose version 1.21.0
  
# Installation
* git clone [repository](ist-git@git.uwaterloo.ca:ece651/react_django.git)
* sudo docker-compose up

# Some Common Command
* Run backend and frontend at the same time:  
   sudo docker-compose up
* Run frontend alone:  
  sudo docker-compose run frontend npm start / run
* Run backend alone:  
  sudo docker-compose run backend python manage.py runserver 0.0.0.0:8000 --settings=hello_world.settings.development
* Test backend:  
  sudo docker-compose run backend python manage.py test
* Test frontend:  
  sudo docker-compose run frontend npm test
* Git push branch:  
git push origin branch-name
* Git fetch remote branch and checkout:
git fetch origin branch-name
git checkout branch-name
# Software stack
Our website runs on the following software:  
* Ubuntu
* Docker
* Docker-compose
* Django
* React
* Node.js
* SQLite
# CI/CD
* Currently, we rely on gitlab runner to do continuous Integration and Testing.
* Manully deploy our website on the AWS EC2 server:
[Website Link](http://ec2-18-188-108-51.us-east-2.compute.amazonaws.com:3000/)
# Test Tool
* Jest
* Enzyme
# System Architecture
```mermaid
graph TB

  SubGraph1[Send API request] --> SubGraph1Flow
  subgraph "Backend"
  SubGraph1Flow(Django_rest framework) --> n[Database]
  end

  subgraph "Frontend"
  HTTPRequest[HTTP Request] --> Nodejs[Nodejs]
  Nodejs[Node.js] -->  Reactcomponent[Render React component]
  Reactcomponent[Render React component] --> SubGraph1[Send API request]
end
```
