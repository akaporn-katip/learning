package response

import "github.com/learning/gin-gonic/blog-api/internal/core/entity/error_code"

type Response struct {
	Data         interface{}          `json:"data"`
	Status       bool                 `json:"status"`
	ErrorCode    error_code.ErrorCode `json:"errorCode"`
	ErrorMessage string               `json:"errorMessage"`
}

type BlogCreatedResponse struct {
	PostID string `json:"postId"`
}

type IdResponse struct {
  Id string `json:"id"`
}
