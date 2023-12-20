import unittest
from ..main.nb_handler import NBHandler

# Test default success message
def test_default_success():
    message = NBHandler.success("Az sum joro ignatov i tova e sudeben spor!")
    assert message == "ttt"