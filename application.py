from flask import Flask, render_template, url_for

application = Flask(__name__)


@application.route('/')
def hello_world():
    return render_template('%s.html' % 'index')

@application.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@application.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)


if __name__ == '__main__':
    application.run()
    #application.run(host='0.0.0.0', port=80)
