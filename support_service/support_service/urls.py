
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('api/tickets/', create_ticket, name='create_ticket'),
    path('admin/', admin.site.urls),
    path('support/', include('support.urls')),
]
