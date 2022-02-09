from django.shortcuts import render
from .serializers import StudentSerializer, SubjectSerializer, TeacherSerializer, ClassSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.views import APIView # For class based view
from rest_framework import status
from .models import Student,Subject,Teacher,Class
# Create your views here.





# class Register(APIView):
# # --------------------------------------------------------POST----------------------------------
#     def post(self, request, format = None):
#         serializer = RegisterSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data has been created'}, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)








class StudentAPI(APIView):
    # authentication_classes=[TokenAuthentication]
    # # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
    # --------------------------------------------------GET-------------------------------------
    def get(self, request, format = None, pk = None):
        # id = request.data.get('id')
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
# --------------------------------------------------------POST----------------------------------
    def post(self, request, format = None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        #    -----------------------------------------------PUT-------------------------------------
    def put(self, request, format = None):
        id = request.data.get('id')
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# ----------------------------------------------PATCH---------------------------------------------------
    def patch(self, request, format = None):
        id = request.data.get('id')
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# --------------------------------------------------------------DELETE--------------------------------------
    def delete(self, request, format = None, pk=None):
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(pk=id)
            stu.delete()
            return Response(serializer.data)
        return Response({'msg':'Error in delete'})




# ---------------------------------------------------Subject Class------------------------------------------------




class SubjectAPI(APIView):
    # serializer_class = SubjectSerializer
    # def get_queryset(self):
    #     return super().get_queryset().select_related('relation').prefetch_related('relation__student_name')

    def get(self, request, format = None):
        id = request.data.get('id')
        if id is not None:
            stu = Subject.objects.get(id=id)
            serializer = SubjectSerializer(stu)
            return Response(serializer.data)
        stu = Subject.objects.all()
        serializer = SubjectSerializer(stu, many = True)
        return Response(serializer.data)


    def post(self, request, format = None):
        serializer = SubjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
           

    def put(self, request, format = None):
        id = request.data.get('id')
        stu = Subject.objects.get(pk = id)
        serializer = SubjectSerializer(stu, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




    def patch(self, request, format = None):
        id = request.data.get('id')
        stu = Subject.objects.get(pk = id)
        serializer = SubjectSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




    def delete(self, request, format = None):
        id = request.data.get('id')
        if id is not None:
            stu = Subject.objects.get(pk=id)
            stu.delete()
            return Response(serializer.data)
        return Response({'msg':'Error in delete'})







# ----------------------------------------- Teacher Data------------------------------------


class TeacherAPI(APIView):
    # --------------------------------------------------GET-------------------------------------
    def get(self, request, format = None):
        id = request.data.get('id')
        if id is not None:
            stu = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(stu)
            return Response(serializer.data)
        stu = Teacher.objects.all()
        serializer = TeacherSerializer(stu, many = True)
        return Response(serializer.data)
# --------------------------------------------------------POST----------------------------------
    def post(self, request, format = None):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        #    -----------------------------------------------PUT-------------------------------------
    def put(self, request, format = None):
        id = request.data.get('id')
        stu = Teacher.objects.get(pk = id)
        serializer = TeacherSerializer(stu, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# ----------------------------------------------PATCH---------------------------------------------------
    def patch(self, request, format = None):
        id = request.data.get('id')
        stu =Teacher.objects.get(pk = id)
        serializer = TeacherSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# --------------------------------------------------------------DELETE--------------------------------------
    def delete(self, request, format = None):
        id = request.data.get('id')
        if id is not None:
            stu = Teacher.objects.get(pk=id)
            stu.delete()
            return Response(serializer.data)
        return Response({'msg':'Error in delete'})


# ------------------------------------------------Class Data----------------------------------------------------


class ClassAPI(APIView):
    #        -------------------------------------------------GET-------------------------------------
    def get(self, request, format = None):
        id = request.data.get('id')
        if id is not None:
            stu = Class.objects.get(id=id)
            serializer = ClassSerializer(stu)
            return Response(serializer.data)
        stu = Class.objects.all()
        serializer = ClassSerializer(stu, many = True)
        return Response(serializer.data)
# --------------------------------------------------------POST----------------------------------
    def post(self, request, format = None):
        serializer = ClassSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        #    -----------------------------------------------PUT-------------------------------------
    def put(self, request, format = None):
        id = request.data.get('id')
        stu = Class.objects.get(pk = id)
        serializer = ClassSerializer(stu, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# ----------------------------------------------PATCH---------------------------------------------------
    def patch(self, request, format = None):
        id = request.data.get('id')
        stu =Class.objects.get(pk = id)
        serializer = ClassSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# --------------------------------------------------------------DELETE--------------------------------------
    def delete(self, request, format = None):
        id = request.data.get('id')
        if id is not None:
            stu = Class.objects.get(pk=id)
            stu.delete()
            return Response(serializer.data)
        return Response({'msg':'Error in delete'})
