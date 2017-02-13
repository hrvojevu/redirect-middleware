from django.http import HttpResponseRedirect


class UrlRedirectMiddleware:
    blacklist = ('/course', '/u/', '/account', '/search', '/about', '/blog', '/contact', '/donate')

    def process_request(self, request):
        url_path = request.META['PATH_INFO']
        protocol = "https://" if request.is_secure() else "http://"
        dashboard = "%s%s/dashboard" % (protocol, request.META['HTTP_HOST'])
        oidc = "%s%s/auth/login/oidc-oauth2/?auth_entry=login&next=%%2Fdashboard" % (protocol, request.META['HTTP_HOST'])

        if url_path.find('/login') is 0:
            return HttpResponseRedirect(oidc)
        elif url_path == '/':
            return HttpResponseRedirect(dashboard)
        else:
            for str in self.blacklist:
                if url_path.find(str) is 0:
                    return HttpResponseRedirect(dashboard)
