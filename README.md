# ConnectLang

ConnectLang is a language learning partner matching app that allows users to find language exchange partners based on their chosen language, known language, and spoken language.

## Features

- **User Registration:** Users can register with the app by providing their username and language preferences.
- **Search Language Partners:** Find language learning partners based on chosen language, known language, and spoken language.
- **User Profile:** View and update user profiles with language preferences.

## Technologies Used

- **FastAPI:** FastAPI is a modern, fast web framework for building APIs with Python 3.7+.
- **PostgreSQL:** PostgreSQL is used as the database to store user information.
- **SQLAlchemy:** SQLAlchemy is used as the Object-Relational Mapping (ORM) tool for database interactions.
- **databases:** The `databases` library is used for managing database connections asynchronously.
- **uvicorn:** Uvicorn is used as the ASGI server to run the FastAPI application.
- **pandas and numpy:** Optional libraries for data manipulation tasks.

## Getting Started

### Prerequisites

- Python 3.7+
- PostgreSQL installed and running
- FastAPI

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Germain-Adediha/ConnectLang
   ```
   ```bash
   cd connectLang
   ```
2.  Install required packages:
    ```bash
    pip install fastapi[all] uvicorn databases[postgresql] sqlalchemy
    ```
3.  Run the FastAPI app:
    ```bash
    uvicorn main:app --reload
    ```
    The app will be accessible at http://127.0.0.1:8000.


4.  Example looking for user:
    ```bash
    http://127.0.0.1:8000/search_users/?chosen_language=English&known_language=Spanish&spoken_language=French
    ```

# API Documentation
Explore the API endpoints and test them using the Swagger documentation available at: http://127.0.0.1:8000/docs

# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.
