import pandas as pd
from api.models import RealEstateData
from django.conf import settings
import os

def import_data():
    df = pd.read_excel(os.path.join(settings.BASE_DIR, 'Sample_data.xlsx'))

    for _, row in df.iterrows():
        RealEstateData.objects.create(
            location=row['final location'],
            city=row['city'],
            lat=row['loc_lat'],
            lng=row['loc_lng'],
            year=row['year'],
            total_sales=row['total_sales - igr'],
            total_sold=row['total sold - igr'],
            flat_sold=row['flat_sold - igr'],
            office_sold=row['office_sold - igr'],
            shop_sold=row['shop_sold - igr'],
            others_sold=row['others_sold - igr'],
            flat_avg_price=row['flat - weighted average rate'],
            office_avg_price=row['office - weighted average rate'],
            shop_avg_price=row['shop - weighted average rate'],
            others_avg_price=row['others - weighted average rate'],
            total_units=row['total units'],
            total_area=row['total carpet area supplied (sqft)']
        )
    print('sucess')