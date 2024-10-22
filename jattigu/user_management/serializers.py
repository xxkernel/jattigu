from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            'email',
            'first_name',
            'second_name',  
            'date_of_birth',
            'gender',
            'weight',
            'height',
            'fitness_goal',
            'password'
        ]
