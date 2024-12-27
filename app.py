from flask import Flask, render_template
from flask_socketio import SocketIO
import keyboard
import time

app = Flask(__name__)
socketio = SocketIO(app)

key_mappings = {
    'y': 'y', 'u': 'u', 'i': 'i', 'o': 'o', 'p': 'p',
    'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', ';': ';',
    'n': 'n', 'm': 'm', ',': ',', '.': '.', '/': '/'
}

@socketio.on('keypress')
def handle_keypress(data):
    keys = data.get('keys', [])
    for key in keys:
        key_lower = key.lower()  
        if key_lower in key_mappings:
            keyboard.press(key_mappings[key_lower]) 
            time.sleep(0.1)
            keyboard.release(key_mappings[key_lower])  

    socketio.emit('server_response', {'message': f"Processed keys: {', '.join(keys)}"})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000)
