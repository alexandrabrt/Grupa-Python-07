import pytest
from functions import sum_from_args

sequences = (
    (1, 2, 3, 4, 5),
    (1, 2, 3)
)


@pytest.mark.parametrize('sequence,expected_result', [
    (sequences[0], 45),
    (sequences[1], 18),
])
def test_sum_from_args(sequence, expected_result):
    result = sum_from_args(*sequence)
    assert result == expected_result


@pytest.mark.parametrize('sequence,expected_result', [
    (sequences[0], 15),
    (sequences[1], 6),
])
def test_original_sum_from_args():
    result = sum_from_args.__wrapped__(1, 2, 3, 4, 5)
    assert result == 15
