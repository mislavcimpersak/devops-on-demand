from rest_framework import serializers


class DataCenterSerializer(serializers.Serializer):
    """Describe single data center."""

    name = serializers.CharField()
    servers = serializers.IntegerField(min_value=0)


class DevOpsNeedsSerializer(serializers.Serializer):
    """Describe request sent to the app with all data centers needs."""

    DM_capacity = serializers.IntegerField(min_value=1)
    DE_capacity = serializers.IntegerField(min_value=1)
    data_centers = DataCenterSerializer(many=True, allow_empty=False)
