from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True, null=True)
  completed = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now=True)
  completed_at = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.title