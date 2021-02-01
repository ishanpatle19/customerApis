from rest_framework import serializers
from customers.models import Customer, Register, Login, Forgot


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            'firstName',
            'lastName',
            'email',
            'password',
            'phone'
        )


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = (
            'firstName',
            'lastName',
            'email',
            'password',
            'phone'
        )



class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = (
            'email',
            'password',
        )


class ForgotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forgot
        fields = (
            'email',
        )



