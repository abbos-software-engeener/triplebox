from .models import *
from  . serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet


class ClientCreateView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzier


class SubCategoryView(ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    

class HouseListView(ListAPIView):
    queryset  = House.objects.all()
    serializer_class = HouseListSerializer


class HouseDetailView(RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer


class HouseViewSet(ModelViewSet):
    queryset =House.objects.all()
    serializer_class = HouseListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializer_class
        else:
            return HouseDetailSerializer