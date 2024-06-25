from .models import House, Client
from  . serializers import HouseListSerializer, HouseDetailSerializer, ClientSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

class ClientCreateView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class HouseListView(ListAPIView):
    queryset  = House.objects.all()
    serializer_class = HouseListSerializer


class HouseDetailView(RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
