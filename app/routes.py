from app import app,socketio,emit
from flask import render_template, request

active_sessions = set()

@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
	sid = request.sid
	print("\n\nAdded {}\n\n".format(sid))
	active_sessions.add(sid)
	print(active_sessions)
	emit('message', {'data': 'Connected'})



@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	sid = request.sid
	print("\n\nRemoved {}\n\n".format(sid))
	active_sessions.remove(sid)
	print(active_sessions)
	print('Client disconnected')


@socketio.on('updateData', namespace='/test')
def test_disconnect(json):
	print(json)
	sessions = list(active_sessions)
	for session in sessions:
		emit("updateHandler",{"data": json }, room=session)
