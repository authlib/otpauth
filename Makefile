.PHONY: clean-pyc clean-build docs test coverage

test:
	@nosetests -s

coverage:
	@rm -f .coverage
	@nosetests --with-coverage --cover-package=otpauth --cover-html

clean: clean-build clean-pyc clean-docs


clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info


clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-docs:
	@rm -fr  docs/_build

docs:
	@$(MAKE) -C docs html

publish-docs: docs
	@python setup.py upload_sphinx --upload-dir=docs/_build/html/
