from rest_framework import serializers
from emp.models import Emp

class EmpSerilaizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emp
        fields = "__all__"