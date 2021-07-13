from flask import Flask

# blueprint import
from blueprints.functions.functions import functions


def create_app(app):
    # register blueprint
    app.register_blueprint(functions)

    return app


if __name__ == "__main__":
    app = Flask(__name__)
    create_app(app).run(host="0.0.0.0", debug=True, port=7979)
