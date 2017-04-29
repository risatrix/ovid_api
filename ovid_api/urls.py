"""ovid_api URL Configuration

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


from api.models import Author, Work, Book, Poem, Line
from api.views import AuthorViewSet, WorkViewSet, BookViewSet, PoemViewSet

from rest_framework import routers, serializers, viewsets
from rest_framework_nested import routers

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Ovid API')

router = routers.SimpleRouter()
router.register(r'authors', AuthorViewSet, base_name="authors")

authors_router = routers.NestedSimpleRouter(router, r'authors', lookup="author")
authors_router.register(r'works', WorkViewSet, base_name="works")

works_router = routers.NestedSimpleRouter(authors_router, r'works', lookup='work')
works_router.register(r'books', BookViewSet, base_name='books')

books_router = routers.NestedSimpleRouter(works_router, r'books', lookup='book')
books_router.register(r'poems', PoemViewSet, base_name='poems')

# router.register(r'lines', LineViewSet)
# router.register(r'poems', PoemViewSet)
# router.register('books', BookViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^', include(authors_router.urls)),
    url(r'^', include(works_router.urls)),
    url(r'^', include(books_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
