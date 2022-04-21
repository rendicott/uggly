version := 0.1.1

release: build push

build:
	protoc \
		--go_out=. \
		--go_opt=paths=source_relative \
		--go-grpc_out=. \
		--go-grpc_opt=paths=source_relative \
		--doc_out=./doc --doc_opt=markdown,README.md \
		uggly.proto

push:
	git add uggly.proto
	git add README.md
	git add Makefile
	git add ./doc
	git add uggly*.go
	git tag v$(version)
	git push origin v$(version)
	git commit -m "update"
	git push origin master
