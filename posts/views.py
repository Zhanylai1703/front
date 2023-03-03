from django.shortcuts import render

from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly, IsAIsAuthenticatedOrReadOnl


from .models import Post
from .serializers import PostSerializer
from user.models import User



# Create your views here.

class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAIsAuthenticatedOrReadOnl,
                          )
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ( IsAIsAuthenticatedOrReadOnl, )



class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAIsAuthenticatedOrReadOnl, )
