from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Transfer(models.Model):
    userfrom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers_sent')
    userto = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers_received')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    payment = models.DecimalField(max_digits=10, decimal_places= 2, verbose_name='Сума')

    def save(self, *args, **kwargs):
        if not self.pk and 'request' in kwargs:
            self.userfrom = kwargs.pop('request').user
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.description
