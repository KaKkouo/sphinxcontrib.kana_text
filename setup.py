import sys
from setuptools import setup
import src as kt

sys.path.append('./src')
sys.path.append('./tests')

setup(
    version = kt.__version__,
    license = kt.__license__,
    author = kt.__author__,
    url = kt.__url__,
    download_url = 'https://pypi.org/project/sphinxcontrib.kana-text/',
    project_urls = {
        'Code': 'https://github.com/KaKkouo/sphinxcontrib.kana_text',
        'Issue tracker': 'https://github.com/KaKkouo/sphinxcontrib.kana_text/issues',
    },
)
