from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False}, 
     {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    # return '<h1>Hello!</h1>'
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos),201


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if position < len(todos):
        todos.pop(position)
        return jsonify(todos)
    else:
        return "Error: Todo not found", 404




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
