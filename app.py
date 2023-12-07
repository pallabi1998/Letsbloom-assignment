from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection Configuration
client = MongoClient("mongodb://127.0.0.1:27017")
db = client['library']

collection = db['books']
#print(list(collection.find()))
# [Endpoints]
# GET: Retrieve All Books
@app.route('/api/books', methods=['GET'])
def get_books():
    try:
        books = list(collection.find())
        return jsonify(books), 200
    except Exception as e:
        return "Error retrieving books from the database.", 500

# POST: Add a New Book
@app.route('/api/books', methods=['POST'])
def add_book():
    try:
        new_book = {
            'title': request.json['title'],
            'author': request.json['author'],
            'isbn': request.json['isbn']
        }
        result = collection.insert_one(new_book)
        #print('inserting done')
        return jsonify(new_book), 201
    except Exception as e:
        return "Error adding the book to the database.", 500

# PUT: Update Book Details
@app.route('/api/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        updated_book = {
            'title': request.json['title'],
            'author': request.json['author'],
            'isbn': request.json['isbn']
        }
        result = collection.update_one({'_id': book_id}, {'$set': updated_book})
        if result.matched_count == 0:
            return "The book with the given ID was not found.", 404
        return jsonify(updated_book), 200
    except Exception as e:
        return "Error updating the book.", 500

# Error Handling
@app.errorhandler(500)
def internal_error(error):
    return "Something failed.", 500

# Server Configuration
if __name__ == '__main__':
    app.run(debug=True)
