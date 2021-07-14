import pytest

@pytest.mark.number
def test_type():
    assert type(1 + 2) is int

@pytest.mark.number
def test_add_int():
    assert 5 + 2 == 7

@pytest.mark.string
def test_string():
    assert 'u' in 'sun'

# @pytest.mark.skip(reason='Temporarily disabled') - to skip test
@pytest.mark.string
def test_add_string():
    assert('sunny' + 'day') == 'sunnyday'

# flag -v to run pytest in verbose mode
# flag -k "<str>" to run pytest to look after given <str>
# flag -m to select "pytest.mark" which we want to run
# flag -rs to show details of skip (reason)
# flag -rsf "f" to show details of failed tests
# flag -q to run in quiet mode
# flag --trace to enable debugger