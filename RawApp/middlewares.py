from django.http import HttpResponseServerError
from django.shortcuts import render

class AjaxMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        def is_ajax(self):
            return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        
        request.is_ajax = is_ajax.__get__(request)
        response = self.get_response(request)
        return response
    
class CustomErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Check if the exception meets the condition
        if isinstance(exception, CustomException):
            # Render the custom error template
            return render(request, '404.html', {'error_message': str(exception)})
        return None

class CustomException(Exception):
    pass