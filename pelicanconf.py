AUTHOR = "Allan Almazan"
SITENAME = "Allan Almazan"
SITESUBTITLE = "A personal blog"

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

THEME = "themes/aalmazan"
TEMPLATE_EXTENSIONS = [".j2", ".html"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = "posts/{date:%Y}-{date:%m}-{slug}.html"
ARTICLE_SAVE_AS = "posts/{date:%Y}-{date:%m}-{slug}.html"

# Top nav menu items
MENUITEMS = (
  ("Archives", "/archives.html"),
  ("Categories", "/categories.html"),
  ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
