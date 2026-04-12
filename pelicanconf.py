from pathlib import Path

AUTHOR = "しま(shima10-x1p)"
SITENAME = "しま"
SITEURL = ""
RELATIVE_URLS = True

PATH = "content"
THEME = "themes/shima-island-coral"
ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]

ARTICLE_URL = "articles/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "articles/{date:%Y}/{date:%m}/{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TIMEZONE = "Asia/Tokyo"

DEFAULT_LANG = "ja"

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
PROFILE_BIO_LINES = ("メモを残します。",)
PROFILE_OG_DESCRIPTION = "メモ書きをする場所"
TWITTER_USERNAME = "@shima10_x1p"
PROFILE_SOCIAL_LINKS = (
    ("GitHub", "https://github.com/shima10-x1p", "github"),
    ("Twitter", "https://x.com/shima10_x1p", "twitter"),
)

# 船旅の記録（年月日, 運航会社, 航路）
PROFILE_SHIP_VOYAGES = (
    ("2026/02/02", "東京湾フェリー", "久里浜港 → 金谷港"),
    ("2026/03/07", "東海汽船", "大さん橋 → 竹芝桟橋"),
    ("2026/03/12", "ふじさん駿河湾フェリー", "清水港 → 土肥港"),
    ("2026/03/21", "東京都観光汽船", "日の出桟橋 → 浅草"),
    ("2026/04/11", "富士急マリンリゾート", "熱海港 ⇔ 初島港")
)

# 推しVTuber（名前, チャンネルURL, 動画リスト）
# 動画リストは (タイトル, 埋め込みURL) のタプル
# 埋め込みURL例: https://www.youtube.com/embed/VIDEO_ID
PROFILE_OSHI_VTUBERS = (
    {
        "name": "周央 サンゴ",
        "channel_url": "https://www.youtube.com/@SuoSango",
        "videos": (
            (
                "【歌ってみた】おやすみポラリスさよならパラレルワールド/cover【周央サンゴ】",
                "https://www.youtube.com/embed/RBqmUsysHNc?si=_fP0FVWOfMvfDo9U",
            ),
        ),
    },
)

MENUITEMS = (
    ("プロフィール", "/profile/"),
    ("ボトルメール", "/bottles/"),
)

# ボトルメール設定
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["bottles"]

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

    image_dir_rel = (
        Path("images") / date.strftime("%Y") / date.strftime("%m") / str(slug)
    )
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

# Markdownのcodehilite設定（Pygmentsシンタックスハイライト）
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}
