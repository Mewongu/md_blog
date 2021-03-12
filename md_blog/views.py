# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
from dataclasses import dataclass
from pathlib import Path

import frontmatter
from flask import Blueprint, render_template
from markdown import markdown
from werkzeug.exceptions import abort

bp = Blueprint('main', __name__)

@dataclass
class Article:
    keywords: set
    title: str
    author: str
    url: str
    content: str


article_by_url = {}
for md_file in Path(__file__).parent.parent.glob('resources/*.md'):
    contents = md_file.read_text()
    data, content = frontmatter.parse(contents)

    article = Article(
        title=data['title'],
        author=data['author'],
        url=data['url'],
        keywords=data['keywords'],
        content=markdown(content),
    )
    article_by_url[article.url] = article


@bp.route('/')
def index():
    all_articles = article_by_url.values()
    return render_template('article_list.html', articles=all_articles, title='md_blog')


@bp.route('/<string:url>', methods=['GET'])
def route(url: str):
    article = article_by_url.get(url, None)
    if not article:
        abort(404)
    return render_template('single_article.html', article=article, title=article.title)

