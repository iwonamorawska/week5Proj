from flask import Blueprint, render_template

blog= Blueprint('blog',__name__, template_folder="blog_templates")
@blog.route('/blog/main')
def blogHome():
    return render_template('blog.html')
