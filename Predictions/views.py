from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import PredictForm
import joblib
import numpy as np
import pandas as pd


def predict(request):
    if request.method == 'GET':
     return render(request,"index.html",{'form' : PredictForm()})
    else:
        form= PredictForm(request.POST or None)
        #import model file
        model = joblib.load('vehicle_price_prediction_model.sav')
        #validating user entered 18 features inputs
        if form.is_valid():
            type= form.cleaned_data.get("type")
            year= form.cleaned_data.get("year")
            manuf= form.cleaned_data.get("manuf")
            condition= form.cleaned_data.get("condition")
            cylinders= form.cleaned_data.get("cylinders")
            fuel= form.cleaned_data.get("fuel")
            odometer= form.cleaned_data.get("odometer")
            transmission= form.cleaned_data.get("transmission")

            #adding validated user inputs to model
            ans =model.predict([[
                                year,
                                manuf,
                                condition,
                                cylinders,
                                fuel,
                                odometer,
                                transmission,
                                type

            ]])
            #extracting predicted value
            predict_value = float(np.round(ans[0], 2))
            context = {

            'predict_value': predict_value,
            }
            # lgb_predict = model.predict([[2013,	1,	4,	5,	1,	119598.0,	1,	8,]])
            # lgb_p = float(np.round(lgb_predict[0], 2))


            return render(request,"results.html",context)
