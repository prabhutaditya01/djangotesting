from rest_framework import serializers
from .models import *
#creating serializers
           
#creating patient serializers
class PatientSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=patient
        fields="__all__"     
#creating doctors serialzers                                 
class DoctorsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Doctors
        fields="__all__"                        