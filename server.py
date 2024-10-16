from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print(data)  # Here you can save data to a file or database
    return jsonify({"message": "Data received!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

