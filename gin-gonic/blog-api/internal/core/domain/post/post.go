package post

import "github.com/learning/gin-gonic/blog-api/internal/core/domain/post/valueobject"

type PostAggregate struct {
	Content valueobject.Content
}

func NewPost(title string, body string, publish bool) PostAggregate {
	post := PostAggregate{
		Content: valueobject.Content{
			Title:   title,
			Body:    body,
			Publish: publish,
		},
	}

	return post
}

func (p PostAggregate) Publish() {
	p.Content.Publish = true
}

func (p PostAggregate) Draft() {
	p.Content.Publish = false
}
