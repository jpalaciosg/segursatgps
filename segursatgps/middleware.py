from django.utils.deprecation import MiddlewareMixin

class AccountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            if str(request.user) != 'AnonymousUser':
                my_request  = request.POST.copy()
                my_request['account'] = request.user.profile.account.name
                request.POST = my_request
        response = self.get_response(request)
        return response