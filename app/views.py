from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

GET_SUCCESS_RESPONSE = {
    "message": "post requests only",
    "status": "200",
    "format": {
        "user_name": " ",
        "email_id": " ",
        "password": " ",
        "gender": "",
        "date_of_birth": "YYY-MM-DD",
        "contact_number": "",
    },
}

POST_SUCCESS_RESPONSE = {
    "message": "success",
    "status": "200",
}


def login(request):

    return HttpResponse("This is the login page")


@api_view(["GET"])
def get_users(request):
    customer_data = Customer.objects.all()
    serializer = CustomerSerializer(customer_data, many=True)
    return Response(GET_SUCCESS_RESPONSE)


@api_view(["POST"])
def create_users(request):
    serializer = CustomerSerializer(request.data)
    return Response(POST_SUCCESS_RESPONSE)


@csrf_exempt
def signup(request):

    if request.method == "GET":
        return JsonResponse(
            {
                "message": "post requests only",
                "status": "200",
                "format": {
                    "user_name": " ",
                    "email_id": " ",
                    "password": " ",
                    "gender": "",
                    "date_of_birth": "YYY-MM-DD",
                    "contact_number": "",
                },
            },
            status=200,
        )

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def customer_detail(request, pk):
    """
    Retrieve, update or delete a code customer.
    """
    try:
        customers = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CustomerSerializer(customers)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customers, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        customers.delete()
        return HttpResponse(status=204)
