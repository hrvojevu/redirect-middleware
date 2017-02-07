from django.http import HttpResponseRedirect


class UrlRedirectMiddleware:
    blacklist = ('/course', '/u/', '/account', '/search', '/about', '/blog', '/contact', '/donate')

    def process_request(self, request):
        url_path = request.META['PATH_INFO']
        protocol = "https://" if request.is_secure() else "http://"
        redirect_url = "%s%s/dashboard" % (protocol, request.META['HTTP_HOST'])

        if url_path == '/':
            return HttpResponseRedirect(redirect_url)
        else:
            for str in self.blacklist:
                if url_path.find(str) is 0:
                    return HttpResponseRedirect(redirect_url)
