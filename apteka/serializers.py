from rest_framework import serializers
from .models import Drug, Contact


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    drug_type = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'drug_type', 'message']

    def get_drug_type(self, obj):
        return obj.drug_type.title

