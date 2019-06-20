from flask import render_template, request, Blueprint
from flaskapp.models import Post, User
from flask_login import current_user

main = Blueprint('main', __name__)

#main page
@main.route("/")
def home():
	page = request.args.get('page', 1,type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
	return render_template('home.html',posts=posts)

#about page
@main.route('/about')
def about():
	return render_template('about.html',title='About')

