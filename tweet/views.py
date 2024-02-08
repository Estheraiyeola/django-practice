from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tweet, Comment
from .serializers import TweetSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from pagination import DefaultPagination
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
class TweetViewSet(ListCreateAPIView, RetrieveDestroyAPIView, GenericViewSet):
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated]
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentViewSet(ListCreateAPIView, RetrieveDestroyAPIView, GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.select_related("tweet").filter(tweet_id=self.kwargs["tweet_pk"])

# class TweetList(ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
#
# class TweetDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#

# class CommentList(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentDetail(RetrieveDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# def get_queryset(self):
#     return Tweet.objects.all()
#
# def get_serializer_class(self):
#     return TweetSerializer

# def get(self, request):
#     tweets = Tweet.objects.all()
#     serializer = TweetSerializer(tweets, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def post(self, request):
#     serializer = TweetSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(["GET", "POST"])
# def tweet_list(request):
#     if request.method == "GET":
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         serializer = TweetSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class TweetDetail(APIView):
#     def get(self, request, pk):
#         tweet = get_object_or_404(Tweet, id=pk)
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request,pk):
#         tweet = get_object_or_404(Tweet, id=pk)
#         serializer = TweetSerializer(tweet, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         tweet = get_object_or_404(Tweet, id=pk)
#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "PUT", "DELETE"])
# def tweet_detail(request, pk):
#     tweet = get_object_or_404(Tweet, id=pk)
#     if request.method == "GET":
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         serializer = TweetSerializer(tweet, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#     elif request.method == "DELETE":
#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
