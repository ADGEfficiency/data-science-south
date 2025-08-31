app:
	hugo server --disableFastRender

PHMDOCTEST_DIR=.phmdoctest
test:
	rm -rf $(PHMDOCTEST_DIR)

	# TODO install pytest and phmdoctest
	uv run phmdoctest pyproject.toml
	pytest $(PHMDOCTEST_DIR)

	# TODO - install shelldoc
	shelldoc run ./content/lessons/*.md

	# TODO - install pytest-playwright
	playwright install

search:
	npx -y pagefind --site public

build:
	hugo --gc --minify

deploy: syntax build search

SYNTAX=github-dark
syntax:
	hugo gen chromastyles --style=$(SYNTAX) > assets/css/syntax.css
