from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("", views.Activities_view, name = "main"),
    path("activity/<int:pk>/", views.activity_detail.as_view(), name="activity_detail"),
    path("formularz", views.HobbyView.as_view(), name = "formularz"),
    path("forum", views.ForumView, name = "forum"),
    path("update/<int:pk>/edit/", views.UpdatePost.as_view(), name = "update"),
    path("delete/<int:pk>/delete/", views.PostDelete.as_view(), name = "delete"),
    path("user_posts", views.user_posts, name= "user_posts"),
    path("succes", views.SuccesView.as_view(), name = "succes"),
    path("register", views.registration, name= "register"),
    path("login", views.sign_in, name = "login"),
    path("logout", views.logoutuser, name = "logout"),

    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)