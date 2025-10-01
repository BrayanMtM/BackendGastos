from rest_framework import viewsets
from .models import Registro
from .serializers import RegistroSerializer

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all().order_by('-id')
    serializer_class = RegistroSerializer
