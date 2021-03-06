from django.http import Http404
from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CommentList(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModifyComment(APIView):

    def get_by_id(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment_id = self.get_by_id(pk)
        serializer = CommentSerializer(comment_id)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        comment_id = self.get_by_id(pk)
        comment_id.likes += 1
        serializer = CommentSerializer(comment_id, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        comment_id = self.get_by_id(pk)
        serializer = CommentSerializer(comment_id, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment_id = self.get_by_id(pk)
        deleteComment = CommentSerializer(comment_id)
        comment_id.delete()
        return Response(deleteComment.data, status=status.HTTP_200_OK)
