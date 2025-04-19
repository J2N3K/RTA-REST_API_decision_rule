from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get("name")
    if name:
        return jsonify({"message": f"Hello {name}!"})
    return jsonify({"message": "Hello!"})

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        
        result = 1 if (num1 + num2) > 5.8 else 0
        
        return jsonify({
            "prediction": result,
            "features": {
                "num1": num1,
                "num2": num2
            }
        })
    except (TypeError, ValueError):
        return jsonify({"error": "Niepoprawne dane. Upewnij się, że podałeś num1 i num2 jako liczby."}), 400

if __name__ == '__main__':
    app.run()
