#!/usr/bin/env python3
"""Modify get locale function"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """configures class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Check if the 'locale' parameter is present in the request"""
 requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    if g.user and 'locale' in g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    request_header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if request_header_locale:
        return request_header_locale
    return app.config['BABEL_DEFAULT_LOCALE']

def get_user(user_id):
    """defines get user info"""
    return users.get(user_id)


@app.before_request
def before_request():
    """defines starting request"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route('/')
def index():
    """defines index"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
