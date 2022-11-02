from rest_framework import serializers
from nikey_restapi.models import Nikey_restApi

class NikeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nikey_restApi
        fields = ['name', 'phone_number', 'address']

