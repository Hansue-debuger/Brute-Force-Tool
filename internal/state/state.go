package state

import (
	"encoding/json"
	"os"
)

type Checkpoint struct {
	Target    string `json:"target"`
	Position  int64  `json:"position"`
	Keyspace  int64  `json:"keyspace"`
	Completed int64  `json:"completed"`
}

func Load(path string) (*Checkpoint, error) {
	b, err := os.ReadFile(path)
	if err != nil {
		if os.IsNotExist(err) {
			return &Checkpoint{}, nil
		}
		return nil, err
	}
	var c Checkpoint
	if err := json.Unmarshal(b, &c); err != nil {
		return nil, err
	}
	return &c, nil
}

func Save(path string, c *Checkpoint) error {
	b, _ := json.MarshalIndent(c, "", "  ")
	return os.WriteFile(path, b, 0644)
}
