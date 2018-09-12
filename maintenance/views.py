from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from .logic import optimal_devops_coverage
from .serializers import DevOpsNeedsSerializer


class DevOpsNeedsView(APIView):
    """Accept current DevOps needs info and return optimal coverage solution."""

    def post(self, request: Request) -> Response:
        serializer = DevOpsNeedsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = optimal_devops_coverage(**serializer.validated_data)

        return Response(response, HTTP_200_OK)
