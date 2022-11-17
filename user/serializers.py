from rest_framework import serializers
from .models import User,Game
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:

        model=User

        fields = ['id','email','password']
        extra_kwargs={'password':{'write_only':True}
        }

    
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance



class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']


    def validate_email(self, value):
        user = self.context['request'].user
        print(user)
        if User.objects.exclude(pk=user.id).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        
        instance.email = validated_data['email']
        instance.save()

        return instance



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game 
        fields = '__all__'

class GameUpateSerializer(serializers.ModelSerializer):
    enter_your_string = serializers.CharField(write_only=True, required=True,max_length=1)
    entered_string = serializers.SerializerMethodField()
    class Meta:
        model = Game
        fields = ['entered_string','enter_your_string']

    def update(self, instance, validated_data):
        
        game_string = instance.game_string
        new_string = validated_data['enter_your_string']
        updated_string = game_string

        if len(updated_string) < 11 :
            m= str(0)
            updated_string += new_string+m
        
        
        instance.game_string = updated_string
        instance.save()
        return instance
    
    def get_entered_string(self,obj):
        pal_check = ""
        for i in range(0,len(obj.game_string),2):
                pal_check += obj.game_string[i]
        return pal_check


        
class RetriveSerializer(serializers.ModelSerializer):
    entered_string = serializers.SerializerMethodField()
    class Meta:
        model  = Game
        fields = ['entered_string']
    def get_entered_string(self,obj):
        pal_check = ""
        for i in range(0,len(obj.game_string),2):
                pal_check += obj.game_string[i]
        return pal_check

class ListGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['id'] 