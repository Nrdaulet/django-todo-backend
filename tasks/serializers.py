import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'








# class TaskModel:
#     def __init__(self, title, description):
#         self.title=title
#         self.description=description





# def encode():
#     model= TaskModel('Do Homework', 'Do homework before dinner and finish last lab')
#     model_sr=TaskSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data) 
#     print(json)

# def decode():
#     stream=io.ByteIO(b'{"title":"Do Homework","description":"Do homework before dinner and finish last lab"}')
#     data= JSONParser().parse(stream)
#     serializers=TaskSerializer(data=data) 
#     serializers.is_valid()
#     print(serializers.validated_data)   