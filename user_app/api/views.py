from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serializers import RegistrationSerializer
# from user_app import models



@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account1 = serializer.save()
            
            data['response'] = "Registration Successful!"
            data['username'] = account1.username
            data['email'] = account1.email


            # token = Token.objects.get(user=account1).key
            # data['token'] = token
            refresh = RefreshToken.for_user(account1)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                
            }
        

        else:
            data = serializer.errors
        

    return Response(data, status.HTTP_201_CREATED)