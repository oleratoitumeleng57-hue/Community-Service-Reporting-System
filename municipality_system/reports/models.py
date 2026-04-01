
from django.db import models

class Issue(models.Model):
    ISSUE_TYPES = [
        ('Electricity', 'Electricity'),
        ('Water', 'Water'),
        ('Roads', 'Roads'),
    ]

    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255)
   

    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue {self.id} - {self.status}"
