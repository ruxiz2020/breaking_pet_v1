from flask import Flask, render_template
from flask_moment import Moment
from flask_cors import CORS

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
CORS(app)
moment = Moment(app)
#app.config.from_object(Config)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
#ckeditor = CKEditor(app)

@app.route('/')
def index():
    return render_template('pages/home.html')


# Default port:
if __name__ == '__main__':
    app.run(port=5051, debug=True)
