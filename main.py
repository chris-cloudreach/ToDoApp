#!/Users/christopher.ogbunuzor/.pyenv/shims/python
"""
TodoApp will have the following CRUD functionalities:

1. Adding items to a list
2. Getting all items from the list
3. Updating an item in the list
4. Deleting an item from the list
"""
import helper
from flask import Flask, request, Response
import json



app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> WELCOME TO MY TODO APP</h1>"

@app.route("/todolist")
def get_all_items():
    # Get items from the helper
    res_data = helper.get_all_items()

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route("/todolist/status", methods=['GET'])
def get_item():
    # Get parameter from the URL
    item_name = request.args.get('name')

    # Get items from the helper
    status = helper.get_item_status(item_name)

    # Return 404 if item not found
    if status is None:
        response = Response("{'error': 'Item Not Found - %s'}"  % item_name, status=404 , mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response


# def getmovies_id(movieid):
#     return json.dumps(movie_db[movieid])

#create a post api for adding new item to our list
@app.route("/todolist/add", methods=['POST'])
def additem():
    # Get data from json body
    req_data= request.get_json()
    item = req_data['item']

    # Add item to todo list
    res_data = helper.add_to_list(item)

    # Return error if item not added
    # if res_data is None:
    #     response = Response("{'error': 'Item not added - " + item + "'}", status=400 , mimetype='application/json')
    #     return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response
    
@app.route('/todolist/update', methods=['PUT'])
def update_status():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']
    status = req_data['status']

    # Update item in the list
    res_data = helper.update_status(item, status)

    # Return error if the status could not be updated
    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + item + ", " + status   +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@app.route('/todolist/remove', methods=['DELETE'])
def delete_item():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']

    # Delete item from the list
    res_data = helper.delete_item(item)

    # Return error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + item +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

if __name__ == "__main__":
    app.run(host = '127.0.0.1')
