from django.urls import path

from . import views


urlpatterns = [
    path("health", views.health),
    path("auth/register", views.register),
    path("auth/login", views.login),
    path("auth/test", views.auth_test),
    path("spaces", views.spaces),
    path("spaces/<int:space_id>", views.space_detail),
    path("bookings", views.bookings),
    path("bookings/my", views.my_bookings),
    path("bookings/<int:booking_id>", views.booking_detail),
    path("users/search", views.search_users),
    path("users/profile", views.profile),
    path("users/updatepassword", views.update_password),
    path("posts", views.posts),
    path("posts/<int:post_id>/like", views.toggle_like),
    path("posts/<int:post_id>/comments", views.add_comment),
    path("posts/<int:post_id>", views.delete_post),
    path("groups", views.groups),
    path("groups/<int:group_id>/join", views.join_group),
    path("groups/<int:group_id>/messages", views.group_messages),
    path("events", views.events),
    path("events/<int:event_id>/register", views.register_event),
    path("events/<int:event_id>/participants", views.event_participants),
]
