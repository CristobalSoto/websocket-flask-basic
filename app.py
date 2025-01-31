from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# WebSocket event handler for receiving messages from the client
@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    emit('response', {'data': 'Message received: ' + msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
