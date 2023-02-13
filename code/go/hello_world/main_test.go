package main

import (
	"bytes"
	"log"
	"strings"
	"testing"
)

func TestMain(t *testing.T) {
    var buf bytes.Buffer
    log.SetOutput(&buf)
    main()
    got := buf.String()
    want := "Hello, World!\n"
    if strings.HasSuffix(got, want) == false {
        t.Errorf("got %q want %q", got, want)
    }
}
