package request

type CreatePostRequest struct {
	Title   string `json:"title"`
	Content string `json:"content"`
	Publish bool   `json:"publish"`
}
