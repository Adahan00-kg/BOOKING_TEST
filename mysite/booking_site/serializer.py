from rest_framework import serializers
from .models import *

class HotelSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name']

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id','user_name','hotel','text','stars','parent']

class ReviewListSerializer(serializers.ModelSerializer):
    user_name = UserProfileSerializer()

    class Meta:
        model = Review
        fields = ['id','user_name','hotel','text','stars','parent']


class RoomImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']

class RoomListSerializer(serializers.ModelSerializer):

    room_images  = RoomImgSerializer(many=True)
    class Meta:
        model = Room
        fields = ['room_number','room_type','room_status',
                  'room_price','room_images','all_inclusive']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImgSerializer(read_only=True,many=True)
    class Meta:
        model = Room
        fields = ['room_number','room_type',
                  'room_status','room_price','all_inclusive',
                  'room_description','hotel_room','room_images']


class HotelImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']

class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImgSerializer(read_only=True,many=True)
    average_rating =  serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['hotel_name','country','city','hotel_images','stars','average_rating' ]


    def get_average_rating(self,obj):
        return obj.get_average_rating()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images = HotelImgSerializer(read_only=True,many=True)
    review = ReviewListSerializer(many=True,read_only=True)
    rooms = RoomListSerializer(read_only=True,many=True)
    owner = UserProfileSerializer()
    average_rating =  serializers.SerializerMethodField()


    class Meta:
        model = Hotel
        fields = ['hotel_name','hotel_description','country',
                  'city','address','stars','hotel_images',
                  'hotel_video','review'
                  ,'owner','created_date','rooms','average_rating'

                  ]

    def get_average_rating(self,obj):
        return obj.get_average_rating()




class BookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    check_out= serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Booking
        fields = ['hotel_book','room_book',
                  'user_booking','check_in',
                  'check_out','total_price',
                  'status_book']

