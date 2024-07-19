package service

import (
	"github.com/learning/gin-gonic/blog-api/internal/core/domain/post/repository"
	"github.com/learning/gin-gonic/blog-api/internal/core/dto/request"
	"github.com/learning/gin-gonic/blog-api/internal/core/dto/response"
	"github.com/learning/gin-gonic/blog-api/internal/core/entity/error_code"
	"github.com/learning/gin-gonic/blog-api/internal/core/port/service"
)

type postService struct {
	postRepo repository.PostRepository
}

func (u postService) CreatePost(request *request.CreatePostRequest) *response.Response {

	Id, err := u.postRepo.Insert()

	if err != nil {
		panic(err)
	}

	return &response.Response{
		Data: response.BlogCreatedResponse{
			PostID: Id,
		},
		Status:       false,
		ErrorCode:    error_code.Success,
		ErrorMessage: "",
	}
}

func NewPostService(postRepo repository.PostRepository) service.PostService {
	return &postService{
		postRepo: postRepo,
	}
}
