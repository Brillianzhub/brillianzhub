from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.sitemaps.views import sitemap


from blog.sitemaps import BlogSitemap


from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()


sitemaps = {

    'blog': BlogSitemap,
}

urlpatterns = [
    path('', views.index_view, name="home"),
    path('accounts/', include("accounts.passwords.urls")),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include("accounts.urls", namespace="account")),
    path('settings/', RedirectView.as_view(url='/account')),
    path('admin/', admin.site.urls),


    path('blog/', include("blog.urls")),
    path('ipray/', include("ipray.urls")),
    path('notifications/', include('notifications.urls')),

    path('book_appointment/', include("consult.urls")),


    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact/', views.contact_view, name="contact"),
    path('about/', views.about_view, name="about"),

    path('privacy_policy/', include("policies.urls")),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls'))

]

urlpatterns = urlpatterns + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
