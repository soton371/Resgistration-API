
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

@api_view(['POST',])
def registrationAPI(request):
    if request.method == "POST":
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']

        # check already username
        if User.objects.filter(username=username).exists():
            return Response({"error": "An user with that username already exists!"})
        
        # match password
        if password1 != password2:
            return Response({"error": "Password didn't match"})
        
        # initial work
        user = User()
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True   # Otherwise login is not possible

        user.set_password(raw_password=password1)   #password are not visible
        user.save()
        return Response({"success": "User successfully registered"})