version := 0.1.3

release: build push

build: go python

prereq:
	pip install grpcio-tools
	pip install "betterproto[compiler]"

go:
	protoc \
		--go_out=. \
		--go_opt=paths=source_relative \
		--go-grpc_out=. \
		--go-grpc_opt=paths=source_relative \
		--doc_out=./doc --doc_opt=markdown,README.md \
		uggly.proto

python: 
	mkdir python
	python3 \
		-m grpc_tools.protoc \
		-I . \
		--python_betterproto_out=python \
		--grpc_python_out=python \
		uggly.proto

push:
	git add uggly.proto
	git add python
	git add README.md
	git add Makefile
	git add ./doc
	git add uggly*.go
	git tag v$(version)
	git push origin v$(version)
	git commit -m "update"
	git push origin master
