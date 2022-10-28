from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from article.models import Article
from article.serializers import ArticleSerializer, ArticleListSerializer, ArticleCreateSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)