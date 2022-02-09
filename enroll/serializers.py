from rest_framework import serializers
from .models import Class, Student, Teacher, Subject, User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ="__all__"

class SubjectSerializer(serializers.ModelSerializer):
    student_names = serializers.SerializerMethodField()
    class Meta:
        model=Subject
        # fields = ['id','subj_name', 'student','student_names']
        fields ="__all__"
    def get_student_names(self, subject):
        new_student=[]
        student = subject.student_name.all()
        for stu in student:
            new_student.append(stu.stu_name)
        return new_student
    # student_name = serializers.StringRelatedField(many=True)
    # student_name= serializers.SerializerMethodField(read_only=True)
    # student= StudentSerializer(many=True)
 
    # class Meta:
    #     model = Subject
    #     # fields =['id','subj_name','student']
    #     fields="__all__"
    
class TeacherSerializer(serializers.ModelSerializer):
    subject_name=serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields =['id','subject','tech_name','subject_name']
    def get_subject_name(self, teacher):
        subject = teacher.subject.subj_name
        return subject


class ClassSerializer(serializers.ModelSerializer):
    stues = serializers.SerializerMethodField()
    class Meta:
        model = Class
        fields =['id','stu','class_name','stues']
        # fields = "__all__"
    def get_stues(self, classs): #is main jo classs parameter ha ya Class model ko show kr ra ha
        student = classs.stu.stu_name # ya pahla Class model main jata ha phir is k bd us k attribute phr phr aga sa Student k model main sa jis attribute ko show krna ha
        return student
       

           # custom user model 
class RegisterSerializer(serializers.ModelSerializer):
    password =serializers.CharField(max_length =68, min_length=6, write_only =True)

    class Meta:
        model=User
        fields = ['email','username','password']
    
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError("the username contain alphanumeric")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)










# class StudentSerializer(serializers.Serializer):
#     stu_name = serializers.CharField(max_length=70)
#     subject = serializers.CharField(max_length = 70)
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.stu_name = validated_data.get('name',instance.name)
#         instance.subject = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance

# class SubjectSerializer(serializers.Serializer):
#     Student_name = serializers.ManyToManyField(Student, related_name ='student1')
#     subj_name = serializers.CharField(max_length=70)

# class TeacherSerializer(serializers.Serializer):
#     subject = serializers.OneToOneField(Subject, on_delete=models.CASCADE)
#     tech_name = serializers.CharField(max_length=70)

# class ClassSerializer(serializers.Serializer):
#     stu = serializers.ForeignKey(Student,on_delete=models.CASCADE)
#     class_name = serializers.CharField(max_length=70)


