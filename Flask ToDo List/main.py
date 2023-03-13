from flask import Flask
from routes import todo_list_bp

app = Flask(__name__)

app.register_blueprint(todo_list_bp, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)
