from flask import Flask

def create_app():
    # initializes our app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfgh'

    from views import views

    app.register_blueprint(views, url_prefix='/')

    return app

app = create_app()

if __name__ == '__main__':
    #Run the Flask app, start a web server
    #Debug=True re-runs the web server when we make a change
    app.run(debug=True)