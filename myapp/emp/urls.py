from django.contrib import admin
from django.urls import path, include
from .views import EmpViewSet, add_emp, delete_emp, do_update_emp, emp_home, update_emp
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Emp',EmpViewSet)

urlpatterns = [
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path('',include(router.urls))
]
