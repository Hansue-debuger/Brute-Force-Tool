package main

import (
	"fmt"
	"os"

	"bruteforce/internal/auth"
	"bruteforce/internal/config"
	"bruteforce/internal/engine"
)

func main() {
	cfg, err := config.Parse(os.Args[1:])
	if err != nil {
		fmt.Fprintln(os.Stderr, "config:", err)
		os.Exit(2)
	}
	if err := auth.Authorize(cfg.Target, cfg.ScopeFile); err != nil {
		fmt.Fprintln(os.Stderr, "authorization denied:", err)
		os.Exit(1)
	}
	eng := engine.New(cfg)
	if err := eng.Run(); err != nil {
		fmt.Fprintln(os.Stderr, "engine:", err)
		os.Exit(1)
	}
}
