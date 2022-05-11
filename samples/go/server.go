package main

import (
	"context"
	"flag"
	"fmt"
	pb "github.com/rendicott/uggly"
	"google.golang.org/grpc"
	"log"
	"net"
)

var (
	port       = flag.Int("port", 10000, "The server port")
)


// convertStringCharRune takes a string and converts it to a rune slice
// then grabs the rune at index 0 in the slice so that it can return
// an int32 to satisfy the Uggly protobuf struct for border and fill chars
// and such. If the input string is less than zero length then it will just
// rune out a space char and return that int32.
func convertStringCharRune(s string) int32 {
	if len(s) == 0 {
		s = " "
	}
	runes := []rune(s)
	return runes[0]
}

/* GetPage implements the Page Service's GetPage method as required in the protobuf definition.

It is the primary listening method for the server. It accepts a PageRequest and then attempts to build
a PageResponse which the client will process and display on the client's pcreen. 
*/
func (s pageServer) GetPage(ctx context.Context, preq *pb.PageRequest) (presp *pb.PageResponse, err error) {
	presp = &pb.PageResponse{
		Name: "hello-world",
		DivBoxes: &pb.DivBoxes{},
		Elements: &pb.Elements{},
	}
	presp.DivBoxes.Boxes = append(presp.DivBoxes.Boxes, &pb.DivBox{
		Name:     "hello-world-div",
		Border:   false,
		// FillChar needs to be a rune so we use the helper function
		FillChar: convertStringCharRune("_"),
		StartX:   10,
		StartY:   10,
		Width:    20,
		Height:   10,
		FillSt: &pb.Style{ // fill style for the div box
			Fg:   "grey",
			Bg:   "darkgrey",
			Attr: "4", // attr is straight from tcell and can be used for underline, etc
		},
	})
	presp.Elements.TextBlobs = append(presp.Elements.TextBlobs, &pb.TextBlob{
		Content: "hello world",
		Style: &pb.Style{
			Fg: "red",
			Bg: "darkgrey",
			Attr: "4",
		},
		DivNames: []string{"hello-world-div"},
	})
	return presp, err
}

/* newPageServer takes the loaded pageconfig YAML and converts it to the structs
required so that the GetPage method can adequately respond with a PageResponse.
*/
func newPageServer() *pageServer {
	return &pageServer{}
}


/* pageServer is a struct from which to attach the required methods for the Page Service
as defined in the protobuf definition
*/
type pageServer struct {
	pb.UnimplementedPageServer
}


func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf("0.0.0.0:%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	var opts []grpc.ServerOption
	grpcServer := grpc.NewServer(opts...)
	s := newPageServer()
	pb.RegisterPageServer(grpcServer, *s)
	log.Println("Server listening")
	grpcServer.Serve(lis)
}
