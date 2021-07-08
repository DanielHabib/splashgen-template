# website.py

from splashgen import launch
from splashgen.components import SplashSite, CTAButton

site = SplashSite(title="DanSplash - Test Splash Pages Built In Python by Dan",
                  theme="dark")
site.headline = "Dan built this page"
site.subtext = """
TRAVISSS"""
site.call_to_action = CTAButton(
    "https://github.com/danielhabib", "View on GitHub")

launch(site)
