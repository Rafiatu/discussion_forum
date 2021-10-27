import datetime as dt
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Post
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import PostSerializer


class PostView(ViewSet):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    @action(detail=False, methods=["POST"])
    def new(self, request) -> HttpResponseRedirect or Response:
        """
        create a new post. The endpoint takes just the post and the title.
        :param request: The HTTP Request
        :return: HTTP Response redirects to the details endpoint of the newly created post.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data["title"]
            content = serializer.validated_data["content"]
            try:
                post = Post.objects.create(
                        title=title,
                        content=content,
                        author=request.user
                    )
                post.save()
                return HttpResponseRedirect(reverse('posts-details', args=[str(post.id)]))
            except Exception as error:
                return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["GET"], permission_classes=[AllowAny])
    def all(self, request) -> Response:
        """
        Retrieves and presents all posts from the database.
        :param request: HTTP request
        :return: Response with relevant success or error message.
        """
        try:
            posts = Post.objects.all()
            serializer = self.serializer_class(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["PUT", "PATCH"])
    def edit(self, request, pk: str) -> Response:
        """
        Edit a post based on its id.
        :param request: HTTP Request
        :param pk: The id of the post to be edited.
        :return:
        """
        try:
            post = get_object_or_404(Post, id=pk)
            serializer = self.serializer_class(data=request.data)
            if request.user != post.author:
                return Response({"error": "Only the Author can edit this post"}, status=status.HTTP_403_FORBIDDEN)
            if serializer.is_valid():
                post.title = serializer.validated_data["title"]
                post.content = serializer.validated_data["content"]
                post.updated_at = dt.datetime.now()
                post.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["GET"])
    def like(self, request, pk: str) -> HttpResponseRedirect or Response:
        """
        Endpoint for liking and unliking posts by their id
        :param request: HTTP request
        :param pk: The id of the Post to be liked
        :return: Response redirect to the details of the post that was just liked/disliked.
        """
        try:
            post = get_object_or_404(Post, id=pk)
            if post.liked_by.filter(id=request.user.id).exists():
                post.liked_by.remove(request.user)
            else:
                post.liked_by.add(request.user)
            return HttpResponseRedirect(reverse('posts-details', args=[str(pk)]))
        except Exception as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["GET"])
    def details(self, request, pk: str) -> Response:
        """
        Fetches and returns details of a particular post.
        :param request: HTTP Request
        :param pk: The id of the post to be gotten.
        :return: Response with the details of the post.
        """
        post = get_object_or_404(Post, id=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET", "DELETE"])
    def delete(self, request, pk: str):
        """
        Delete a post by its id
        :param request: HTTP Request
        :param pk: The id of the post to be deleted.
        :return: Response with success message
        """
        try:
            post = get_object_or_404(Post, id=pk)
            if request.user != post.author:
                return Response({"error": "Only the Author can edit this post"}, status=status.HTTP_403_FORBIDDEN)
            post.delete()
            return Response({"success": "Post successfully deleted"}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
