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

PROFILE_NAME = "shima"
PROFILE_IMAGE_URL = "https://ui-avatars.com/api/?name=shima&background=f97316&color=fff&size=128"
PROFILE_BIO_LINES = (
    "個人サイトのリニューアルを進めています。",
    "開発メモと制作記録を順次公開予定です。",
)
PROFILE_SOCIAL_LINKS = (
    ("GitHub", "https://github.com/shima10-x1p", "github"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# STATIC_PATHS
STATIC_PATHS = ["extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}
