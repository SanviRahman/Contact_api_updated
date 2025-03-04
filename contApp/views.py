from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contact
from .serializers import ContactSerializer


class ContactCreateAPIView(APIView):
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


class ContactDeatilsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #write a code for get
    def get_object(self,pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request):
        contact=Contact.objects.all()
        serializer=ContactSerializer(contact,many=True)
        return Response(serializer.data)
    

    #write a code for put
    def put(self,request,pk):
        contact=self.get_object(pk)
        serializer=ContactSerializer(contact,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    #write a code for delete
    def delete(self,request,pk):
        contact=self.get_object(pk)
        contact.delete()
        return Response({'Message: Delete Successfull'}, status=status.HTTP_204_NO_CONTENT)