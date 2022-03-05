from flask import request, jsonify, make_response
from .models import prepare_predictions
import time 

def error_response(msg, status=404):
    return make_response(jsonify({"detail": str(msg), "status":status, "title":"Bad Request"}), status)

def success_response(features, model, prediction, seconds):
    return make_response(jsonify({'model': model, 'features': features, 'prediction': prediction, 'seconds': seconds}), 200)

def predict(features: list, model: str):
    '''
    http://localhost:8081/features/{features}/model/{model}/prediction
    example: http://localhost:8081/features/23,12,64,34,0,22,0.65,34/model/logit/prediction
    '''
    try:
        start_time = time.time()
        prediction = prepare_predictions(features, model)[0]
        seconds = time.time() - start_time
        return success_response(features, model, prediction, seconds)

    except Exception as exc:
        return error_response(exc)

