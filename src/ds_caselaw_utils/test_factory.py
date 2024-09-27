from .factory import make_court_repo_valid


def test_factory():
    input_data = [
        {
            "name": "court_group",
            "display_name": "court group 1",
            "courts": [
                {
                    "name": "court1",
                    "selectable": True,
                },
                {"name": "court2", "selectable": False},
            ],
        },
        {
            "name": "court_group2",
            "display_name": "court group 2",
            "courts": [{"name": "court3", "selectable": False}],
        },
    ]

    output_data = [
        {
            "name": "court_group",
            "display_name": "court group 1",
            "courts": [
                {
                    "name": "court1",
                    "selectable": True,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "listable": True,
                },
                {
                    "name": "court2",
                    "selectable": False,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "listable": True,
                },
            ],
            "court": [
                {
                    "name": "court1",
                    "selectable": True,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "listable": True,
                },
                {
                    "name": "court2",
                    "selectable": False,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "listable": True,
                },
            ],
        },
        {
            "name": "court_group2",
            "display_name": "court group 2",
            "courts": [
                {
                    "name": "court3",
                    "selectable": False,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "listable": True,
                }
            ],
            "court": [
                {
                    "name": "court3",
                    "selectable": False,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "listable": True,
                }
            ],
        },
    ]
    assert str(output_data) == str(make_court_repo_valid(input_data))
