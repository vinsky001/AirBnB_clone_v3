#!/usr/bin/python3

from models import storage
from api.v1.views import app_views

# Create a Flask application instance
app = Flask(__name__)
app.register_Blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_storage(error=none):
    """ calls storage.close()"""
    return storage.close()

if __name__ == "__main__":
    if getenv('HBNB_API_HOST') and port('HBNB_API_PORT')
        app.run(host=getenv('HBNB_API_HOST'),
            port=int(getenv('HBNB_API_PORT')), threaded=True

    else:
        app.run(host='0.0.0.0', port=500, threaded=True)
