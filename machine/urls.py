"""machine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from machine.views import current_datetime, hours_ahead
from django.views.generic import RedirectView
from django.views.static import serve
from django.views import static  # added along with static.serve line 47
from .settings import MEDIA_ROOT
from accounts.views import say_hello  #index
from accounts import urls as accounts_urls
from products import urls as urls_products
from products.views import all_products
from search import urls as urls_search  # added search
from cart import urls as urls_cart
from checkout import urls as urls_checkout


"""
    # name maps to url at href
    # 'We’ve curtailed the outlandishness here by limiting
    # the offset to 99 hour' (pg 60)
"""


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^hello/', say_hello),  # renders landing/base page
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^$', RedirectView.as_view(url='user_posts/')),
    url(r'^user_posts/', include('user_posts.urls')),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),

]
