from rest_framework.decorators import api_view
from rest_framework.response import Response
from book.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/books',
        'GET /api/books/:id'
    ]
    
    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    
    book = Book.objects.all()
    
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getBook(request, pk):
   
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

