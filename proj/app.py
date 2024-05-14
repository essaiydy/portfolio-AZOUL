from flask import Flask, render_template, url_for, request, send_from_directory, redirect, g, session
from models import storage
from models.user import User
import os
import requests
from uuid import uuid4
from __init__ import UPLOAD_FOLDER, SITUATION, LEVEL, DISEASES, JOBS, allowed_file, DEFAULT_IMG, INFO, ALL_INFO, COUNTRIES

app = Flask(__name__)

app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session.pop('user', None)
        
        password = request.form.get('pass')
        email = request.form.get('email')
        if storage.login(email) and storage.login(email)['psw'] != password:
            return render_template('main.html', email='true', password='false')
        elif storage.login(email) and storage.login(email)['psw']  == password:
            session['user'] = email
            return redirect(url_for('global_page', uname=email.split("@")[0], id=storage.login(email)['id']))

        else:
            return render_template('main.html', email='false', password='false')
    else:
        # adde this condition
        #if g.user:
        #    return redirect(url_for('global_page', uname='.'.join(storage.login(g.user)['name'].split(' ')), id=storage.login(g.user)['id']))
        return render_template('main.html', email='', password='')

    
@app.route('/users/<uname>/<id>')
def global_page(uname, id):
    # adding the condition g.user == storage.usr(id)['email'] befor was just if g.user
    if g.user == storage.usr(id)['email']:
        return render_template('globalpage.html', users=storage.all(), id=id, path=UPLOAD_FOLDER)
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html',
                               list=COUNTRIES,
                               situations=SITUATION,
                               diseases=DISEASES,
                               levels=LEVEL,
                               jobs=JOBS)
    else:
        uname = request.form.get('uname')
        password = request.form.get('pass')
        email = request.form.get('email')
        gender = request.form.get('gender')
        level = request.form.get('level')
        job = request.form.get('job')
        country = request.form.get('country')
        age = request.form.get('age')
        weight = request.form.get('w')
        height = request.form.get('h')
        situation = request.form.get('situ')
        diseases = request.form.get('dis')
        file = request.files['file']
        if storage.login(email):
            return render_template('signup.html', email='false', msg='Account exist with this email !')
        if file.filename == '':
            filename = DEFAULT_IMG
        if file:
            filename = str(uuid4())
            file.save(os.path.join('./static/uploads/users_profile', filename))
        usr = User(name=uname, email=email,
                         password=password,
                         gender=gender,
                         level=level,
                         job=job,
                         country=country,
                         age=age,
                         weight=weight,
                         height=height,
                         situation=situation,
                         diseases=diseases,
                         img=filename)
        storage.add(usr)
        return redirect(url_for('global_page', uname=email.split('@')[0], id=storage.login(email)['id']))

@app.route("/profiles/<id>", methods=["GET", "POST"])
def profile(id):
    if request.method == "GET" and g.user:
        info = storage.all()[id]
        # added
        id_Online = storage.login(g.user)['id']
        name = storage.login(g.user)['name']
        if session['user'] != info['email']:
            return render_template('user.html', info=info, msg=True, path=UPLOAD_FOLDER, id=id_Online, name=name)
        return render_template('user.html', info=info, msg=False, path=UPLOAD_FOLDER, id=id_Online, name=name)
    # if request.method == "POST" and g.user:
    #     return redirect(url_for('settings', id))
    return redirect(url_for('home'))

# SETTING METHOD TO ADD
@app.route('/<id>/settings', methods=['GET', 'POST'])
def settings(id):
    updated_data = {}
    print(id)
    info = storage.all()[str(id)]
    updated_data['email'] = info['email']
    if g.user == storage.usr(id)['email']:

        if request.method == "GET" and g.user:
            return render_template('settings.html', info=info, all_inf=ALL_INFO, path=UPLOAD_FOLDER)

        if request.method == "POST":
            name = request.form.get('name')
            age = request.form.get('age')
            gender = request.form.get('gender')
            country = request.form.get('country')
            level = request.form.get('level')
            job = request.form.get('job')
            weight = request.form.get('weight')
            height = request.form.get('height')
            situation = request.form.get('situation')
            disease = request.form.get('disease')
            file = request.files['file']
            if file.filename == '':
                img = DEFAULT_IMG
            if file:
                img = str(uuid4())
                file.save(os.path.join('./static/uploads/users_profile', img))
            
            for inf in INFO:
                if eval(inf):
                    if eval(inf) == DEFAULT_IMG:
                        pass
                    else:
                        updated_data[inf] = eval(inf)
            storage.settings(id, updated_data)
            return render_template('user.html', info=info, msg=False)
    return redirect(url_for('home'))

@app.route('/api/informations')
def api():
    return ALL_INFO

@app.before_request
def before_request():
    g.user = None
    
    if 'user' in session:
        g.user = session['user']
        print(g.user)
        
@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('main.html', email='', password='')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(os.path.join(app.root_path, 'static'), path)

if __name__ == '__main__':
    app.run(debug=True)