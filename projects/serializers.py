from rest_framework import serializers
from .models import Project
# Esto esta basado en un modelo creado previamente

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology' , 'created_ad')
        read_only_fields = ('created_ad',) # Este campo es solo para leer
