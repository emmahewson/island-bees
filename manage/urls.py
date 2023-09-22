from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage, name='manage'),
    path(
        'toggle/<int:message_id>/',
        views.toggle_message,
        name='toggle_message'
    ),

    # path('add/', views.add_faq, name='add_faq'),
    # path('edit/<int:faq_id>/', views.edit_faq, name='edit_faq'),
    # path('delete/<int:faq_id>/', views.delete_faq, name='delete_faq'),
]
