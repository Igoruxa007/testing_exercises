from functions.level_4.two_students import get_student_by_tg_nickname

def test_get_student_by_tg_nickname_success_case(studentstudents_with_tg):
    assert get_student_by_tg_nickname("AI", studentstudents_with_tg) == studentstudents_with_tg[0]

def test_get_student_by_tg_nickname_tgacc_none_in_list(studentstudents_with_tg):
    assert get_student_by_tg_nickname("BC", studentstudents_with_tg) is None