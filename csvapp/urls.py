from django.urls import path

from .views import PersonalDetailsViews

urlpatterns=[path('Personal_details/',PersonalDetailsViews.as_view())]