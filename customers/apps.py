from django.apps import AppConfig


class CustomersConfig(AppConfig):
    name = 'customers'

class LoginConfig(AppConfig):
    name = 'logindb'

class RegisterConfig(AppConfig):
    name = 'registerdb'

class ForgotConfig(AppConfig):
    name = 'forgotdb'

