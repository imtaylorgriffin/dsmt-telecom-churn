import azure.functions as func
import logging
from prediction import make_prediction


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="predict")
def predict(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tenure = req.params.get('tenure')
    monthly = req.params.get('monthly')
    techSupport = req.params.get('techsupport')

    prediction = make_prediction(tenure=tenure,
                                 MonthlyCharges = monthly,
                                 TechSupport_yes = techSupport)



    if tenure and monthly and techSupport:
        return func.HttpResponse(f"AHHHHHHHHH!!!!! Churn Probability: {prediction}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    