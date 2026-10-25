package config

import (
	"flag"
	"fmt"
)

type Config struct {
	Target     string
	ScopeFile  string
	Wordlist   string
	Mask       string
	Threads    int
	RPS        int
	ProxyFile  string
	OutputFile string
	StateFile  string
}

func Parse(args []string) (*Config, error) {
	c := &Config{}
	fs := flag.NewFlagSet("bruteforce", flag.ContinueOnError)
	fs.StringVar(&c.Target, "target", "", "target (host/url/hash)")
	fs.StringVar(&c.ScopeFile, "scope", "", "authorized scope file")
	fs.StringVar(&c.Wordlist, "wordlist", "", "wordlist path")
	fs.StringVar(&c.Mask, "mask", "", "mask pattern")
	fs.IntVar(&c.Threads, "threads", 4, "worker count")
	fs.IntVar(&c.RPS, "rps", 10, "requests per second")
	fs.StringVar(&c.ProxyFile, "proxies", "", "proxy pool file")
	fs.StringVar(&c.OutputFile, "output", "hits.txt", "success output")
	fs.StringVar(&c.StateFile, "state", "session.state", "checkpoint file")
	if err := fs.Parse(args); err != nil {
		return nil, err
	}
	if c.Target == "" {
		return nil, fmt.Errorf("--target required")
	}
	return c, nil
}
