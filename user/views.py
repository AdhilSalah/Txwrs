from rest_framework import generics
from .models import User,Game
from .serializers import UserSerializer,ChangePasswordSerializer,UpdateUserSerializer,MyTokenObtainPairSerializer,GameSerializer,GameUpateSerializer,RetriveSerializer,ListGameSerializer
                                                                                                                                                
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UpdateUserSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class DestroyUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]
class StartGameView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = GameSerializer

class RetriveGameView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = RetriveSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        string = Game.objects.get(id=kwargs.get('pk'))
        updated_string = string.game_string
        if len(updated_string) == 12:
            pal_check = ""
            for i in range(0,len(updated_string),2):
                pal_check += updated_string[i]
            if pal_check == pal_check[::-1]:

                return Response({
                                "string":pal_check,
                                "Message":"string is  palindrome"})
            else:
            
                return Response({
                                "string":pal_check,
                                "Message":"string is not palindrome"})

        return super().retrieve(request, *args, **kwargs)
class UpdateGameView(generics.UpdateAPIView,generics.RetrieveAPIView):
    queryset = Game.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class=GameUpateSerializer


    def update(self, request, *args, **kwargs):

        string = Game.objects.get(id=kwargs.get('pk'))
        updated_string = string.game_string
        new_string = request.data['enter_your_string']

        if len(updated_string)==10:
            pal_check = ""
            for i in range(0,len(updated_string),2):
                pal_check += updated_string[i]
            pal_check+=new_string

            if pal_check == pal_check[::-1]:
                super().update(request, *args, **kwargs)
                return Response({
                                "string":pal_check,
                                "Message":"string is  palindrome"})
            else:
                
                super().update(request, *args, **kwargs)
                return Response({
                                "string":pal_check,
                                "Message":"string is not palindrome"})
        
        if len(updated_string) == 12:
            pal_check = ""
            for i in range(0,len(updated_string),2):
                pal_check += updated_string[i]
            if pal_check == pal_check[::-1]:

                return Response({
                                "string":pal_check,
                                "Message":"string is  palindrome"})
            else:
                
                
                return Response({
                                "string":pal_check,
                                "Message":"string is not palindrome"})
        
        return super().update(request, *args, **kwargs)


class ListGameView(generics.ListAPIView):

    queryset = Game.objects.all()
    serializer_class = ListGameSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
