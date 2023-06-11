from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import JsonResponse
@csrf_exempt
def create_superuser(request):
    if request.method == 'POST':
        # Retrieve the username and password from the request body
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # User.objects.create_superuser(username=username,email= email,password=password)

        return JsonResponse({'message': 'Superuser created successfully'})

    return JsonResponse({'message': 'Invalid request method'}, status=400)
