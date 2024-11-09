from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'user',UserProfileSimpleViewSet,basename='user-list')
router.register(r'hotel',HotelListViewSet,basename='hotel-list')
router.register(r'hotel-detail',HotelDetailViewSet,basename='hotel-detail')
router.register(r'rooms',RoomListViewSet,basename='room-list')
router.register(r'room-detail',RoomDetailViewSet,basename='room-detail')
router.register(r'review',ReviewViewSet,basename='review')
router.register(r'booking',BookingViewSet,basename='booking')
router.register(r'img_room',RoomImgViewSet,basename='room_img')

urlpatterns = [
    path('',include(router.urls))

    ]


