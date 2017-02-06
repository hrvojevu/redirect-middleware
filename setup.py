import os
from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


setup(name='redirect_middleware',
      version='0.1',
      description='Django middleware that redirects all URLs to single URL',
      url='https://github.com/hrvojevu/redirect-middleware',
      author='ExtensionEngine',
      author_email='hvucic@extensionengine.com',
      long_description=README,
      license='MIT',
      packages=['redirect_middleware'],
      zip_safe=False)
