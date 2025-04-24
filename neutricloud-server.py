from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = data.get('user')
    password = data.get('password')

    # Simulando conexión sin verificar credenciales
    return jsonify({'success': True, 'message': 'Connection established'})

if __name__ == '__main__':
    app.run(debug=True)
