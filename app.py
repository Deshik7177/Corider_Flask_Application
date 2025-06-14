from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='testing_mongodb',
                         port=27017,
                         username='root',
                         password='pass',
                         authSource='admin')
    db = client["details_db"]
    return db

@app.route('/')
def check_flask():
    return "Flask Backend Working"

# GET/users to return list of all the users
@app.route('/users', methods=['GET'])
def fetch_users():
    db = get_db()
    _users = db.users.find()
    users = [{"id": str(user["id"]), "name": user["name"], "email": user["email"], "password": user["password"]} 
             for user in _users
             ]
    return jsonify({"users": users})

#GET/users/<id> to return user with specified ID
@app.route('/users/<string:user_id>', methods=['GET'])
def fetch_user_byid(user_id):
    db = get_db()
    user = db.users.find_one({'id': user_id})
    return jsonify({
        'id': str(user['id']),
        'name': user['name'],
        'email': user['email'],
        'password': user["password"]
    })

#POST /users to create a new user
@app.route('/users', methods=['POST'])
def user_create():
    db = get_db()
    data = request.get_json()
    new_user ={
        "id": data["id"],
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }
    db.users.insert_one(new_user) 
    return jsonify({'message': 'user created successfully', 'id': data["id"]})

# PUT /users/<id> Updates the user with the specified ID with the new data.
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    db = get_db()
    data = request.get_json()
    update_result = db.users.update_one(
        {"id": id},
        {"$set": data}
    )
    if update_result.matched_count == 0:
        return jsonify({"error": "no user with the id"})
    
    return jsonify({'message': 'User updated successfully'})

# DELETE /users/<id> Deletes the user with the specified ID.
@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    db = get_db()
    delete_result = db.users.delete_one({"id": id})
    if delete_result.deleted_count == 0:
        return jsonify({"no user to delete"})
    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
