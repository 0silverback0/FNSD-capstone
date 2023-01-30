# FNSD-capstone

## Description
-This project is the capstone to Udacity's Fullstack NanoDegree. It's a basic API that demonstrates 
user authentication and authorization. This fitness style API Allow coaches to sign up create clients and workouts and assign those workouts to clients. Clients also have the ability to create workouts, and clients can be assigned a trainer.

-This will be a project to continues to grow as I can see this as being a useful tool, as the project grows.
Expansion of the database will eventually allow for images, video links, more detailed explinations, and search.

## Run Locally
- To run locally I recommend createing a virtual environment by running `python -m venv venv` in root directory
- Start your virtual environment 
- Next run `pip install -r requirements.txt`
- Set your environment variables. This app uses python-dotenv and a .env file
- Finally run `flask run`
  
## Tech Stack
- Python
- Flask
- Postgresql
- Auth0

## Roles
- Currently there is two roles. Coach, and Client. Where Coach has permissions to access all end points
- Coach Permissions
    - `get:trainers` Get all trainers/coaches
    - `post:trainer` Create a new trainer/coach
    - `get:client` Get all clients
    - `post:client` Create a new client
    - `post:workouts` Create new workout
    - `patch:workouts` Edit workouts
    - `delete:workouts` Delete workouts

- Client Permisssions
    - `get:trainers` Get all trainers/coaches
    - `post:workouts` Create new workout
    - `patch:workouts` Edit workouts

## Endpoints
- `get:trainers` returns an array of all trainers
  ```
    {
    "success": true,
    "trainers": [
        "coach Mike",
        "coach John",
        "coach Nancy",
        "Ellen"
    ]
    }
  ```

-  `post:trainers` returns new trainer
  ```
    {
    "success": true,
    "trainer": [
        "coach Annie"
    ]
    }
  ```

- `get:clients` returns an array of all clients
  ```
    {
    "success": true,
    "clients": [
        "Jess",
        "Megan",
        "Julia",
        "Joe"
    ]
    }
  ```
- `post:clients` returns new client
  ```
    {
    "success": true,
    "client": [
        "Darron G"
    ]
    }
  ```
-  `post:workouts` returns an array of exercises
  ```
    {
    "success": true,
    "workout": [
        "squats",
        "deadlifts",
        "pull-ups"
    ]
    }
  ```
-  `patch:workouts` returns edited workout array
  ```
    {
    "success": true,
    "workout": [
        "squats",
        "romanian deadlifts",
        "pull-ups"
    ]
    }

  ```

- `delete:workouts` returns message of deleted workout
  
  ```

    {
    "success": true,
    "workout": "workout id: 3 deleted" 
    }

  ```
## Testing
- In the root folder there is a test_capstone.py file with test for the endpoints.
to run the test in your console type `python3 test_capstone.py`

## Render.io Link
- `https://capstone-0njs.onrender.com/`