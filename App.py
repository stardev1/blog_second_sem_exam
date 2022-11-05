from flask import Flask, request, render_template, redirect
from functions.forms import NewUserForm, Login, CreateBlog
from models.user import User
from models.post import Post
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'dcd7df0c-ab14-4dcb-9dd9-1fff9f6aca8a'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def index():
    posts = Post.all()
    return render_template('index.html', user=current_user, posts=posts)

@app.route('/blog/<id>', methods=['GET','POST'])
def blog(id):
    post = Post.get(id)
    return render_template('blog.html', post=post, user=current_user)

@app.route('/create_blog', methods=['GET','POST'])
@login_required
def create_blog():
    form = CreateBlog()
    if request.method == 'POST' and form.validate_on_submit():
        title, content, _ = form
        post = Post(title=title.data, content=content.data, author_id=current_user.id)
        post.save()
        return redirect('/blog/' + post.id)
    return render_template('create_blog.html', form=form, user=current_user)

@app.route('/edit_blog/<id>', methods=['GET','POST'])
@login_required
def edit_blog(id):
    post = Post.get(id)
    if post.author_id != current_user.id:
        return redirect('/blog/' + post.id)
    form = CreateBlog(obj=post)
    if request.method == 'POST' and form.validate_on_submit():
        title, content, _ = form
        if post.author_id == current_user.id:
            post.update(title=title.data, content=content.data)
        return redirect('/blog/' + post.id)
    return render_template('edit_blog.html', form=form, user=current_user, post=post)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if request.method == 'POST' and form.validate_on_submit():
        email, password, _ = form
        user = User.where(email=email.data)
        if user is not None:
            if check_password_hash(user.password, password.data):
                login_user(user)
                return redirect('/')
    return render_template('Auth/login.html', form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    """
        function to register new user and
        and to show register view
    """
    form = NewUserForm()
    if request.method == 'POST' and form.validate_on_submit():
        name, email, password, confirm, _ = form
  
        passhashed = generate_password_hash(password.data)
        user = User(name=name.data, email=email.data, password=passhashed)
        user.save()
        login_user(user)
        return redirect('/')

    else:
        return render_template('Auth/register.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/logout', methods=['GET', "POST"])
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")