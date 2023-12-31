from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from .serializers import EmailSerializer


class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)

        if serializer.is_valid():
            to_email = list(map(lambda addr: addr.strip(), serializer.validated_data['to_email'].split(",")))
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']

            send_mail(subject, message, 'info@pardehmahoor.ir', [to_email])

            return Response({'message': 'Success'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
