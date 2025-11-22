AUTHOR = 'しま（shima10-x1p）'
SITENAME = '夏島諸島'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/shima10-x1p"),
    ("Twitter", "https://twitter.com/shima10_x1p"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# STATIC_PATHS
STATIC_PATHS = ["extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

THEME = 'theme/natsu-shima'

AUTHOR_BIO = {
    "しま（shima10-x1p）": "PythonとWeb開発が好きなエンジニアです。Pelicanでブログを書いています。"
}

# Content paths
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# URL settings
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Disable Author pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_URL = ''
