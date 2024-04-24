from rest_framework import serializers
from vinny.models import Frase

class FraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frase
        fields = '__all__'