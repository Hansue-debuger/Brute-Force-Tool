package wordlist

import (
	"bufio"
	"os"
)

// Stream reads a wordlist line-by-line without loading into RAM.
func Stream(path string, fn func(line string) bool) error {
	f, err := os.Open(path)
	if err != nil {
		return err
	}
	defer f.Close()
	sc := bufio.NewScanner(f)
	sc.Buffer(make([]byte, 1024*1024), 1024*1024)
	for sc.Scan() {
		if !fn(sc.Text()) {
			break
		}
	}
	return sc.Err()
}
