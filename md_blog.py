# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
from md_blog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)