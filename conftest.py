"""Необязательные сетевые настройки браузера для управляемой среды."""

import os

import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Стандартный запуск и поддержка явно указанного корпоративного прокси."""
    options = dict(browser_type_launch_args)
    proxy_server = os.environ.get("PLAYWRIGHT_PROXY_SERVER")
    browser_home = os.environ.get("PLAYWRIGHT_BROWSER_HOME")
    if proxy_server:
        options["proxy"] = {"server": proxy_server}
    if browser_home:
        options["env"] = dict(os.environ, HOME=browser_home)
    return options
