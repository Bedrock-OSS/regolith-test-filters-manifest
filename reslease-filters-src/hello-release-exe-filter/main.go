package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	filePath := filepath.Join("BP", "hello_release_exe_filter.txt")
	content := "Hello from hello-release-exe-filter!"

	// Create and write to the file
	file, err := os.Create(filePath)
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer file.Close()

	if _, err := file.WriteString(content); err != nil {
		fmt.Println("Error writing to file:", err)
		return
	}

	fmt.Println("File created successfully:", filePath)
}
