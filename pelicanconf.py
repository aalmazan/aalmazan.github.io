AUTHOR = "Allan Almazan"
SITENAME = "Allan Almazan"
SITESUBTITLE = "A personal blog"
SITEURL = "http://localhost:8000"

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

STATIC_PATHS = ["extra"]

EXTRA_PATH_METADATA = {
  "extra/robots.txt": {"path": "robots.txt"},
}

GOOGLE_SITE_VERIFICATION = "VczqzsxwsqxPjqIp5M_vX8c9hqCr2zTp18UQAEplyV4"

SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = False  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = False  # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False  # Subfeature of SEO enhancer

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
    'markdown.extensions.toc': {},
  },
  'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
