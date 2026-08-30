import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pelicanconf import *  # noqa: E402,F403

# This matches content/extra/CNAME. Change both places if the domain changes.
SITEURL = "https://www.shima10-x1p.net"
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
