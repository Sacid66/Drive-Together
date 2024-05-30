from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('draw_event')
def handle_draw_event(json):
    emit('broadcast_draw', json, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
