import sys
from pathlib import Path

import pytest

# Add src/ to sys.path so we can import the application modules
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import web_app  # noqa: E402  # isort: skip
from tuomari import Tuomari  # noqa: E402  # isort: skip


@pytest.fixture
def app():
    return web_app.app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def reset_scoreboards():
    """Reset per-mode scoreboards before each test for isolation.

    Uses the existing Tuomari class to re-initialize the scoreboard
    instances, keeping behavior identical to the application.
    """
    if hasattr(web_app, "_SCOREBOARDS"):
        for key in list(web_app._SCOREBOARDS.keys()):
            web_app._SCOREBOARDS[key] = Tuomari()
    yield
    if hasattr(web_app, "_SCOREBOARDS"):
        for key in list(web_app._SCOREBOARDS.keys()):
            web_app._SCOREBOARDS[key] = Tuomari()
