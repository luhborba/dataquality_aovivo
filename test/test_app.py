"""Arquivo de testes da interface visual."""

import subprocess
from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Inicia o navegador."""
    process = subprocess.Popen(["streamlit", "run", "app.py"])

    driver = webdriver.Firefox()
    driver.get("http://localhost:8501")
    driver.set_page_load_timeout(10)

    yield driver

    driver.quit()
    process.kill()


def test_app_open(driver):
    """Testa se a interface visual está aberta."""
    driver.get("http://localhost:8501")
    sleep(3)


def test_app_title(driver):
    """Testa se o tiítulo da interface visual está correto."""
    driver.get("http://localhost:8501")
    sleep(3)
    assert driver.title == "Validação de CSV"
