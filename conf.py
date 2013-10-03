# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://posativ.org//conf.py.html

import subprocess

TITLE = ('Erebus', 'Consulting')

SITENAME = '(ab)Using technology to solve real-world problems'
WWW_ROOT = 'http://www.erebus-consulting.com/'

AUTHOR = 'Christopher Liljenstolpe'
EMAIL = 'blog@erebus-consulting.com'

DEPLOY_DIR = 's3://www.erebus-consulting.com'

STATIC = [ 'assets' ]
STATIC_FILTER += ['Jinja2']

CONTENT_EXTENSION = '.md'
LANG = 'en'
DATE_FORMAT = '%Y-%m-%d, %H.%M'
strptime = '%Y-%m-%d, %H.%M'

# Added to be able to include the git commit code in the base.html file in shadowplay

GIT_COMMIT_SHORT = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
GIT_COMMIT = subprocess.check_output(['git', 'rev-parse', 'HEAD'])

FILTERS = ['markdown+codehilite(css_class=highlight)', 'hyphenate', 'h1']
VIEWS = {
    '/': {'filters': 'summarize', 'view': 'index',
          'pagination': '/page/:num/'},

    '/:year/:slug/': {'view': 'entry'},

    '/tag/:name/': {'filters': 'summarize', 'view':'tag',
                    'pagination': '/tag/:name/:num/'},

    '/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
    '/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},

    '/:slug/': {'view': 'page'},  # static pages
    '/articles/': {'view': 'articles'},
    '/sitemap.xml': {'view': 'sitemap'},

}

THEME = 'shadowplay'
ENGINE = 'acrylamid.templates.jinja2.Environment'

DISQUS_SHORTNAME = 'erebusconsulting'

DEFAULT_ORPHANS = 3

# Tuples are (name, link)
#BLOGROLL = [
    #('Some of my photographs', 'http://gallery.liljenstolpe.org/')
#]

SOCIAL = [
    ('Linkedin', 'http://www.linkedin.com/in/liljenstolpe', '/img/linkedin.png'),
]
    
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_START_INDEX = 0
TAG_CLOUD_SHUFFLE = True

DEPLOYMENT = {
    "ls": "ls $OUTPUT_DIR",
    "echo": "echo '$OUTPUT_DIR'",
    "default": "s3cmd sync --delete-removed $OUTPUT_DIR/ $DEPLOY_DIR"
}
