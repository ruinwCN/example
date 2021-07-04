package go_logger

import "testing"

func TestSugarLog(t *testing.T) {
	SugarLog()
}

func TestCoreLog(t *testing.T) {
	//CoreLog()
	InitLogger()
	Info("test%d", 123)

}
