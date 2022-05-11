# uggly
Protocol for TUIOW (terminal user interface over the wire)

Protobuf definition currently used for gRPC and is compiled for Golang and Python.

Docs are generated using the handy [protoc-gen-doc](https://github.com/pseudomuto/protoc-gen-doc) package and can be found [here](./doc).

See the samples folder for some "hello world" example servers in Go and Python. View them with the [uggly-client](https://github.com/rendicott/uggly-client). For more advanced server examples check out the following:

* [uggly-server](https://github.com/rendicott/uggly-server) - a server that hosts sites from static files. 
* [uggly-server-login](https://github.com/rendicott/uggly-server-login) - a server that gives examples of login flows and cookie usage
* [puggly-server](https://github.com/rendicott/puggly-server) - a python server that shows dynamic navigation of a CSV using keyboard shortcuts

## About Project
Uggly is a means to generate Terminal User Interfaces in a client-server architecture. Think of it as TUI over-the-wire (TUIOW). The client requests content from the server via gRPC protobuffers and the client handles rendering of that content. The server is sending "pages" of content one screen at a time. The protocol and page definitions take inspiration from CSS/HTML in that there are constructs such as DivBoxes, TextBlobs, Links, and Forms for example. It is opinionated in that only keyboard strokes are supported for link navigation.
