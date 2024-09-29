from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BlogSerializer
from .models import Blog
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_all(request):
    if request.method=="GET":
        blogs = Blog.objects.all()
        p = Paginator(blogs, 5)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)
        context = {'page_obj': page_obj}
        # sending the page object to index.html
        return render(request, 'index.html', context)    
    
    
class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        try:
            blogs = Blog.objects.filter(user=request.user)
            
            if request.GET.get('search'):
                search = blogs.filter(Q(title__icontains=search)| Q(blog_text__icontains=search))
            serializer = BlogSerializer(blogs, many=True)

            return Response({
                'data': serializer.data,
                'message': 'blogs fetched successfully'
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                    'data': {},
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
        


    def post(self,request):
        try:
            data = request.data
            data['user'] = request.user.id

            serializer = BlogSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                    'data': serializer.data,
                    'message': 'blog created successfully'
                },status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response({
                    'data': {},
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
                



        