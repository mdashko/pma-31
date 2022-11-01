import uuid

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

current_cat = None
cats = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Tom',
        'age': 2
    }
]

print('Init DB:')
print(cats)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cats', methods=['POST'])
def get_cats():
    return render_template('cats.html', context={'cats': cats, 'current_cat': current_cat})


@socketio.on('POST')
def handle_my_custom_event(json):
    print('Received json for POST: ' + str(json))
    cat = {
        **json,
        'id': str(uuid.uuid4())
    }
    cats.append(cat)
    print(cats)


@socketio.on('GET')
def handle_my_custom_event(json):
    global current_cat
    print('Received json for GET: ' + str(json))

    for cat in cats:
        if cat['id'] == json['id']:
            current_cat = cat
            print("Cat found:")
            print(cat)

@socketio.on('DELETE')
def handle_my_custom_event(json):
    print('Received json for DELETE: ' + str(json))

    for idx, cat in enumerate(cats):
        if cat['id'] == json['id']:
            del cats[idx]
            print("Cat deleted!")


@socketio.on('PUT')
def handle_my_custom_event(json):
    print('Received json for PUT: ' + str(json))

    for cat in cats:
        if cat['id'] == json['id']:
            cat['name'] = json['name']
            print("Cat updated!")


if __name__ == '__main__':
    socketio.run(app)
