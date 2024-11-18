from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


# GET /getcookies - Retrieve cookies
@app.route('/getcookies', methods=['GET'])
def get_cookies():
    # Get the cookie from the request
    user_cookie = request.cookies.get('username')

    if user_cookie:
        return f'Cookie value: {user_cookie}'
    else:
        return 'No cookies found!'


# POST /setcookies - Set a cookie
@app.route('/setcookies', methods=['POST'])
def set_cookies():
    # Get data from the POST request (here we're looking for 'username' key in JSON body)
    user_name = request.json.get('username')

    if user_name:
        resp = make_response(jsonify(message=f'Cookie set for {user_name}!'))

        # Set the cookie in the response
        resp.set_cookie('username', user_name)

        return resp
    else:
        return jsonify(message='No username provided!'), 400


if __name__ == '__main__':
    app.run(debug=True)