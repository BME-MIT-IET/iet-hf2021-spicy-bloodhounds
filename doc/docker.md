# Dockerizing Cocoa-bot

##  Docker fundamentals
Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime. 

Continuous integration support: Docker supports CI tools like Travis and Jenkins. Docker images can be built and tagged with specific versions and deployed anywhere.

## DockerFile

In order to use docker we created a Dockerfile that gives the instructions. It contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession.

In our case Dockerfile gives the following instructions:
- sets python:3.8-slim-buster as a base image
- installs sudo, postgre, psycopg2
- installs the requirements
- creates a user
- defines main.py as entrypoint

### Example of starting a container

Creating docker image:

![image](https://user-images.githubusercontent.com/33528244/118400032-3eb38480-b660-11eb-9da9-8b31274011d1.png)


![image](https://user-images.githubusercontent.com/33528244/118400055-53901800-b660-11eb-84da-d15424838fb9.png)

Running the container using created image:

![image](https://user-images.githubusercontent.com/33528244/118400144-aff33780-b660-11eb-89eb-2b4ede8f218b.png)

The container is the excited state because it needs postgre to be running.
We can see the logs: 

![image](https://user-images.githubusercontent.com/33528244/118400165-c0a3ad80-b660-11eb-8f07-b445999f2565.png)

## Docker Compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. 

In our case we need an instance of our python app and postgre database. We described this services in the docker-compose.yml file. 
We specified that cocoa service is dependent from database.
We need different environment variables for database initialization that we specify in .env file.

### Example of starting containers using compose

In the following example we show how db and cocoa services interact.
From the logs we can see the error regarding the connections, which we didn't resolve yet.
The problem might be that there is one more environmental variable, which is a token.
Since token is a sensitive information, it should be stored in the secret.
Secrets are supported by Docker Swarm or Kubernetes bur these are not part of our assignment.

![image](https://user-images.githubusercontent.com/33528244/118399948-e41a2880-b65f-11eb-82ce-2b062184bafa.png)


![image](https://user-images.githubusercontent.com/33528244/118399987-11ff6d00-b660-11eb-8b4c-bdd45077a8be.png)

![image](https://user-images.githubusercontent.com/33528244/118400011-29d6f100-b660-11eb-8411-bce382520fe8.png)








