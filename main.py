from flask import Flask
from app import views
from flask import render_template,request

deepfakeapp = Flask(__name__) # webserver gatewar interface wsgi

deepfakeapp.add_url_rule(rule="/",endpoint='home',view_func= views.index,methods=['GET','POST'])


'''
deepfakeapp.add_url_rule(rule="/app/",endpoint='app',view_func= views.app,)
deepfakeapp.add_url_rule(rule="/app/gender/",endpoint='gender',view_func= views.genderapp,
                 methods=['GET','POST'])


@deepfakeapp.route('/show_message')
def show_message():
    # Some backend logic
    message_to_show = "This is a message from the backend!"
    return render_template('index.html', message=message_to_show)

@deepfakeapp.route('/no_message')
def no_message():
    # No message to show
    return render_template('index.html', message=None)

'''

if __name__ =="__main__":
    deepfakeapp.run(debug=True)

