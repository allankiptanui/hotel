from django.urls import path

from .views import BookingList, RoomDetailsView, CancelBookingView,RoomListView

app_name='core'

urlpatterns = [
    path ('book/',RoomListView, name = 'RoomList'),
    path ('booking_list/',BookingList.as_view(), name = 'BookingList'),
    path ('booking/cancel/<pk>',CancelBookingView.as_view(), name = 'CancelBookingView'),
    path ('room/<category>/', RoomDetailsView.as_view(), name = 'RoomDetailView')
    
]

