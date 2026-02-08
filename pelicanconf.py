from pathlib import Path

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
STATIC_PATHS = ["extra/CNAME", "images"]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

IMAGE_EXTENSIONS = ("webp", "jpg", "jpeg", "png", "avif", "gif")
CONTENT_ROOT = (Path(__file__).resolve().parent / PATH).resolve()


def _normalize_thumbnail_path(raw_value):
    if raw_value is None:
        return None

    value = str(raw_value).strip()
    if not value:
        return None

    if value.startswith(("http://", "https://", "//")):
        return value

    return value.lstrip("/").replace("\\", "/")


def _resolve_named_image(image_dir, stem):
    for ext in IMAGE_EXTENSIONS:
        candidate = image_dir / f"{stem}.{ext}"
        if candidate.is_file():
            return candidate
    return None


def _relative_to_content_root(file_path):
    try:
        return file_path.resolve().relative_to(CONTENT_ROOT).as_posix()
    except ValueError:
        return None


def resolve_article_thumbnail(article):
    metadata = getattr(article, "metadata", {}) or {}
    explicit_thumbnail = (
        metadata.get("thumbnail")
        or metadata.get("Thumbnail")
        or getattr(article, "thumbnail", None)
    )
    normalized_explicit = _normalize_thumbnail_path(explicit_thumbnail)
    if normalized_explicit:
        return normalized_explicit

    date = getattr(article, "date", None)
    slug = getattr(article, "slug", None)
    if not date or not slug:
        return None

    image_dir_rel = Path("images") / date.strftime("%Y") / date.strftime("%m") / str(slug)
    image_dir = CONTENT_ROOT / image_dir_rel
    if not image_dir.is_dir():
        return None

    for stem in ("thumbnail", "cover"):
        named_candidate = _resolve_named_image(image_dir, stem)
        if named_candidate:
            return _relative_to_content_root(named_candidate)

    fallback_images = [
        path
        for path in sorted(image_dir.iterdir(), key=lambda p: p.name.lower())
        if path.is_file() and path.suffix.lower().lstrip(".") in IMAGE_EXTENSIONS
    ]
    if fallback_images:
        return _relative_to_content_root(fallback_images[0])

    return None


JINJA_FILTERS = {
    "resolve_article_thumbnail": resolve_article_thumbnail,
}
