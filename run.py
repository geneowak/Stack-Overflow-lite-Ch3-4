from API.app import app
from API.config import app_config

''' start the app '''
if __name__ == "__main__":
    app.config.from_object(app_config['development'])
    app.run()
