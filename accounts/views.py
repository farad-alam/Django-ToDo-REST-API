from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import CustomUserSerializer, UserListSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# class UserCreateView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer


# class UserListView(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserListSerializer

class UserCreateListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Save the user using the serializer
        user = serializer.save()

        # Generate JWT tokens for the newly registered user
        refresh = RefreshToken.for_user(user)

        # Prepare response data
        self.response_data = {
            'user': CustomUserSerializer(user).data,  # User data
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Return response with JWT tokens
        return Response(self.response_data, status=status.HTTP_201_CREATED, headers=headers)

# class UserDetailedUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     lookup_field = 'id'


class UserDetailedUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]





# Password reset token generator
token_generator = PasswordResetTokenGenerator()

# Step 1: Request password reset
@api_view(['POST'])
def request_password_reset(request):
    email = request.data.get('email')
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Generate password reset token
    token = token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    # Create password reset link
    reset_link = f"{request.build_absolute_uri('/accounts/reset-account-password/')}?uid={uid}&token={token}"

    # Send email
    subject = "Password Reset Request"
    message = render_to_string('password_reset_email.html', {
        'reset_link': reset_link,
        'user': user
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

    return Response({'message': 'Password reset link sent to your email.'}, status=status.HTTP_200_OK)


def token_verify(uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=int(uid))
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)

    # Check the token
    if not token_generator.check_token(user, token):
        return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"message":'Token Verify Successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def verify_password_restet_token(request):
    uidb64 = request.data.get('uid')
    token = request.data.get('token')
    verify_token_status = token_verify(uidb64, token)
    return verify_token_status


# Step 2: Reset password
@api_view(['POST'])
def reset_password(request):
    uidb64 = request.data.get('uid')
    token = request.data.get('token')
    new_password = request.data.get('password')

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=int(uid))
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        return Response({'error': 'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)

    # Check the token
    if not token_generator.check_token(user, token):
        return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

    # Update the password
    user.password = make_password(new_password)
    user.save()

    return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)


# # Step 2: Reset password
# @api_view(['POST'])
# def reset_password(request):
#     uidb64 = request.data.get('uid')
#     token = request.data.get('token')
#     new_password = request.data.get('password')

#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = CustomUser.objects.get(pk=int(uid))
#     except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
#         return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)

#     # Check the token
#     if not token_generator.check_token(user, token):
#         return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

#     # Update the password
#     user.password = make_password(new_password)
#     user.save()

#     return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)



def registration_view(request):
    return HttpResponse('sound from accounts!!!')


def request_password_reset_view(request):
    return render(request, 'request_password_reset.html')

def reset_password_view(request):
    return render(request, 'reset_password.html')

