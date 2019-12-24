from rest_framework import serializers
from rest_framework import Article

class ArticleSerializers(Serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'
