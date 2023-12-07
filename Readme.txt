
API Details
=====================================

Introduction
------------
This report provides detailed instructions on setting up and running the API locally. 
The API is built with Flask and MongoDB, and allows for CRUD operations on books.
Setting Up the Project
-----------------------

1. Project Setup:
   - Create a new directory for the project.
   - Start the mongodb server by running 'sudo systemctl start mongod'.
   - Install necessary packages: flask, pymongo by running `pip install flask pymongo`.

Database Setup
--------------
1. MongoDB Configuration:
   - Ensure MongoDB is running on your local machine. By default, MongoDB listens on `localhost:27017`.
   - If using a remote MongoDB instance, note down the connection string.

2. Database Schema:
   - The project uses a simple schema for books, with fields for `title`, `author`, and `isbn`.

Running the Application
-----------------------
1. Start the Server:
   - Run the command `python app.py` from the root directory of your project.
   - The server will start, and you can access the API endpoints at `http://localhost:5000/api/books`.

API Endpoints and Usage
-----------------------
Used Use tool cURL to test API endpoints
1. **GET `/api/books`**:
   - Retrieves a list of all books in the library.
   - No request parameters are needed.
   
   example, curl -X GET http://localhost:5000/api/books
	
2. **POST `/api/books`**:
   - Adds a new book to the library.
   - Requires a JSON body with `title`, `author`, and `isbn`.
   
   example, curl -X POST -H "Content-Type: application/json" -d '{
    "title": "The Speckled Band",
    "author": "Sir Arthur Conan Doyle",
    "isbn": "1-86092-003-9"
}' http://localhost:5000/api/books

3. **PUT `/api/books/:id`**:
   - Updates the details of a specific book.
   - Requires the book's ID in the URL and a JSON body with updated `title`, `author`, and/or `isbn`.
   
   example, curl -X PUT -H "Content-Type: application/json" -d '{
    "title": "Updated Book Title",
    "author": "Updated Author",
    "isbn": "Updated ISBN"
}' http://localhost:5000/api/books/{book_id}

