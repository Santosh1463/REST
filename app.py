from flask import Flask, request

app = Flask(__name__)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json
        user_id = "Santosh_14062003"
        email = "sv7618@srmist.edu.in"
        roll_number = "RA2011003020208"
        numbers = data['numbers']
        alphabets = data['alphabets']
        highest_alphabet = max(alphabets, key=lambda x: x.upper())

        response = {
            'is_success': True,
            'user_id': user_id,
            'email': email,
            'roll_number': roll_number,
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_alphabet': highest_alphabet,
        }

        return response, 200

    else:
        response = {
            'operation_code': 1
        }

        return response, 200

if __name__ == '__main__':
    app.run(debug=True)
