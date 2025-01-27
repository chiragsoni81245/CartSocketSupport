from flask import Flask
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app,cors_allowed_origins="*")

from app import routes

if __name__ == '__main__':
    socketio.run(app)