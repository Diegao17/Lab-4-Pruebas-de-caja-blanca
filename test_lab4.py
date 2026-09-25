import process_grades
import pytest

@pytest.mark.parametrize(
        'students, expected',
        [
            ([{'name': 'Ana', 'grades': [80, 80, 80]}], ['Ana']),
        ]
)
@pytest.mark.system
def test_proccess_grade_pass(students, expected):
    result = process_grades.process_grades(students)
    assert result['passed'] == expected

@pytest.mark.parametrize(
        'students, expected',
        [
            ([{'name': 'Ana', 'grades': [55, 55, 55]}], 'is in recovery'),
        ]
)
@pytest.mark.system
def test_proccess_grade_recovery(students, expected, capsys):
    process_grades.process_grades(students)
    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize(
        'students, expected',
        [
            ([{'name': 'Ana', 'grades': [40, 40, 40]}], ['Ana']),
        ]
)
@pytest.mark.wip
def test_proccess_grade_fail(students, expected):
    result = process_grades.process_grades(students)
    assert result['failed'] == expected