# Corider_Flask_Application
>should have
 - Docker running in the background
 - code editor like VS Code
 - postman to test api end points

>Steps to setup 

step-1 git clone
clone the repo to you local pc from VS Code terminal or normal bash
```bash
git clone https://github.com/Deshik7177/Corider_Flask_Application.git
```
step-2 run file
enter the command in the cloned directory
```bash
docker compose up --build
```

step-3 test rest-api end points in postman
open local host in postman then make a get request you should see #Flask Backend Working  
```bash
localhost:5000
```
then try these end points
 - GET /users - Returns a list of all users.
 - GET /users/<id> - Returns the user with the specified ID.
 - POST /users - Creates a new user with the specified data.
 - PUT /users/<id> - Updates the user with the specified ID with the new data.
 - DELETE /users/<id> - Deletes the user with the specified ID.

-project file structure
 - ├── app.py                
 - ├── requirements.txt      
 - ├── Dockerfile            
 - ├── docker-compose.yml    
 - └── README.md            

