from django.urls import path

from .views import DrugListApiView, DrugDetailApiView, ContactCreateApiView, OrderCreateApiView

urlpatterns = [
    path('drug/list/', DrugListApiView.as_view()),
    path('drug/detail/<int:pk>/', DrugDetailApiView.as_view()),
    path('contact/create/', ContactCreateApiView.as_view()),
    path('order/create/', OrderCreateApiView.as_view())
]