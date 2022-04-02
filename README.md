# uggly
Protocol for TUIOW (terminal user interface over the wire)

Protobuf definition currently used for gRPC and is compiled for Golang.

Docs are generated using the handy [protoc-gen-doc](https://github.com/pseudomuto/protoc-gen-doc) package and can be found [here](./doc).

See [uggly-client](https://github.com/rendicott/uggly-client) and [uggly-server](https://github.com/rendicott/uggly-server) for usage examples.

## About Project
Uggly is a means to generate Terminal User Interfaces in a client-server architecture. Think of it as TUI over-the-wire (TUIOW). The client requests content from the server via gRPC protobuffers and the client handles rendering of that content. The server is sending "pages" of content one screen at a time. The protocol and page definitions take inspiration from CSS/HTML in that there are constructs such as DivBoxes, TextBlobs, Links, and Forms for example. It is opinionated in that only keyboard strokes are supported for link navigation.
