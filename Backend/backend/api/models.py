from django.db import models

# Create your models here.
class RealEstateData(models.Model):
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()   
    year = models.IntegerField()
    total_sales = models.FloatField()
    total_sold = models.IntegerField()
    
    # Property Type Counts
    flat_sold = models.IntegerField()
    office_sold = models.IntegerField()
    shop_sold = models.IntegerField()
    others_sold = models.IntegerField()
    
    # Average Prices
    flat_avg_price = models.FloatField()
    office_avg_price = models.FloatField()
    shop_avg_price = models.FloatField()
    others_avg_price = models.FloatField()
    
    # Additional Metrics
    total_units = models.IntegerField()
    total_area = models.FloatField()
    
    class Meta:
        unique_together = ('location', 'year')  # Prevents duplicate entries
    
    def __str__(self):
        return f"{self.location} ({self.year})"