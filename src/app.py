from flask import Flask, jsonify
from flask import request
app=Flask(__name__)

todos= [{"label": "My first task", "done":False}, { "label": "My second task", "done": False }]

  
@app.route('/todos', methods=['GET'])
def hello_world():
    #return "<h1>Hello!</h1>"
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body) 
    print("Incoming request with the following body", request_body)
    return jsonify(todos)



@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print (todos)
    print(position)
    if position < len(todos) and position >= 0:
        todos.pop(position)
        return 'Todo eliminado con éxito', 200
    
    else:
        return f'Error al eliminar todo en la posición {position}', 400





if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3245, debug=True)