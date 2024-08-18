from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world),
    path('task', views.task_t),
    path('', views.home_page),
    path('analytics', views.analytics),
    
    # If 'redirect' needs special handling, point it to 'redirect_url' or another view
    path('redirect/<slug:customname>', views.redirect_url),

    # Catch-all for other slugs
    path('<slug:customname>', views.redirect_url),
]
