test:
	python -m unittest discover 

all:
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."
	rm -rf __pychache__ .pytest_cache

