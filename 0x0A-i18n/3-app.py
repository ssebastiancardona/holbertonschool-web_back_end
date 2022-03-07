#!/usr/bin/env python3
"""Aplicación Flask para traducir i18n
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config ():
    """configurar el idioma de la aplicación
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)


babel = Babel(app)


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """localizar el idioma y la zona horaria de la aplicación
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """página de inicio de la aplicación del matraz
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
