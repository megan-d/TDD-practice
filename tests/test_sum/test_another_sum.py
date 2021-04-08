from sum.another_sum import another_sum
import pytest


@pytest.mark.smoke
def test_another_sum() -> int:
    assert another_sum(3, 2) == 5

