from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other employee details as needed

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    punch_in_time = models.DateTimeField(auto_now_add=True)
    punch_out_time = models.DateTimeField(null=True, blank=True)

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=(("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")), default="Pending")
