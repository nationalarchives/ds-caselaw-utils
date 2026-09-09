from ds_caselaw_utils.tests.factory import make_court_repo_valid


def test_factory():
    input_data = [
        {
            "name": "court_group",
            "display_name": "court group 1",
            "courts": [
                {
                    "name": "court1",
                    "show_in_search_filters": True,
                },
                {"name": "court2", "show_in_search_filters": False},
            ],
        },
        {
            "name": "court_group2",
            "display_name": "court group 2",
            "courts": [{"name": "court3", "show_in_search_filters": False}],
        },
    ]

    output_data = [
        {
            "name": "court_group",
            "display_name": "court group 1",
            "courts": [
                {
                    "name": "court1",
                    "show_in_search_filters": True,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "show_to_editors": True,
                },
                {
                    "name": "court2",
                    "show_in_search_filters": False,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "show_to_editors": True,
                },
            ],
            "court": [
                {
                    "name": "court1",
                    "show_in_search_filters": True,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "show_to_editors": True,
                },
                {
                    "name": "court2",
                    "show_in_search_filters": False,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "show_to_editors": True,
                },
            ],
        },
        {
            "name": "court_group2",
            "display_name": "court group 2",
            "courts": [
                {
                    "name": "court3",
                    "show_in_search_filters": False,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "show_to_editors": True,
                }
            ],
            "court": [
                {
                    "name": "court3",
                    "show_in_search_filters": False,
                    "code": "placeholder code",
                    "link": "placeholder link",
                    "show_to_editors": True,
                }
            ],
        },
    ]
    assert str(output_data) == str(make_court_repo_valid(input_data))
