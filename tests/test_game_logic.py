from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# Tests for get_range_for_difficulty — targeting the Hard range bug
def test_hard_range_is_larger_than_normal():
    # Bug: Hard used to return (1, 50), which is easier than Normal (1, 100)
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, "Hard difficulty should have a larger range than Normal"

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


# Tests for parse_guess
def test_parse_guess_none():
    ok, val, err = parse_guess(None)
    assert ok == False
    assert val is None
    assert err == "Enter a guess."

def test_parse_guess_empty():
    ok, val, err = parse_guess("")
    assert ok == False
    assert val is None
    assert err == "Enter a guess."

def test_parse_guess_non_numeric():
    ok, val, err = parse_guess("abc")
    assert ok == False
    assert val is None
    assert err == "That is not a number."

def test_parse_guess_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok == True
    assert val == 42
    assert err is None

def test_parse_guess_float_string():
    ok, val, err = parse_guess("3.7")
    assert ok == True
    assert val == 3
    assert err is None


# Tests for update_score
def test_update_score_win_early():
    # attempt 1: points = 100 - 10*(1+1) = 80
    result = update_score(0, "Win", 1)
    assert result == 80

def test_update_score_win_floor():
    # attempt 9: points = 100 - 10*(9+1) = 0 → floored to 10
    result = update_score(0, "Win", 9)
    assert result == 10

def test_update_score_too_high_even_attempt():
    # even attempt → +5
    result = update_score(100, "Too High", 2)
    assert result == 105

def test_update_score_too_high_odd_attempt():
    # odd attempt → -5
    result = update_score(100, "Too High", 3)
    assert result == 95

def test_update_score_too_low():
    result = update_score(100, "Too Low", 1)
    assert result == 95

def test_update_score_unknown_outcome():
    result = update_score(100, "Unknown", 1)
    assert result == 100
