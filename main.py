from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/app/data/all', methods=['GET'])
def get_data():
    
    data = {
        'name': "Alok",
        'age': 21
    }

    return jsonify(data)
@app.route('/app/data/', methods=['GET'])
def get_dataa():
    
    data = {
        'name': "Alok"
    }

    return jsonify(data)

@app.route('/app/post/data', methods=['POST'])
def post_data():
    data = request.get_json()

    name = data['name']
    age = data['age']

    result = f"Hello, {name}! Your age is {age}."

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
