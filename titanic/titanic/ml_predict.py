def prediction_model(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title):
    import pickle
    x = [[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title]]
    randomforest = pickle.load(open('titanic_model.sav','rb'))
    prediction = randomforest.predict(x)
    

    if prediction == 0:
        prediction = "Not Survived"
        
    elif prediction == 1:
        prediction = "Survived"
        
    else:
        prediction = "Error"
    
    return prediction