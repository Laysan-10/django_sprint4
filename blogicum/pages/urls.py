from django.urls import path
from .views import AboutView, RulesView, LogoutView



app_name = 'pages'


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('rules/', RulesView.as_view(), name='rules'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
