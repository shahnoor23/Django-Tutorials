from rest_framework import serializers
from Add_Chairman.models import Chairman


class ChairmanSerializer(serializers.ModelSerializer):
   class Meta:
       model = Chairman
       fields ='__all__'