from django.contrib.sitemaps import Sitemap
from .models import Blog


class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Blog.objects.all().published()

    def lastmod(self, obj):
        return obj.publish
