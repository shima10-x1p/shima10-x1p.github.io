AUTHOR = 'しま（shima10-x1p）'
SITENAME = '夏島諸島'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'Japanese'

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
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
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
