from django.urls import path
from maintenance.views import DevOpsNeedsView


urlpatterns = [path("", DevOpsNeedsView.as_view(), name="devops_maintenance")]
