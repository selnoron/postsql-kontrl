# Flask
from flask import (
    Flask,
    Request,
    request,
    redirect,
    Response,
    render_template
)
from flask.app import Flask as FlaskApp

# Local
from models.settings import *
from models.DB import *

app: FlaskApp = Flask(__name__)
now_user: dict = {
    'id': '',
    'login': '',
    'full_name': '',
    'author': '',
    'author_id': ''
}


@app.route('/auth', methods=['GET', 'POST'])
def auth_page():
    if request.method == 'POST':
        log: str = request.form.get('login')
        pas: str = request.form.get('password')
        if auth_user(log, pas) == 0:
            data = get_users_data(log)
            now_user['id'] = data[0]
            now_user['login'] = data[1]
            now_user['full_name'] = data[2]
            now_user['author'] = data[3]
            now_user['author_id'] = data[4]
            print(now_user)
            return redirect('/main')
        return render_template(
            'auth.html'
        )
    return render_template(
        'auth.html'
    )

@app.route('/', methods=['GET', 'POST'])
def reg_page():
    if request.method == 'POST':
        temp_log: str = request.form.get('login')
        temp_password: str = request.form.get('password')
        temp_full_name: str = request.form.get('full_name')
        temp_author: int = int(request.form.get('author'))
        insert_user(temp_log, temp_full_name, temp_password, temp_author)
        return redirect('/auth')
    
    return render_template(
        'red.html'
    )

@app.route('/main', methods=['GET', 'POST'])
def main_page():
    arts = [info for info in get_all_artcs()]
    sred = [DB.get_rate_of_art(i+1) for i in range(len(get_all_artcs()))]
    for i in range(len(get_all_artcs())):
        arts[i].append(sred[i])
    print(arts)
    return render_template(
        'index.html',
        artcs=arts
    )

@app.route('/create', methods=['GET', 'POST'])
def create_page():
    if now_user.get('author') == 2:
        return "<h1> you dont have author's rights</h1>"
    if request.method == 'POST':
        temp_title: str = request.form.get('title')
        temp_text: str = request.form.get('text')
        temp_auth_id: int = now_user.get('author_id')
        insert_article(temp_title, temp_text, temp_auth_id)
        return redirect('/main')
    
    return render_template(
        'create.html'
    )

@app.route('/comment/<int:id>', methods=['GET', 'POST'])
def comment_page(id: int):
    if request.method == 'POST':
        temp_rate: str = request.form.get('rate')
        temp_text: str = request.form.get('text')
        temp_user_id: int = now_user.get('id')
        temp_artcs_id: int = id
        insert_rate(temp_rate, temp_text, temp_user_id, temp_artcs_id)
        return redirect('/main')
    comes = []
    res = []
    for i in get_all_comments():
        res = []
        if i[1] == id:
            for j in i:
                res.append(j)
        if res:
            comes.append(res)
    print(comes)
    return render_template(
        'comment.html',
        coms=comes
    )


if __name__ == '__main__':
    DB.create()
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )