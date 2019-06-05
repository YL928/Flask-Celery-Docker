from flask_script import Server, Manager
from app import create_app, DefaultConfig

manager = Manager(create_app)
manager.add_command("runserver", Server(host=DefaultConfig.HOST, port=DefaultConfig.PORT))
if __name__ == "__main__":
    manager.run()