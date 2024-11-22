# Accelerate Learning Project

This is a full-stack web application built with GraphQL, PostgreSQL, and SQLAlchemy. The goal of the project is to manage and track teachers, students, assignments, and scores in a school setting. The app allows users to perform basic CRUD operations through a GraphQL API.

## Features

- **GraphQL API**: Expose CRUD operations for teachers, students, assignments, and scores.
- **PostgreSQL Database**: Store data for teachers, students, assignments, and scores.
- **SQLAlchemy ORM**: Interact with the PostgreSQL database using Python objects.
- **Seed Data**: Populate the database with sample data.
  
## Tech Stack

- **Backend**: Python with FastAPI, SQLAlchemy (for ORM), and GraphQL (via Strawberry or Graphene).
- **Database**: PostgreSQL.
- **API**: GraphQL.
- **ORM**: SQLAlchemy.
- **Other Tools**: Alembic for database migrations, Postman/GraphQL Playground for testing.

## Setup and Installation

### Prerequisites

1. **Python 3.11+**  
   Ensure that you have Python 3.11 or later installed on your machine.
   
2. **PostgreSQL**  
   Make sure PostgreSQL is installed and running on your system. If not, you can install it via [Homebrew (macOS)](https://brew.sh/) or [official installation guide](https://www.postgresql.org/download/).

3. **Virtual Environment**  
   It is recommended to set up a Python virtual environment to manage dependencies.

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/accelerate-learning-project.git
    cd accelerate-learning-project
    ```

2. **Set up the virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For macOS/Linux
    # or
    .\venv\Scripts\activate  # For Windows
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database**:
    - Make sure your PostgreSQL service is running. You can start it using the following command (if you installed via Homebrew on macOS):
      ```bash
      brew services start postgresql@14
      ```

    - Create a new PostgreSQL user and database if not already created:
      ```bash
      psql -U postgres
      CREATE DATABASE accelerate_learning;
      CREATE USER max WITH ENCRYPTED PASSWORD 'password';
      GRANT ALL PRIVILEGES ON DATABASE accelerate_learning TO max;
      \q
      ```

5. **Configure Database URL**:
    Open the `database.py` file and update the `DATABASE_URL` to reflect your PostgreSQL database credentials, e.g.:
    ```python
    DATABASE_URL = "postgresql://max:password@localhost/accelerate_learning"
    ```

6. **Run the migrations (if using Alembic)**:
    ```bash
    alembic upgrade head
    ```

7. **Populate the database with sample data** (optional):
    To populate the database with sample teachers, students, assignments, and scores, run:
    ```bash
    python app/seed_data.py
    ```

8. **Start the server**:
    ```bash
    uvicorn app.main:app --reload  # FastAPI (if using FastAPI)
    # or
    python app/app.py  # If you're using Flask or another framework
    ```

### Testing the API

1. **Using Postman or GraphQL Playground**:  
   Open Postman or any GraphQL IDE (like GraphiQL or Apollo Studio) and send requests to the API.

2. **GraphQL Example Query**:  
   Test querying the teachers:
   ```graphql
   query {
     allTeachers {
       id
       name
       email
     }
   }
