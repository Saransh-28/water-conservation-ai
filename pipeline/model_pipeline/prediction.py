from pipeline.actions.trigger_gate import trigger_door_alert
threshold = 0.6

def load_model(path):
    # model = joblib.load(...)
    pass

def make_prediction(model, data):
    # prediction = model.predict(data)
    pass

def criteria(prediction):
    return prediction > threshold

def inference(data):
    model = load_model('path/to/model')
    prediction = make_prediction(model, data)
    if criteria(prediction):
        trigger_door_alert({'MESSAGE':'OPEN GATE !!!'})

