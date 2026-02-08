AUTHOR = 'しま(shima10-x1p)'
SITENAME = 'しま'
SITEURL = ""
RELATIVE_URLS = True

PATH = "content"
THEME = "themes/shima-island"
ARTICLE_PATHS = ["articles"]

ARTICLE_URL = "articles/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "articles/{date:%Y}/{date:%m}/{slug}/index.html"

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
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

PROFILE_NAME = "しま"
PROFILE_IMAGE_URL = "https://avatars.githubusercontent.com/u/57385580?v=4"
PROFILE_BIO_LINES = (
    "メモを残します。",
)
PROFILE_SOCIAL_LINKS = (
    ("GitHub", "https://github.com/shima10-x1p", "github"),
    ("Twitter", "https://x.com/shima10_x1p", "twitter"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# STATIC_PATHS
STATIC_PATHS = ["extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}
