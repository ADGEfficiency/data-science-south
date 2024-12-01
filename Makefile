app:
	hugo server --minify

syntax:
	hugo gen chromastyles --style=dracula > assets/css/syntax.css

PHMDOCTEST_DIR=.phmdoctest
test:
	rm -rf $(PHMDOCTEST_DIR)
	phmdoctest pyproject.toml
	pytest $(PHMDOCTEST_DIR)
	shelldoc run ./content/lessons/*.md
