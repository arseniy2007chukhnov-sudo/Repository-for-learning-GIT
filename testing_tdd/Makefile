.PHONY: help venv install install-dep test test-cov build clean publish-testpypi create-structure

ifeq ($(OS),Windows_NT)
    VENV = .venv
    PYTHON = $(VENV)\Scripts\python.exe
    PIP = $(VENV)\Scripts\pip.exe
    ACTIVATE = $(VENV)\Scripts\activate
    RM_DIR = rmdir /s /q
    MKDIR = mkdir
else
    VENV = .venv
    PYTHON = $(VENV)/bin/python
    PIP = $(VENV)/bin/pip
    ACTIVATE = source $(VENV)/bin/activate
    RM_DIR = rm -rf
    MKDIR = mkdir -p
endif

help:
	@echo "Доступные команды:"
	@echo "  make venv              - Создать виртуальное окружение"
	@echo "  make install           - Установить пакет (editable)"
	@echo "  make install-dep       - Установить зависимости"
	@echo "  make test              - Запустить тесты"
	@echo "  make build             - Собрать пакет"
	@echo "  make publish-testpypi  - Опубликовать на TestPyPI"
	@echo "  make clean             - Очистить артефакты"
	@echo "  make create-structure  - Создать структуру проекта"

create-structure:
	@echo "📁 Создаём структуру проекта..."
	$(MKDIR) src\your_package 2>nul || $(MKDIR) -p src/your_package
	$(MKDIR) docs 2>nul || $(MKDIR) -p docs
	$(MKDIR) tests 2>nul || $(MKDIR) -p tests
	echo "# Domain Documentation" > docs/DOMAIN.md
	echo "# your_package" > src/your_package/__init__.py
	echo "__version__ = \"0.1.0\"" >> src/your_package/__init__.py
	echo "# Tests" > tests/__init__.py
	echo "def test_placeholder(): pass" > tests/test_main.py
	echo "# Dependencies" > requirements.txt
	echo "pytest>=7.0" >> requirements.txt
	echo "ruff>=0.1" >> requirements.txt
	echo "mypy>=1.0" >> requirements.txt
	touch src/.gitkeep tests/.gitkeep 2>nul || type nul > src/.gitkeep && type nul > tests/.gitkeep
	@echo " Структура создана!"

venv:
	@echo " Создаём виртуальное окружение..."
	python -m venv $(VENV)
	@echo " Готово! Активируйте: $(ACTIVATE)"

install:
	@echo " Устанавливаем пакет в режиме editable..."
	$(PIP) install -e .

install-dep:
	@echo "📥 Устанавливаем зависимости..."
	$(PIP) install -r requirements.txt

install-dev: install install-dep
	$(PIP) install pytest-cov black ruff mypy build twine


test:
	@echo " Запускаем тесты..."
	$(PYTHON) -m pytest tests/ -v


build:
	@echo " Собираем дистрибутивы..."
	$(PIP) install build
	$(PYTHON) -m build

clean:
	@echo " Очищаем артефакты..."
	$(RM_DIR) dist build *.egg-info 2>nul || true
	$(RM_DIR) .pytest_cache .mypy_cache .ruff_cache htmlcov 2>nul || true
	@echo " Очистка завершена"

publish-testpypi: build
	@echo " Публикуем на TestPyPI..."
	$(PIP) install twine
	@echo "  Убедитесь, что ~/.pypirc настроен с токеном TestPyPI"
	twine upload --repository testpypi dist/*
	@echo " Опубликовано! Проверьте: https://test.pypi.org/project/your-package/"
\
all: venv install-dev lint typecheck test build
	@echo " Все проверки пройдены! Готово к публикации."