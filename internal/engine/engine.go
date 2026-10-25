package engine

import (
	"fmt"

	"bruteforce/internal/config"
)

type Engine struct {
	Cfg *config.Config
}

func New(c *config.Config) *Engine { return &Engine{Cfg: c} }

func (e *Engine) Run() error {
	fmt.Printf("engine started: target=%s threads=%d rps=%d\n", e.Cfg.Target, e.Cfg.Threads, e.Cfg.RPS)
	// TODO: orchestrate worker pool, wordlist stream, state checkpoint
	return nil
}
