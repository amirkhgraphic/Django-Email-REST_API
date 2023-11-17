from rest_framework.serializers import Serializer, EmailField, CharField

class EmailSerializer(Serializer):
    to_email = EmailField()
    subject = CharField()
    message = CharField()
