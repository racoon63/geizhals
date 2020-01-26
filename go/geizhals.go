package main

import (
	"crypto/tls"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {

	baseURL := "https://geizhals.de/gigabyte-geforce-rtx-2070-super-windforce-oc-3x-8g-gv-n207swf3oc-8gd-a2122943.html?hloc=at&hloc=de"

	config := &tls.Config{
		InsecureSkipVerify: true,
	}

	transport := &http.Transport{
		TLSClientConfig: config,
	}

	netClient := &http.Client{
		Transport: transport,
	}

	response, err := netClient.Get(baseURL)

	checkErr(err)

	body, err := ioutil.ReadAll(response.Body)
	checkErr(err)
	fmt.Println(string(body))

	response.Body.Close()
}

func checkErr(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
