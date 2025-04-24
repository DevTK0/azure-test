import azure.functions as func

app = func.FunctionApp()

@app.route(route="test")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("hello world")
