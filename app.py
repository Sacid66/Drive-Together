from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start')
def handle_start(data):
    emit('start', data, broadcast=True)

@socketio.on('draw')
def handle_draw(data):
    emit('draw', data, broadcast=True)

@socketio.on('end')
def handle_end(data):
    emit('end', data, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
