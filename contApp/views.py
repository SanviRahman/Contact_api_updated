from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contact
from .serializers import ContactSerializer


class ContactAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        contact=Contact.objects.all()
        serializer=ContactSerializer(contact,many=True)
        return Response(serializer.data)


    #write a code for post
    def post(self, request):
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
