# SETTING ENVIRONMENT
CAN USE **GITHUB CODESPACE** OR **GOOGLE CLOUD VM + SSH ACCESS**

## 1.4.2 GITHUB CODESPACE
1. CREATE NEW REPO AT GITHUB
2. SIDEBAR -> CODESPACE -> OPEN IN VSCODE DESKTOP
3. INSTALL NECESSARY EXTENSION
4. INSTALL HASHICORP TERRAFORM (https://developer.hashicorp.com/terraform/install)
5. PIP INSTALL JUPYTER NOTEBOOK
6. OPTIONAL
    - GIT COMMAND
        1. GIT ADD . (stage all modified & new files in repo)
        2. GIT COMMIT -M "COMMENT HERE" (COMMIT INTO REPO AFTER STAGING)
        3. GIT PUSH (PUSH INTO REMOTE/ONLINE REPO)
        4. GIT PULL (FETCH & MERGE LATEST CHANGE FROM REMOTE BRANCH INTO LOCAL BRANCH)

## 1.2.1 - INTRODUCTION TO DOCKER
1. ``` docker run hello-world ``` = container
    
    - when run, itll go to the DockerHub to find the ``` hello-world ``` image & download it, and run it
2. ``` docker run -it ubuntu bash ```
    
    - ``` -it ``` - run the docker in interactive mode, will be able to interact in the terminal
    - ``` ubuntu bash ``` - anything thats typed after the image ```ubuntu``` is the parameter ```bash```
3. ``` docker run -it python:3.9 ```
    
    - image = ```python```
    - tag = ``` :3.9 ``` - specific version of an image
4. ``` docker run -it --entrypoint=bash python:3.9 ```

    - ``` --entrypoint= ``` - when you want to run a base command, which in this case is ```bash```
    - note that when we close the container, any library thats install in those images are also gone, causing the need to ```pip install``` everytime we run the images
5. create ```Dockerfile```, which is a custom ```image``` that we can install any dependencies and configurations inside.
    
    ``` docker
        FROM python:3.9

        RUN pip install pandas

        ENTRYPOINT [ "bash" ]
    ``` 
6. next we need to build a new image from the dockerfile,

    - ```docker build -t [name]:[tag] [location]```
    - ```docker build -t test:pandas .```
7. test the image see if it works

    - ```docker run -it test:pandas```

8. dockerfile that runs a pipeline.py file
    
    - update the dockerfile
    ``` docker
        FROM python:3.9

        RUN pip install pandas

        WORKDIR /app
        COPY pipeline.py pipeline.py

        ENTRYPOINT [ "python", "pipeline.py" ]
    ``` 
9.  ```docker run -it test:pandas 2025-01-22```
10. the output would be ```['pipeline.py', '2025-01-22'] job is done for 2025-01-22```

## 1.2.2 - Ingesting NY Taxi Data to Postgres

1. PostgreSQL is an object relational database management system (ORDBMS) with SQL capability. To run postgres we use the official docker image ```postgres:17```. Eventually we will use docker compose, but for the first example, we will use the command line.

- Make sure theres no space following the backslash
```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --name pgdatabase
  postgres:17-alpine
```
- ```-e``` environment variables to configure the postgres
- ```-p``` [host port]:[container port] mapping the host port to the container port
- ```-v``` [path to host folder]:[path to container folder]














### What is Docker?
- Platform as a Service (PaaS) that use OS level virtualization to deliver software in packages called **Containers**