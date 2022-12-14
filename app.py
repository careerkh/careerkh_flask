import os
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# Give proper 404 message for bad requests
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# test API
@app.route('/', methods=['GET'])
def test_api_1():
    if request.method == 'GET':
        return jsonify({'status_code': 200,
                        'position': 'Back End Developer',
                        'href': '#',
                        'industry': { 'name': 'Information Technology', 'href': '#' },
                        'description': '',
                        'caption': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. ',
                        'term': 'Full-Time',
                        'location': 'Remote',
                        'salary': '500k',
                        'date': 'Jaunary 9, 2022',
                        'imageUrl': 'https://images.unsplash.com/photo-1496128858413-b36217c2ce36?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1679&q=80',
                        })

# test API
@app.route('/api', methods=['GET'])
def test_api_2():
    if request.method == 'GET':
        return jsonify({'status_code': 200, 'message': 'second end point "test2" is called'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5055, debug=False)
