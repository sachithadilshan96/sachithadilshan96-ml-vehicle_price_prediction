from django import forms



Manuf_Choices= [
    (1, 'Chevrolet'),
    (2, 'Ford'),
    (3, 'Nissan'),
    (4, 'Jeep'),
    (5, 'Toyota'),
    (6, 'Honda'),
    (7, 'Audi'),
    (8, 'GMC'),
    (9, 'RAM'),
    (10, 'Dodge'),

    ]


Condition_Choices= [
    (1, 'Brand New'),
    (2, 'Like new'),
    (3, 'Excellent'),
    (4, 'Good'),
    (5, 'Fair'),
    (6, 'Salvage'),
    ]


cylinders_Choices= [
    (1, '3 cylinders'),
    (2, '4 cylinders'),
    (3, '5 cylinders'),
    (4, '6 cylinders'),
    (5, '8 cylinders'),
    (6, '10 cylinders'),
    (7, '12 cylinders'),
    (8, 'other'),

    ]

fuel_Choices= [
    (1, 'Gas'),
    (2, 'Diesel'),
    (3, 'Hybrid'),
    (4, 'Electric'),
    (5, 'Other'),
    ]

transmission_Choices= [
    (1, 'Automatic'),
    (2, 'Manual'),
    (3, 'Other'),
    ]


type_Choices= [
    (1, 'Truck'),
    (2, 'SUV'),
    (3, 'scedan'),
    (4, 'Pickup'),
    (5, 'Wagon'),
    (6, 'Coupe'),
    (7, 'Hatchback'),
    (8, 'Van'),
    (9, 'Mini-Van'),

    ]

year_Choices= [tuple([x,x]) for x in range(1923,2022)]


class PredictForm(forms.Form):

      type = forms.IntegerField(label='Select Type',widget=forms.Select(choices=type_Choices))
      year = forms.IntegerField(label='Enter manufactured year',widget=forms.Select(choices=year_Choices))
      manuf = forms.IntegerField(label='Select manufacturer',widget=forms.Select(choices=Manuf_Choices))
      condition = forms.IntegerField(label='Select Condition',widget=forms.Select(choices=Condition_Choices))
      cylinders = forms.IntegerField(label='Select cylinders',widget=forms.Select(choices=cylinders_Choices))
      fuel = forms.IntegerField(label='Select fuel type',widget=forms.Select(choices=fuel_Choices))
      odometer = forms.FloatField(label='Odometer')
      transmission = forms.IntegerField(label='Select transmission',widget=forms.Select(choices=transmission_Choices))
