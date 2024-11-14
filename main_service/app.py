from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def create_email():
    data = request.get_json()
    get_emails(data)
    print(data)
    if not data:
        return jsonify({'error': 'No data'}), 400
    return jsonify({'data':'ok'}), 200




if __name__ == "__main__":
    app.run(debug=True)