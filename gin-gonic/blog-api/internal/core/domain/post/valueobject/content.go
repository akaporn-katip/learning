package valueobject

type Content struct {
	Title   string `json:"title"`
	Body string `json:"body"`
	Publish bool   `json:"publish"`
}