# Casserole API 
A cute little REST API for retrieving casserole recipes from a database.
* This application is for demo use only. 
* Contributions are not currently being accepted.
## Table of Contents
* [About This Document](#about-this-document)
* [Running the Application](#running-the-application)
* [Authentication](#authentication)
* [Viewing Casseroles](#viewing-casseroles)
## About This Document
This README assumes you know how to:
* Use git.
* Use a command line interface. 

All example API calls are given in cURL, but can be performed with the HTTP client of your choice. 

## Running the Application
**To run the application locally:**
1. Ensure that docker is installed in your environment and running. 
2. From the command line, navigate to the project root directory.
3. Run the following command to build the image: `docker build -t casseroleapi .`
4. Run the following command to run the container: `docker run -p 8000:8000 casseroleapi`
5. When finished using the application, stop the container with `ctrl + c`.  
## Authentication
**To obtain an API key:**
1. From the command line, run the following: 
    ```
    curl -X POST http://localhost:8000/auth/ \
    -H "Content-Type: application/json" \
    -d '{"username": "guest", "password": "12345"}'
    ```
2. Add the returned API key string to the authorization headers of all subsequent API calls. Include the keyword `Bearer`. Examples are given in the following sections. 

## Viewing Casseroles
**To view all casseroles in the database:** 

```
curl -X GET http://localhost:8000/casseroles/ \
-H "Authorization: Bearer <your-api-key>"
```

**To view the recipe for a specific casserole:**
```
curl -X GET http://localhost:8000/casseroles/<casserole-name>/ \
-H "Authorization: Bearer <your-api-key>"
```
