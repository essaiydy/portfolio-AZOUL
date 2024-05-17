from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, send
import random
from string import ascii_uppercase # for generating random room code

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app)

roomsjson = "rooms.json"

"""onerrooms = {id1:{room1,room2}, id2:{}}#json file
#request.form.get('id')
if room in onerrooms[id1]:
    rederect(room1)
if  rooms[room]["members"] >= 2:
    code = generate_unique_code(4)"""


def generate_unique_code(length):
    while True:
        code = ""
        for _ in range (length):
            code += random.choice(ascii_uppercase)
            
        if code not in rooms:
            break
    return code

        
def deserialise_rooms():
    try:
        with open(roomsjson, "r") as file:
            return eval(file.read())
    except:
        print("Error deserialising rooms")
        return {}
    
rooms = deserialise_rooms()
            
def serialise_rooms(rooms):
    try:
        with open(roomsjson, "w") as file:
            file.write(str(rooms))
    except:
        print("Error serialising rooms")  

@app.route('/', methods=['GET', 'POST'])
def home():
    session.clear() # clear the session
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)
        create = request.form.get('create', False)
        userid = request.form.get('userid', False)
        
        if not name:
            return render_template('home.html', error='print ur name', name=name, code=code, userid=userid)
        
        if join != False and not code:
            return render_template('home.html', error='print the room code', name=name, code=code)
        
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
            rooms[room]["members"] += 1
            rooms[room]["messages"].append({"name": "Server", "message": f"{name} created the room"})
            
            serialise_rooms(rooms)
        elif code not in deserialise_rooms():
            return render_template('home.html', error='room not found')
        
        session["room"] = room # store the room code in the session
        session["name"] = name 
        return redirect(url_for("room"))
        
    return render_template('home.html')

@app.route('/room')
def room():
    room = session.get('room')
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for('home'))
    
    return render_template('room.html', code=room, messages=rooms[room]["messages"])
#side of the server
@socketio.on("message")
def message(data):
    room = session.get('room') # get the room code from the session object to ensure that the user is in a room and has a name
    if room not in rooms:
        return
    
    content = {
        "name": session.get('name'),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")
    

@socketio.on("connect") # when a user connects to the server
def connect(auth):
    room = session.get('room')
    name = session.get('name')
    
    if not room or not name: # to ensure that the user is in a room and has a name and if the user connect before joining a room
        return
    
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "joined the room"}, to=room)
    rooms[room]["members"] += 1 # increment the number of members in the room
    print(f"{name} joined the room {room}")
    


@socketio.on("disconnect")
def disconnect():
    room = session.get('room') # get the room code
    name = session.get('name') # get the name of the user
    leave_room(room)
    
    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
            
    send({"name": name, "message": "left the room"}, to=room)
    print(f"{name} left the room {room}")

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.2', port=5800, debug=True)