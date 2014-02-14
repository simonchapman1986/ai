install:
	pip install -r requirements.txt

cleandb:
	./src/manage.py syncdb

clean:
	pip freeze > old.freeze
	pip uninstall -r requirements.txt -y
