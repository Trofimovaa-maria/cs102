import unittest
from src.lab33.task2 import Respondent, AgeGroup, Survey
from io import StringIO
from unittest.mock import patch

class TestAgeGroup(unittest.TestCase):

    def test_add_person(self):
        group = AgeGroup(18, 25)
        person = Respondent("Иванов Иван", 20)

        group.add_person(person)

        self.assertEqual(len(group.people), 1)
        self.assertEqual(group.people[0].fio, "Иванов Иван")

    def test_sort_people(self):
        group = AgeGroup(18, 35)

        group.add_person(Respondent("Петров Петр", 20))
        group.add_person(Respondent("Иванов Иван", 25))
        group.add_person(Respondent("Сидорова Анна", 25))

        group.sort_people()

        self.assertEqual(
            [person.fio for person in group.people],
            ["Иванов Иван", "Сидорова Анна", "Петров Петр"]
        )

    def test_create_groups(self):
        survey = Survey()

        survey.create_groups([18, 25, 35])

        self.assertEqual(len(survey.groups), 4)

        self.assertEqual(
            [(group.lower_limit, group.high_limit) for group in survey.groups],
            [(0, 18), (19, 25), (26, 35), (36, 123)]
        )

    def test_distribute_person(self):
        survey = Survey()
        survey.create_groups([18, 25, 35])

        person = Respondent("Иванов Иван", 20)
        survey.distribute_person(person)

        self.assertEqual(len(survey.groups[1].people), 1)
        self.assertEqual(survey.groups[1].people[0].fio, "Иванов Иван")

    def test_sort_groups(self):
        survey = Survey()
        survey.create_groups([18, 25, 35])

        survey.sort_groups()

        self.assertEqual(
            [(group.lower_limit, group.high_limit) for group in survey.groups],
            [(36, 123), (26, 35), (19, 25), (0, 18)]
        )

    def test_print_groups(self):
        survey = Survey()
        survey.create_groups([18, 25, 35])

        person = Respondent("Иванов Иван", 20)
        survey.distribute_person(person)

        with patch("sys.stdout", new=StringIO()) as output:
            survey.print_groups()

        self.assertEqual(output.getvalue(), "19-25: Иванов Иван (20)\n")