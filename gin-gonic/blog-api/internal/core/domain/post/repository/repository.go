package repository

type PostRepository interface {
	Insert() (string, error)
	Add() error
}
