from var06 import get_var06


def test_get_var06_empty():
    lines = []
    actual = get_var06(lines, 'S')
    expected = (0, 0)
    assert actual == expected


def test_get_var06_fare_single_line():
    testline = '1,1,3,"Brand, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S'
    actual = get_var06([testline], 'S')
    expected = (7.25, 0)
    assert actual == expected


def test_get_var06_fare_multiple_lines():
    lines = ["1,0,3,'Brand, Mr. Owen Harris',male,22,1,0,A/5 21171,5,,S",
             "2,1,1,'Comings, Mrs. John Bradley (Florence Briggs Thayer)',"
             "female,38,1,0,PC 17599,100,C85,C",
             "32,0,1,'Spencer, Mrs. William Augustus (Marie Eugenie)',"
             "female,,1,0,PC 17569,50,B78,C",
             "3,1,3,'Heineken, Miss. Laina',"
             "female,26,0,0,STON/O2. 3101282,10,,S",
             "4,1,1,'Refuelled, Mrs. Jacques Heath (Lily May Peel)',"
             "female,35,1,0,113803,15,C123,S"]
    actual = get_var06(lines, "S")
    expected = (12.5, 5.0)

    assert actual == expected
