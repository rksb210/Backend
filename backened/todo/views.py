from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly



# FUNCTION BASED VIEWS
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def todolist(request):
    task = Todo.objects.all()
    serializer = TodoSerializer(task, many=True)
    return Response(serializer.data)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
@api_view(['GET'])
def tododetail(request,pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(task, many=False)
    return Response(serializer.data)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def todocreate(request):   
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def todoupdate(request,pk):
    task = Todo.objects.get(id=pk)   
    serializer = TodoSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def tododelete(request,pk):
    task = Todo.objects.get(id=pk)   
    task.delete()
    return Response('item deleted')


# CLASS BASAED VIEWS

class todolist(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class todocreate(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class todoretrieve(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class todoupdate(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class tododestroy(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]









# Create your views here.
