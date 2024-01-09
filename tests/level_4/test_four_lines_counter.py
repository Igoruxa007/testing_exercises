from functions.level_4.four_lines_counter import count_lines_in

def test_count_lines_in_success(filepath):
    assert count_lines_in(filepath) == 5

def test_count_lines_in_file_missing():
    assert count_lines_in('1.txt') is None