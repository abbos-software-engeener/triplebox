from rest_framework.serializers import ModelSerializer
from .models import Client, House


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields  = '__all__'



class HouseListSerializer(ModelSerializer):
    class Meta:
        model = House 
        fields = ["id", "name", "phone", "location", "image_data1",]    


class HouseDetailSerializer(ModelSerializer):
    class Meta:
        model = House 
        fields = '__all__'


        