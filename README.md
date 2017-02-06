Redirect Middleware for edX
=======================

Installation
------------

```bash
$ pip install git+https://github.com/hrvojevu/redirect-middleware
```
After installing, import this package and add this middleware to MIDDLEWARE_CLASSES inside /edx-platform/lms/envs/common.py:

```bash
import redirect_middleware

MIDDLEWARE_CLASSES = (
    'redirect_middleware.middleware.UrlRedirectMiddleware',
)
```
* Order of classes inside MIDDLEWARE_CLASSES is important! Add this middleware to the end of the tuple.

Usage
-------
This middleware will check if request url is blacklisted, redirect to edX dashboard if so.