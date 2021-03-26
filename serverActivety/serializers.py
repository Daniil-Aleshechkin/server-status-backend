from rest_framework import serializers

from serverActivety.models import Time

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['date','uptime','noPlayerTime']