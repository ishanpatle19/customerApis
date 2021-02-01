from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from customers.models import Customer
from customers.serializers import CustomerSerializer, RegisterSerializer, LoginSerializer, ForgotSerializer


@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': 
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data)

    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def register(request):
    # regData = JSONParser().parse(request)
    # customers_serializer = CustomerSerializer(regData, many=True)
    # return JsonResponse(customers_serializer.data, safe=False)
    if request.method == 'GET':
        customers = Customer.objects.all()
        register_serializer = RegisterSerializer(customers, many=True)
        return JsonResponse(register_serializer.data, safe=False)
    # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        register_data = JSONParser().parse(request)
        register_serializer = RegisterSerializer(data=register_data)
        if register_serializer.is_valid():
            register_serializer.save()
            return JsonResponse(register_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def login(request):
    # logData = JSONParser().parse(request)
    # customers_serializer = CustomerSerializer(logData, many=True)
    # return JsonResponse(customers_serializer.data, safe=False)
    if request.method == 'GET':
        customers = Customer.objects.all()
        login_serializer = LoginSerializer(customers, many=True)
        return JsonResponse(login_serializer.data, safe=False)
    # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        login_data = JSONParser().parse(request)
        login_serializer = LoginSerializer(data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse(login_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def forgot(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        forgot_serializer = ForgotSerializer(customers, many=True)
        return JsonResponse(forgot_serializer.data, safe=False)
    # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        forgot_data = JSONParser().parse(request)
        forgot_serializer = ForgotSerializer(data=forgot_data)
        if forgot_serializer.is_valid():
            forgot_serializer.save()
            return JsonResponse(forgot_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(forgot_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

