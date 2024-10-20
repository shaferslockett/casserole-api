from rest_framework import serializers
from .models import Casserole

class CasseroleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casserole 
        fields = ["name", "ingredients", "instructions"] 
