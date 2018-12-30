from flask import Flask, render_template, url_for

application = Flask(__name__)


@application.route('/')
def hello_world():
    return render_template('%s.htm' % 'index')


@application.route('/aboutus')
def aboutus():
    return render_template('about-us.htm')


@application.route('/admin')
def admin():
    return render_template('admin.html')

@application.route('/services')
def services():
    return render_template('services.htm')

@application.route('/contact')
def contact():
    return render_template('contact.htm')

@application.route('/career')
def career():
    return render_template('career.htm')

@application.route('/gallery')
def gallery():
    return render_template('gallery.htm')

@application.route('/index')
def index():
    return render_template('index.htm')

@application.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s' % page_name)


if __name__ == '__main__':
    application.run()
    #application.run(host='0.0.0.0', port=80)
