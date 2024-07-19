package gamesrv

type service struct {}

func New() *service {
  return &service{}
}


func (srv *service) Get(id string) (domain.Game, error) {
  return domain.Game{}, nil
}

