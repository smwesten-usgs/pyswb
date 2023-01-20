major = 0
minor = 0
micro = 1
__version__ = f"{major}.{minor}.{micro}"

__pakname__ = "pyswb"

author_dict = {
    "Steve Westenbroek": "smwesten@usgs.gov"
}
__author__ = ", ".join(author_dict.keys())
__author_email__ = ", ".join(s for _, s in author_dict.items())
