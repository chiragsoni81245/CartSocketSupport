from flask import Flask
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="http://localhost:3000")

from app import routes, models

if __name__ == '__main__':
    socketio.run(app)