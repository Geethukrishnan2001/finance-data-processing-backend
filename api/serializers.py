from rest_framework import serializers
from .models import User, Record

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value

    def validate_type(self, value):
        if value not in ['income', 'expense']:
            raise serializers.ValidationError("Type must be income or expense")
        return value