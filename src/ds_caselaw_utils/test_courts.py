import unittest
import pathlib
from ruamel.yaml import YAML
from datetime import date

from .courts import courts, Court, CourtsRepository


class TestCourtsRepository(unittest.TestCase):
    def test_loads_selectable_courts(self):
        data = [{
            "name": "court_group",
            "courts": [{
                "name": "court1",
                "selectable": True,
            }, {
                "name": "court2",
                "selectable": False
            }]
        }]
        repo = CourtsRepository(data)
        selectable = repo.get_selectable()
        self.assertIn("court1", [c.name for c in selectable])
        self.assertNotIn("court2", [c.name for c in selectable])

    def test_loads_listable_courts(self):
        data = [
            {
                "name": "court_group1",
                "display_name": "court group 1",
                "courts": [{
                    "name": "court1",
                    "listable": True,
                }, {
                    "name": "court2",
                    "listable": False
                }]
            }, {
                "name": "court_group2",
                "display_name": "court group 2",
                "courts": [{
                    "name": "court3",
                    "listable": False
                }]
            }
        ]
        repo = CourtsRepository(data)
        groups = repo.get_listable_groups()
        self.assertIn("court group 1", [g.name for g in groups])
        self.assertNotIn("court group 2", [g.name for g in groups])
        self.assertIn("court1" , [c.name for g in groups for c in g.courts])
        self.assertNotIn("court2" , [c.name for g in groups for c in g.courts])
        self.assertNotIn("court3" , [c.name for g in groups for c in g.courts])



class TestCourt(unittest.TestCase):
    def test_list_name_explicit(self):
        court = Court({"list_name": "court_name"})
        self.assertEqual("court_name", court.list_name)

    def test_list_name_default(self):
        court = Court({"name": "court_name"})
        self.assertEqual("court_name", court.list_name)

    def test_param_aliases(self):
        court = Court({"param": "param_1", "extra_params": ["param_2"]})
        self.assertEqual(["param_1", "param_2"], court.param_aliases)

    def test_end_year_explicit(self):
        court = Court({"end_year": 1983})
        self.assertEqual(1983, court.end_year)

    def test_end_year_default(self):
        court = Court({})
        self.assertEqual(date.today().year, court.end_year)

class TestCourts(unittest.TestCase):
    def test_loads_court_yaml(self):
        yaml = YAML()
        datafile = pathlib.Path(__file__).parent / "data/court_names.yaml"
        with open(datafile) as f:
            court_data = yaml.load(f)
        courts_from_yaml = []
        for group in court_data:
            for court in group.get("courts"):
                courts_from_yaml.append(court)
        for (court, data) in zip(courts.get_all(), courts_from_yaml):
            self.assertEqual(court.name, data["name"])

