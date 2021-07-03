package color

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestColorFormatting(t *testing.T) {
	assert.Equal(
		t,
		"\x1b[31mfoo\x1b[0m",
		Red.Add("foo"),
		"Unexpected colored output.",
	)
}

func TestColor_Add(t *testing.T) {
	fmt.Println(Red.Add("foo"))
	fmt.Println(Blue.Add("foo"))
	fmt.Println(Magenta.Add("foo"))
	fmt.Println(Cyan.Add("foo"))
}
