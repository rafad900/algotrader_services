from flask import Flask, request, jsonify

app = Flask(__name__)

shared_variable = {"count": 0}
data = {"tradingview_data": []}
@app.route('/test', methods=['GET'])
def get_webhook():
    response = shared_variable["count"]
    last_reponse = data["tradingview_data"]
    print(f"Received webhook data: {last_reponse}")
    return jsonify(last_reponse)

@app.route('/', methods=['GET'])
def get_data():
    # Listen the port 
    # Create a sample JSON response
    response = {
        "message": "Hello, Victor!",
        "status": "success",
        "data": {
            "user": "victor",
            "age": 30,
            "location": "Davis, CA"
        }
    }
    return jsonify(response)


# Correct use of 'methods' (plural)
@app.route('/webhook', methods=['POST'])
def receive_webhook():
    try:
        shared_variable["count"] += 1
        # Get JSON data sent from the webhook
        data["tradingview_data"].append(request.json)
        # print(f"Received webhook data: {data["tradingview_data"][-1]}")

        # Example: Respond with success
        return jsonify({"status": "success", "message": "Webhook received!"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    # Ensure the Flask server runs properly
    app.run(host='0.0.0.0', port=5001)


# Test
# curl -X POST http://localhost:5001/webhook -H "Content-Type: application/json" -d '{"message": "Hello"}'
