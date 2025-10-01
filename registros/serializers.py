from rest_framework import serializers
from .models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    hora = serializers.SerializerMethodField()  # 👈 Sobrescribimos el campo

    class Meta:
        model = Registro
        fields = '__all__'

    def get_hora(self, obj):
        # Devolver la hora sin microsegundos en formato HH:MM:SS
        return obj.hora.strftime("%H:%M:%S")
