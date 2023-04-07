from rest_framework import serializers
from inventory.models.products_movements import Movements


class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements
        fields = '__all__'
