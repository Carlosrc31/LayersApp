from flask import Flask
from grocery.controller import handler
from grocery.controller import hello

app = Flask(__name__)

#app.register_blueprint(blueprint)
app.register_blueprint(hello.blueprint)
app.register_blueprint(handler.blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)