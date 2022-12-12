import joblib




def test_run():

    model = joblib.load('regression.joblib')
    X = [[205.999168680, 2, 0]]
    prediction = model.predict(X)
    assert prediction >= 200000 and prediction <=300000
    ## afficher la prediction
   
 
