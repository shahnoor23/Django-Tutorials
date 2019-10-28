from Add_Chairman.models import Chairman
from rest_framework import viewsets,permissions
from .serializers import ChairmanSerializer

#Chairman Viewset
class ChairmanViewSet(viewsets.ModelViewSet):
  queryset = Chairman.objects.all()
  permission_classes = [
      permissions.AllowAny
  ]
  serializer_class = ChairmanSerializer

  
