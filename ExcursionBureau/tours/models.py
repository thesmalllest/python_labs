from django.db import models

class Guide(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Booking(models.Model):
    client_name = models.CharField(max_length=100)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.tour.title}"
