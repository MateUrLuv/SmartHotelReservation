from django.urls import path
from .views import (
    HotelListCreate, HotelRetrieveUpdateDestroy,
    RoomListCreate, RoomRetrieveUpdateDestroy,
    ReservationListCreate, ReservationRetrieveUpdateDestroy,
    CustomerListCreate, CustomerRetrieveUpdateDestroy,
    PaymentListCreate, PaymentRetrieveUpdateDestroy,
)

urlpatterns = [
    path('hotels/', HotelListCreate.as_view(), name='hotel-list-create'),
    path('hotels/<int:pk>/', HotelRetrieveUpdateDestroy.as_view(), name='hotel-detail'),
    path('rooms/', RoomListCreate.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomRetrieveUpdateDestroy.as_view(), name='room-detail'),
    path('reservations/', ReservationListCreate.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', ReservationRetrieveUpdateDestroy.as_view(), name='reservation-detail'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-detail'),
    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroy.as_view(), name='payment-detail'),
]