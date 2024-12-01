app:
	hugo server --minify

syntax:
	hugo gen chromastyles --style=dracula > assets/css/syntax.css

PHMDOCTEST_DIR=.phmdoctest
test:
	rm -rf $(PHMDOCTEST_DIR)

	# TODO install pytest and phmdoctest
	phmdoctest pyproject.toml
	pytest $(PHMDOCTEST_DIR)

	# TODO - install shelldoc
	shelldoc run ./content/lessons/*.md

	# TODO - install pytest-playwright
	playwright install

