from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken


UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
	def create(self, validated_data):
		# Extract the required fields
		email = validated_data['email']
		username = validated_data['username']
		password = validated_data['password']

		# Remove the required fields from the validated data
		del validated_data['email']
		del validated_data['username']
		del validated_data['password']

		# Create the user object with the remaining fields
		user_obj = UserModel.objects.create_user(email=email, password=password)
		user_obj.username = username

		# Save the additional user information
		for key, value in validated_data.items():
			setattr(user_obj, key, value)

		# Save the user object
		user_obj.save()

		return user_obj
class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(max_length=128, write_only=True)
	def validate(self, attrs):
		email = attrs.get('email')
		password = attrs.get('password')

		if email and password:
			user = authenticate(email=email, password=password)
			if user:
				if not user.is_active:
					raise serializers.ValidationError('User account is disabled.')
				attrs['user'] = user
				refresh = RefreshToken.for_user(user)
				# Add the token to the response data
				attrs['token'] = {
					'refresh': str(refresh),
					'access': str(refresh.access_token),
				}
				return attrs
			else:
				raise serializers.ValidationError('Invalid email or password.')
		else:
			raise serializers.ValidationError('Must include "email" and "password".')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
