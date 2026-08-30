from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Profile: replace the values in this block with your own information.
AUTHOR = "しま"
SITENAME = "shima10-x1p.net"
SITE_DESCRIPTION = "雑記"
SITESUBTITLE = SITE_DESCRIPTION
COPYRIGHT_YEAR = 2026
PROFILE_EYEBROW = ""
PROFILE_TAGLINE = (
    "暇なときに、勉強がてら色々やります。"
)
PROFILE_SHORT_BIO = (
    "暇なときに、勉強がてら色々やります。"
)
PROFILE_AVATAR_URL = "https://avatars.githubusercontent.com/u/57385580?v=4"
PROFILE_ROLE = "しがないソフトウェアエンジニア"
PROFILE_LOCATION = "日本 / 千葉"
PROFILE_INTERESTS = "Python, にじさんじ"
# About page: add, remove, or reorder items to customize the displayed tags.
ABOUT_INTERESTS = (
    "Python",
    "周央サンゴ",
    "家長むぎ"
)
SOCIAL = (
    ("GitHub", "https://github.com/shima10-x1p"),
    ("Twitter", "https://twitter.com/shima10_x1p"),
)

PATH = "content"
OUTPUT_PATH = "output"
THEME = str(BASE_DIR / "theme")
PLUGIN_PATHS = [str(BASE_DIR / "plugins")]

TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"
DEFAULT_DATE_FORMAT = "%Y年%-m月%-d日"

ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

DIRECT_TEMPLATES = ["index", "archives"]
ARCHIVES_URL = "blog/"
ARCHIVES_SAVE_AS = "blog/index.html"

# The site intentionally has no category, tag, or author archive pages.
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

STATIC_PATHS = ["extra", "images"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

FEED_ALL_RSS = "feeds/all.rss.xml"
FEED_DOMAIN = "http://localhost:8000"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "guess_lang": False,
            "linenums": True,
        },
        "plugins.code_language": {},
    },
    "output_format": "html5",
}

DEFAULT_PAGINATION = False
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
