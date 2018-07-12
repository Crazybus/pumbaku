VERSION := 1.0.0
IMAGE := 'crazybus/pumbaku:$(VERSION)'

build:
	docker build -t $(IMAGE) .

deploy: build
	docker push $(IMAGE)

run: build
	docker run \
		-e HAIKU_CHANNEL=$$HAIKU_CHANNEL \
		-e SLACK_BOT_TOKEN=$$SLACK_BOT_TOKEN \
		--rm -ti \
		$(IMAGE) \
		python3 pumbaku.py

test: build
	docker run \
		--rm -ti \
		$(IMAGE) \
		pytest

debug: build
	docker run \
		-e DEBUG=true \
		--rm -ti \
		$(IMAGE) \
		python3 pumbaku.py
