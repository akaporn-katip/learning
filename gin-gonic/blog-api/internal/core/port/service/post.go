package service

import (
	"github.com/learning/gin-gonic/blog-api/internal/core/dto/request"
	"github.com/learning/gin-gonic/blog-api/internal/core/dto/response"
)

type PostService interface {
	CreatePost(request *request.CreatePostRequest) *response.Response
}
