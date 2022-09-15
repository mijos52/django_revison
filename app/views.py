from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import CustomerSerializer


def login(request):
    return HttpResponse("This is the login page")


def signup(request):
    return HttpResponse("This is the Signup page")


@csrf_exempt
def customers(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"message": "you have succesfull created an account", "jwt_token": "","status": "200"},
                status=200,
            )
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def customer_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
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
