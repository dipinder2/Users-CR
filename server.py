from flask import Flask, render_template, redirect, request
app = Flask(__name__)
from users import User

@app.route('/')
def index():
    result = User.get_all_users()
    return render_template('index.html', users = result)

@app.route('/users')
def form_users():
    return render_template('users.html')


@app.route('/create-user',methods=['GET','POST'])
def create_user():
    req = request.form
    User.add_user(req)
    return redirect('/')




if __name__ == '__main__':
  app.run(debug=True)
 