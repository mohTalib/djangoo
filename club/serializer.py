from jsonschema import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import List_Opps, List_Opps_others, List_Opps_volon, List_Opps_program, List_Opps_intern, List_Opps_course, Training


class OppsSerializer(ModelSerializer):
    class Meta:
        model = List_Opps
        fields = '__all__'

class OppsSerializerco(ModelSerializer):
    class Meta:
        model = List_Opps_course
        fields = '__all__'

class OppsSerializerin(ModelSerializer):
    class Meta:
        model = List_Opps_intern
        fields = '__all__'

class OppsSerializerpr(ModelSerializer):
    class Meta:
        model = List_Opps_program
        fields = '__all__'

class OppsSerializervo(ModelSerializer):
    class Meta:
        model = List_Opps_volon
        fields = '__all__'

class OppsSerializerot(ModelSerializer):
    class Meta:
        model = List_Opps_others
        fields = '__all__'

class OppsSerializertr(ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

# serializers.py



# users/serializers.py

# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'email')



