from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def home(request):
    return render(request,'Home.html')
def predict(request):
    return render(request,'predict.html')

def result(request):
    # Remplacez par le nom réel du fichier CSV dans ce répertoire
    file_path = r'C:\Users\arwag\Desktop\Projet_Medical_Diabites\diabetes.csv'

    # Lire le fichier CSV
    data = pd.read_csv(file_path)
    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # Utilisation de POST pour récupérer les valeurs
    val1 = float(request.POST['pregnancies'])
    val2 = float(request.POST['glucose'])
    val3 = float(request.POST['blood_pressure'])
    val4 = float(request.POST['skin_thickness'])
    val5 = float(request.POST['insulin'])
    val6 = float(request.POST['bmi'])
    val7 = float(request.POST['diabetes_pedigree_function'])
    val8 = float(request.POST['age'])

    # Effectuer la prédiction
    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    # Résultat de la prédiction
    if pred == [1]:
        result1 = "Positive"
    else:
        result1 = "Negative"

    return render(request, 'predict.html', {"result2": result1})