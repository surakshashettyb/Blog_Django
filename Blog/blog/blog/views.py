from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from articles.models  import Article
from .serializers import ArticleSerializers


def homepage(request):
	#return HttpResponse('homepage')
	return render(request,'homepage.html')
def about(request):
	#return HttpResponse('about')
	return render(request,'about.html')

class ArticleList(APIView):
	def get(self, request):
		Article1= Article.objects.all()
		serializer = ArticleSerializers(Article1,many=True)
		return Response(serializer.data)
	def post(self):
		pass

