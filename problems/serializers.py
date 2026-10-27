
from rest_framework import serializers

from problems.models import Question


class Questionserializers(serializers.ModelSerializer):


    class Meta:

        model = Question

        fields = "__all__"

        read_only_fields =["id","assessment","created_at","updated_at","created_by"]