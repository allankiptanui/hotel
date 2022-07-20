
from multiprocessing import context
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
import datetime

from django.views.generic import ListView, FormView, View, DeleteView

from core.forms import AvailabilityForm
from .models import Categories, Hotel, Room, Booking

# Create your views here.


def availability_check(room, check_in, check_out,):
    availablity_rooms = []

    bookings_list = Booking.objects.filter(room=room)
    for booking in bookings_list:
        if booking.check_in > check_in or booking.check_out < check_out:
            availablity_rooms.append(True)
        else:
            availablity_rooms.append(False)
    return all(availablity_rooms)


def RoomListView(request):
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)
    room_names = room_categories.values()
    print(room_categories)
    room_list = []
    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('core:RoomDetailView', kwargs={
                           'category': room_category})
        room_list.append((room, room_url))
    context = {
        "room_list": room_list,
    }

    return render(request, 'room_list.html', context)


class BookingList(ListView):
    model = Booking
    template_name = 'booking_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            bookings_list = Booking.objects.all()
            return bookings_list
        else:
            return Booking.objects.filter(user=self.request.user)


class RoomDetailsView(View):

    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)

        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)

            context = {
                'room_category': room_category,
                'form': form
            }
        else:
            return HttpResponse("category doesnt exixt")

        return render(request, 'room_details.html', context)

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)
        template_name= 'booking_confirm_delete.html'
        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if availability_check(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,

                hotel_name=data['destination'],
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out'],

            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = "roomAvailability_form.html"

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if availability_check(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse(" we sorry all this rooms are booked!!!😢 try onother room☺😊")


class CancelBookingView(DeleteView):
    model = Booking
    success_url = reverse_lazy('core:BookingList')
