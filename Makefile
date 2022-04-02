build:
	protoc \
		--go_out=. \
		--go_opt=paths=source_relative \
		--go-grpc_out=. \
		--go-grpc_opt=paths=source_relative \
		--doc_out=./doc --doc_opt=markdown,docs.md \
		uggly.proto

