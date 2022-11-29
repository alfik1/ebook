from dataclasses import fields
from .models import Ebooks
from rest_framework import serializers

class EbookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ebooks
        fields = '__all__'
    
    def validate(self, attrs):
        print('welcome')
        author = attrs.get('author',None)
        title = attrs.get('title',None)
        genre = attrs.get('genre',None)
        review = attrs.get('review',None)
        print(author,title,genre,review)
        if author == None or title == None or genre == None or review == None:
            serializers.ValidationError('missing fields')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        return Ebooks.objects.create(**validated_data)



