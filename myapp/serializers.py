from rest_framework import serializers
from .models import students

class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = students
        fields = ('firstname','lastname')