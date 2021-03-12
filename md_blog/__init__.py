# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
from pathlib import Path

from flask import Flask


def create_app():
    app = Flask(__name__, template_folder=Path(__file__).parent.parent / 'resources/templates')

    from md_blog.views import bp
    app.register_blueprint(bp)

    return app

