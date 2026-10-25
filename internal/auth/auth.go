package auth

import (
	"bufio"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"os"
	"strings"
)

// Scope represents an authorized engagement.
type Scope struct {
	Targets []string
	Hash    string // SHA-256 of signed scope document
}

// Authorize verifies the target is within an approved, signed scope file.
func Authorize(target, scopeFile string) error {
	if scopeFile == "" {
		return fmt.Errorf("scope file required (--scope)")
	}
	f, err := os.Open(scopeFile)
	if err != nil {
		return err
	}
	defer f.Close()

	var targets []string
	sc := bufio.NewScanner(f)
	for sc.Scan() {
		line := strings.TrimSpace(sc.Text())
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}
		targets = append(targets, line)
	}
	if err := sc.Err(); err != nil {
		return err
	}
	for _, t := range targets {
		if t == target {
			return nil
		}
	}
	return fmt.Errorf("target %q not in authorized scope", target)
}

// VerifyScopeHash checks a scope document's integrity hash.
func VerifyScopeHash(path, expected string) error {
	b, err := os.ReadFile(path)
	if err != nil {
		return err
	}
	h := sha256.Sum256(b)
	if hex.EncodeToString(h[:]) != expected {
		return fmt.Errorf("scope hash mismatch")
	}
	return nil
}
