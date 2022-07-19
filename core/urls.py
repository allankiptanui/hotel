from django.urls import path

from .views import BookingList, RoomDetailsView, RoomListView, BookingView

app_name='core'

urlpatterns = [
    path ('availability_list/',RoomListView, name = 'RoomList'),
    path ('booking_list/',BookingList.as_view(), name = 'BookingList'),
    path ('book/',BookingView.as_view(), name = 'Booking_view'),
    path ('room/<category>/', RoomDetailsView.as_view(), name = 'RoomDetailView')
    
]

