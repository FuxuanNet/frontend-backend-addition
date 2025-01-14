package main

import (
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"net/http"
)

func add(num1, num2 float32) float32 {
	return num1 + num2
}

func UsingAddFunction(c *gin.Context) {
	var Data struct {
		Num1 float32 `json:"num1"`
		Num2 float32 `json:"num2"`
	}
	if err := c.ShouldBindJSON(&Data); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	result := add(Data.Num1, Data.Num2)

	c.JSON(http.StatusOK, gin.H{"result": result})
}

func main() {
	r := gin.Default()

	r.Use(cors.Default())

	r.POST("/api/add", UsingAddFunction)

	r.Run(":5000")
}
