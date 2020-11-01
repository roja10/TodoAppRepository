from django.shortcuts import render

# Create your views here.



from django.shortcuts import render
from rest_framework import generics, status,views
from rest_framework.response import Response
from todo.models import Todo
from todo.serializers import TodoSerializer
from django.http import JsonResponse




# Method to create and list the to-do list
# className ---> TodoCreateListView
class TodoCreateListView(views.APIView):

  '''
  queryset=Todo.objects.all()
  serializer_class= TodoSerializer
  '''
  def get(self,request):
    obj=Todo.objects.all()
    serialize=TodoSerializer(obj,many=True)
    return Response(serialize.data)
  def post(self,request):
    if(request.data['title']==''or request.data['description']==''):
      data={'title':["This field may not be blank."],'description':["This field may not be blank."]}
      return JsonResponse(data)
    serialize=TodoSerializer(data=request.data)
    if(serialize.is_valid()):
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)



'''
class TodoUpdateDeleteView(generics.UpdateAPIView,generics.DestroyAPIView):

  queryset=Todo.objects.all()
  serializer_class=TodoSerializer
'''

class TodoUpdateDeleteView(views.APIView):

  def get(self,request,id):
    try:
      obj=Todo.objects.get(id=id)
      serialize = TodoSerializer(obj)
      return Response(serialize.data)
    except Todo.DoesNotExist:
      data={"detail": "Not found."}
      return Response(data,status=404)



  def patch(self,request,id):
    try:

      obj=Todo.objects.get(id=id)

      serialize=TodoSerializer(obj,data=request.data,partial=True)
      if(serialize.is_valid()):
          serialize.save()
          return Response(serialize.data, status=status.HTTP_200_OK)
    except Todo.DoesNotExist:
      data={"detail": "Not found."}
      return Response(data,status=404)


  def delete(self,request,id):
    try:
      obj=Todo.objects.get(id=id)
      obj.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    except Todo.DoesNotExist:
      data={"detail": "Not found."}
      return Response(data,status=404)





# Method to update and delete the to-do list
# className ---> TodoUpdateDeleteView





