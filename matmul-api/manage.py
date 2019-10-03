import os
import unittest

from flask_cors import CORS
from flask_script import Manager

from api import create_app
from api.blueprint import blueprint

app = create_app(os.getenv('PYTHON_ENV') or 'dev')
app.register_blueprint(blueprint)

manager = Manager(app)

CORS(app, resorces={r'/d/*': {"origins": '*'}})


@manager.command
def run():
    app.run(host='0.0.0.0', port=8000)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('.')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
