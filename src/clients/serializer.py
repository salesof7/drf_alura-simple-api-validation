from rest_framework import serializers
from .models import Client
from .validators import *

class ClientSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        """"""
        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'The CPF must have 11 digits'})
        if not valid_name(data['name']):
            raise serializers.ValidationError({'name': "Don\'t include numbers in this field"})
        if not valid_rg(data['rg']):
            raise serializers.ValidationError({'rg': 'The RG must have 9 digits'})
        if not valid_cell_phone(data['cell_phone']):
            raise serializers.ValidationError({
                'cell_phone': 'The mobile number must follow this model, respecting spaces and dashes: (XX) XXXXX-XXXX'
            })
        return data
