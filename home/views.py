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


def get_one(request,pk):
    if request.method=="GET":
        try:
            post = Blog.objects.all(pk=pk)
            serializer = BlogSerializer(post, many=False)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)

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
                        
    



class PublicBlog(APIView):
    def get(self,request):
        try:
            blogs = Blog.objects.all()
            
            if request.GET.get('search'):
                search = blogs.filter(Q(user__icontains=search)| Q(created_at__icontains=search))
            
            page_number = request.GET.get('page',1)
            paginator = Paginator(blogs,2)
            serializer = BlogSerializer(paginator.page(page_number),many=True)
            return Response({
                'data': serializer.data,
                'message': 'blogs fetched successfully'
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                    'data': {},
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
        
    
class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        try:
            blogs = Blog.objects.filter(user=request.user)
            
            if request.GET.get('search'):
                search = blogs.filter(Q(user__icontains=search)| Q(created_at__icontains=search))
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

    def patch(self,request):
        try:
            data = request.data
            blog = Blog.objects.filter(uid=data.get('uid'))
            if not blog.exists():
                return Response({
                    'data': {},
                    'message': 'invalid uid'
                },status=status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
                return Response({
                    'data': {},
                    'message': 'you are not authorized'
                },status=status.HTTP_400_BAD_REQUEST)
            
            serializer = BlogSerializer(blog[0],data=data, partial = True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                    'data': serializer.data,
                    'message': 'blog updated successfully'
                },status=status.HTTP_202_ACCEPTED
                )
        except Exception as e:
            return Response({
                    'data': {},
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)    
            

    def delete(self,request):
        try:
            data = request.data
            blog = Blog.objects.filter(uid=data.get('uid'))
            if not blog.exists():
                return Response({
                    'data': {},
                    'message': 'invalid uid'
                },status=status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
                return Response({
                    'data': {},
                    'message': 'you are not authorized'
                },status=status.HTTP_400_BAD_REQUEST)
            
            blog[0].delete()
            return Response({
                    'data': serializer.data,
                    'message': 'blog updated successfully'
                },status=status.HTTP_202_ACCEPTED
                )
        except Exception as e:
            return Response({
                    'data': {},
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)



        