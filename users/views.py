from django.shortcuts import render
import json

from rest_framework.viewsets import ViewSet

from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets

from .models import user
from .serializers import UploadSerializer,UserSerializer

from rest_framework.decorators import action

# Create your views here.

from django.shortcuts import render

def dashboard(request):
    return render(request, "users/dashboard.html")




# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    # parser_class = (FileUploadParser,)


    def list(self, request):
        return response.Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        newFile = json.load(file_uploaded)
        print("yolo")
        print(newFile[0])
        for line in NewFile:
            u=user()
            u.id=line.id
            u.title=line.title

            u.save()

        # newRec = Users() ------- model definition
        # newRec.id = 1 --------- sendong valies to db
        # newRec.name = "Venkat" sending value to db
        # newRec.save() saving in db

        # user.my_file_field.save(, f, save=True)

        response1 = "POST API and you have uploaded a {} file".format(content_type)   
        return response.Response(response1)
   
    @action(
        detail=True,
        methods=['PUT'],
        serializer_class=UploadSerializer,
        parser_classes=[parsers.MultiPartParser],
    )
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = user.objects.all()

#     @action(
#         detail=True,
#         methods=['PUT'],
#         serializer_class=UploadSerializer,
#         parser_classes=[parsers.MultiPartParser],
#     )
#     def pic(self, request, pk):
#         obj = self.get_object()
#         serializer = self.serializer_class(obj, data=request.data,
#                                            partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data)
#         return response.Response(serializer.errors,
#                                  status.HTTP_400_BAD_REQUEST)