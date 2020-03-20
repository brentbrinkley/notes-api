from helpers.scales import Scale


def test_scales():
    assert Scale.get_scale("circle", "major") == [
        "circle",
        "star",
        "triangle",
        "square",
        "leaf",
        "cube",
        "sun",
    ]

    assert Scale.get_scale("key", "melodic_minor") == [
        "key",
        "crown",
        "cube",
        "sun",
        "moon",
        "plus",
        "square",
    ]

