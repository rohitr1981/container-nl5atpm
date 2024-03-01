from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Handle incoming messages and provide responses
    data = request.json
    message = data['message']
    # Process message and generate response (replace this with your chatbot logic)
    response = "This is a response from the Flask chatbot!"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
