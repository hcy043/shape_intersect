#  ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ _________ ____ ____ ____ ____
# ||I |||n |||s |||e |||r |||t |||       |||C |||o |||d |||e |||       |||H |||e |||r |||e ||
# ||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||_______|||__|||__|||__|||__||
# |/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|

# DON'T FORGET TO CHANGE the2.minority_shape_intersect TO minority_shape_intersect IF YOU DONT USE IMPORT !!!

# def minority_shape_intersect(first_minority_shape, second_minority_shape):
#     return ()


# Or import the2.py
import the2


#   *   )             )
# ` )  /(   (      ( /( (          (  (
#  ( )(_)) ))\ (   )\()))\   (     )\))(
# (_(_()) /((_))\ (_))/((_)  )\ ) ((_))\
# |_   _|(_)) ((_)| |_  (_) _(_/(  (()(_)
#   | |  / -_)(_-<|  _| | || ' \))/ _` |
#   |_|  \___|/__/ \__| |_||_||_| \__, |
#                                 |___/

# Set SENSITIVITY
SENSITIVITY = 0.001

# Create Empty Test List
tests = []

# Import sys to read CLI Arguments
import sys

### Options ###

# This means run all tests. You can specify which tests to run by setting this to ["X", "Uber Basic"] etc.
wanted_tests = []

# This means run all tests. You can specify which tests to not run by setting this to ["X", "Uber Basic"] etc.
# Eg. If "X" is specified, every test other than X will run
# !!! This is overwirtes wanted_tests and has more POWER !!!
unwanted_tests = []

# Whether to show calculated input or not
show_calculated_input = True

# Whether to show shapes used in the test or not
show_minority_shapes = True

# Whether to show only fails or whole test result
show_only_fails = False

### Options ###

### Check CLI arguments to change options ###

if "-fo" in sys.argv or "--fails-only" in sys.argv:
    show_only_fails = True

if "-nms" in sys.argv or "--no-minority-shapes" in sys.argv:
    show_minority_shapes = False

if "-nci" in sys.argv or "--no-calculated-input" in sys.argv:
    show_calculated_input = False

### Check CLI arguments to change options ###

wanted_tests_length = len(wanted_tests)
unwanted_tests_length = len(unwanted_tests)


### Example Tests ###

# Test X (On the instruction PDF)
if ((wanted_tests_length == 0 or "X" in wanted_tests) and ("X" not in unwanted_tests)):

    test_x_shapes = (
        [(4., 8.), (20.6, 10.), (9.4, 18.1)],
        [(12.5, 7.), (18.7, 16.2), (2., 12.), (12.5, 11.3)]
    )

    test_x_calculations = the2.minority_shape_intersect(
        [(4., 8.), (20.6, 10.), (9.4, 18.1)],
        [(12.5, 7.), (18.7, 16.2), (2., 12.), (12.5, 11.3)]
    )

    test_x_results = [
        (12.5, 11.3),
        (12.5, 9.024096385542167),
        (13.984606613454961, 9.202964652223491),
        (16.513454260733393, 12.955448257862459),
        (13.748900224891674, 14.954813230212277),
        (6.781560380848003, 13.202548119734228),
        (5.996175908221797, 11.733588272785214)
    ]

    test_x = (
        "X",
        test_x_results,
        test_x_calculations,
        test_x_shapes
    )

    tests.append(test_x)

# Test Uber Basic
if ((wanted_tests_length == 0 or "Uber Basic" in wanted_tests) and ("Uber Basic" not in unwanted_tests)):

    test_uber_basic_shapes = (
        [(0, -6), (0, 6), (-6, 6), (-6, -6)],
        [(0, 0), (-2, 2), (-2, -2)]
    )

    test_uber_basic_calculations = the2.minority_shape_intersect(
        [(0, -6), (0, 6), (-6, 6), (-6, -6)],
        [(0, 0), (-2, 2), (-2, -2)]
    )

    test_uber_basic_results = [
        (-2, -2),
        (-2, 2),
        (0, 0)
    ]

    test_uber_basic = (
        "Uber Basic",
        test_uber_basic_results,
        test_uber_basic_calculations,
        test_uber_basic_shapes
    )

    tests.append(test_uber_basic)

### End Of Example Tests ###


### Tests in honour of Arda Kara ###

# Test One Point In
if ((wanted_tests_length == 0 or "One Point In" in wanted_tests) and ("One Point In" not in unwanted_tests)):

    test_triangle_ONEPOINTIN_shapes = (
        [(1.1, 6.9), (2.8, 4.3), (5.3, 8.2)],
        [(3., 7.), (5.9, 4.), (8., 7.1)]
    )

    test_triangle_ONEPOINTIN_calculations = the2.minority_shape_intersect(
        [(1.1, 6.9), (2.8, 4.3), (5.3, 8.2)],
        [(3., 7.), (5.9, 4.), (8., 7.1)]
    )

    test_triangle_ONEPOINTIN_results = [
        (3.920414673046252, 6.047846889952153),
        (4.550649350649351, 7.031012987012987),
        (3.0, 7.0)
    ]

    test_triangle_ONEPOINTIN = (
        "One Point In",
        test_triangle_ONEPOINTIN_results,
        test_triangle_ONEPOINTIN_calculations,
        test_triangle_ONEPOINTIN_shapes
    )

    tests.append(test_triangle_ONEPOINTIN)

# Test Two Point In
if ((wanted_tests_length == 0 or "Two Point In" in wanted_tests) and ("Two Point In" not in unwanted_tests)):

    test_triangle_TWOPOINTIN_shapes = (
        [(0.1, 0.1), (0.5, 0.1), (0.1, 1.0)],
        [(0.2, 0.5), (0.3, 0.3), (0.3, 1.0)]
    )

    test_triangle_TWOPOINTIN_calculations = the2.minority_shape_intersect(
        [(0.1, 0.1), (0.5, 0.1), (0.1, 1.0)],
        [(0.2, 0.5), (0.3, 0.3), (0.3, 1.0)]
    )

    test_triangle_TWOPOINTIN_results = [
        (0.3, 0.5500000000000002),
        (0.23793103448275862, 0.6896551724137931),
        (0.2, 0.5),
        (0.3, 0.3)
    ]

    test_triangle_TWOPOINTIN = (
        "Two Point In",
        test_triangle_TWOPOINTIN_results,
        test_triangle_TWOPOINTIN_calculations,
        test_triangle_TWOPOINTIN_shapes
    )

    tests.append(test_triangle_TWOPOINTIN)

# Test Whole Inside
if ((wanted_tests_length == 0 or "Whole Inside" in wanted_tests) and ("Whole Inside" not in unwanted_tests)):

    test_triangle_WHOLEINSIDE_shapes = (
        [(6., 6.), (9., 1.), (12., 6.)],
        [(8., 5.), (8., 4.), (9., 3.)]
    )

    test_triangle_WHOLEINSIDE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(8., 5.), (8., 4.), (9., 3.)]
    )

    test_triangle_WHOLEINSIDE_results = [
        (8., 5.),
        (8., 4.),
        (9., 3.)
    ]

    test_triangle_WHOLEINSIDE = (
        "Whole Inside",
        test_triangle_WHOLEINSIDE_results,
        test_triangle_WHOLEINSIDE_calculations,
        test_triangle_WHOLEINSIDE_shapes
    )

    tests.append(test_triangle_WHOLEINSIDE)

# Test Adjacent Edge
if ((wanted_tests_length == 0 or "Adjacent Edge" in wanted_tests) and ("Adjacent Edge" not in unwanted_tests)):

    test_triangle_ADJACENTEDGE_shapes = (
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (12., 6.), (6., 10.)]
    )

    test_triangle_ADJACENTEDGE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (12., 6.), (6., 10.)]
    )

    test_triangle_ADJACENTEDGE_results = [
        (6., 6.),
        (12., 6.)
    ]

    test_triangle_ADJACENTEDGE = (
        "Adjacent Edge",
        test_triangle_ADJACENTEDGE_results,
        test_triangle_ADJACENTEDGE_calculations,
        test_triangle_ADJACENTEDGE_shapes
    )

    tests.append(test_triangle_ADJACENTEDGE)

# Test Point on Edge
if ((wanted_tests_length == 0 or "Point on Edge" in wanted_tests) and ("Point on Edge" not in unwanted_tests)):

    test_triangle_POINTONEDGE_SHAPES = (
        [(6., 6.), (9., 1.), (12., 6.)],
        [(7., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_POINTONEDGE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(7., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_POINTONEDGE_results = [
        (7., 6.)
    ]

    test_triangle_POINTONEDGE = (
        "Point on Edge",
        test_triangle_POINTONEDGE_results,
        test_triangle_POINTONEDGE_calculations,
        test_triangle_POINTONEDGE_SHAPES
    )

    tests.append(test_triangle_POINTONEDGE)

# Test Common Corner
if ((wanted_tests_length == 0 or "Common Corner" in wanted_tests) and ("Common Corner" not in unwanted_tests)):

    test_triangle_COMMONCORNER_shapes = (
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_COMMONCORNER_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_COMMONCORNER_results = [
        (6., 6.)
    ]

    test_triangle_COMMONCORNER = (
        "Common Corner",
        test_triangle_COMMONCORNER_results,
        test_triangle_COMMONCORNER_calculations,
        test_triangle_COMMONCORNER_shapes
    )

    tests.append(test_triangle_COMMONCORNER)

### End Of Arda Kara ###


### Tests in honour of Kursat Vurusan ###

# Test Case 0
if ((wanted_tests_length == 0 or "Case 0" in wanted_tests) and ("Case 0" not in unwanted_tests)):

    test_Case0_shapes = (
        [(1, 1), (5, 5), (1, 6)],
        [(6, 3), (7, 5), (6, 5)]
    )

    test_Case0_calculations = the2.minority_shape_intersect(
        [(1, 1), (5, 5), (1, 6)],
        [(6, 3), (7, 5), (6, 5)]
    )

    test_Case0_results = [
    ]

    test_Case0 = (
        "Case 0",
        test_Case0_results,
        test_Case0_calculations,
        test_Case0_shapes
    )

    tests.append(test_Case0)

# Test Case 1
if ((wanted_tests_length == 0 or "Case 1" in wanted_tests) and ("Case 1" not in unwanted_tests)):

    test_Case1_shapes = (
        [(1, 1), (5, 5), (1, 6)],
        [(2, 3), (3, 5), (2, 5)]
    )

    test_Case1_calculations = the2.minority_shape_intersect(
        [(1, 1), (5, 5), (1, 6)],
        [(2, 3), (3, 5), (2, 5)]
    )

    test_Case1_results = [
        (3, 5),
        (2, 5),
        (2, 3)
    ]

    test_Case1 = (
        "Case 1",
        test_Case1_results,
        test_Case1_calculations,
        test_Case1_shapes
    )

    tests.append(test_Case1)

# Test Case 2
if ((wanted_tests_length == 0 or "Case 2" in wanted_tests) and ("Case 2" not in unwanted_tests)):

    test_Case2_shapes = (
        [(1.0, 1.0), (5.0, 5.0), (1.0, 6.0)],
        [(6.0, 3.0), (7.0, 5.0), (2.0, 4.0)]
    )

    test_Case2_calculations = the2.minority_shape_intersect(
        [(1.0, 1.0), (5.0, 5.0), (1.0, 6.0)],
        [(6.0, 3.0), (7.0, 5.0), (2.0, 4.0)]
    )

    test_Case2_results = [
        (4.5, 4.5),
        (3.6, 3.6),
        (2.0, 4.0)
    ]

    test_Case2 = (
        "Case 2",
        test_Case2_results,
        test_Case2_calculations,
        test_Case2_shapes
    )

    tests.append(test_Case2)

# Test Case 3
if ((wanted_tests_length == 0 or "Case 3" in wanted_tests) and ("Case 3" not in unwanted_tests)):

    test_Case3_shapes = (
        [(1.0, 1.0), (5.0, 4.0), (1.0, 6.0)],
        [(6.0, 3.0), (7.0, 5.0), (2.0, 4.0)]
    )

    test_Case3_calculations = the2.minority_shape_intersect(
        [(1.0, 1.0), (5.0, 4.0), (1.0, 6.0)],
        [(6.0, 3.0), (7.0, 5.0), (2.0, 4.0)]
    )

    test_Case3_results = [
        (4.25, 3.4375),
        (4.142857142857143, 4.428571428571429),
        (2.0, 4.0),
        (5.0, 4.0)
    ]

    test_Case3 = (
        "Case 3",
        test_Case3_results,
        test_Case3_calculations,
        test_Case3_shapes
    )

    tests.append(test_Case3)

# Test Case 4
if ((wanted_tests_length == 0 or "Case 4" in wanted_tests) and ("Case 4" not in unwanted_tests)):

    test_Case4_shapes = (
        [(1.0, 1.0), (5.0, 4.0), (1.0, 6.0)],
        [(2.0, 2.0), (7.0, 5.0), (2.0, 4.0)]
    )

    test_Case4_calculations = the2.minority_shape_intersect(
        [(1.0, 1.0), (5.0, 4.0), (1.0, 6.0)],
        [(2.0, 2.0), (7.0, 5.0), (2.0, 4.0)]
    )

    test_Case4_results = [
        (3.6666666666666665, 3.0),
        (4.142857142857143, 4.428571428571429),
        (2.0, 2.0),
        (2.0, 4.0),
        (5.0, 4.0)
    ]

    test_Case4 = (
        "Case 4",
        test_Case4_results,
        test_Case4_calculations,
        test_Case4_shapes
    )

    tests.append(test_Case4)

# Test Case 20
if ((wanted_tests_length == 0 or "Case 20" in wanted_tests) and ("Case 20" not in unwanted_tests)):

    test_Case20_shapes = (
        [(-4, -4), (6, 2), (6, 8), (-4, 4)],
        [(2, 2), (4, 10), (-2, 10)]
    )

    test_Case20_calculations = the2.minority_shape_intersect(
        [(-4, -4), (6, 2), (6, 8), (-4, 4)],
        [(2, 2), (4, 10), (-2, 10)]
    )

    test_Case20_results = [
        (3.2222222222222223, 6.888888888888889),
        (0.16666666666666666, 5.666666666666667),
        (2, 2)
    ]

    test_Case20 = (
        "Case 20",
        test_Case20_results,
        test_Case20_calculations,
        test_Case20_shapes
    )

    tests.append(test_Case20)

# Test Case 21
if ((wanted_tests_length == 0 or "Case 21" in wanted_tests) and ("Case 21" not in unwanted_tests)):

    test_Case21_shapes = (
        [(-4, -4), (6, 2), (2, 8), (-4, 4)],
        [(2, 2), (4, 10), (-2, 10)]
    )

    test_Case21_calculations = the2.minority_shape_intersect(
        [(-4, -4), (6, 2), (2, 8), (-4, 4)],
        [(2, 2), (4, 10), (-2, 10)]
    )

    test_Case21_results = [
        (3.090909090909091, 6.363636363636363),
        (-0.25, 6.5),
        (2, 8),
        (2, 2)
    ]

    test_Case21 = (
        "Case 21",
        test_Case21_results,
        test_Case21_calculations,
        test_Case21_shapes
    )

    tests.append(test_Case21)

# Test Case 22
if ((wanted_tests_length == 0 or "Case 22" in wanted_tests) and ("Case 22" not in unwanted_tests)):

    test_Case22_shapes = (
        [(-4, -4), (6, 2), (2, 8), (-4, 4)],
        [(12, -10), (10, 10), (-8, -5)]
    )

    test_Case22_calculations = the2.minority_shape_intersect(
        [(-4, -4), (6, 2), (2, 8), (-4, 4)],
        [(12, -10), (10, 10), (-8, -5)]
    )

    test_Case22_results = [
        (4.0, 5.0),
        (-4.0, -1.6666666666666667),
        (-4, -4),
        (6, 2)
    ]

    test_Case22 = (
        "Case 22",
        test_Case22_results,
        test_Case22_calculations,
        test_Case22_shapes
    )

    tests.append(test_Case22)

# Test Case 23
if ((wanted_tests_length == 0 or "Case 23" in wanted_tests) and ("Case 23" not in unwanted_tests)):

    test_Case23_shapes = (
        [(-4, -4), (8, -15), (4, -5), (4, 10)],
        [(12, -10), (10, 10), (-8, -5)]
    )

    test_Case23_calculations = the2.minority_shape_intersect(
        [(-4, -4), (8, -15), (4, -5), (4, 10)],
        [(12, -10), (10, 10), (-8, -5)]
    )

    test_Case23_results = [
        (4.0, 5.0),
        (-1.4545454545454546, 0.45454545454545453),
        (-1.0, - 6.75),
        (5.333333333333333, -8.333333333333334),
        (-4, -4),
        (4, -5)
    ]

    test_Case23 = (
        "Case 23",
        test_Case23_results,
        test_Case23_calculations,
        test_Case23_shapes
    )

    tests.append(test_Case23)

# Test Case 24
if ((wanted_tests_length == 0 or "Case 24" in wanted_tests) and ("Case 24" not in unwanted_tests)):

    test_Case24_shapes = (
        [(-4, -4), (6, -7.1), (4, -5), (6, 0)],
        [(12, -10), (10, 10), (-8, -5)]
    )

    test_Case24_calculations = the2.minority_shape_intersect(
        [(-4, -4), (6, -7.1), (4, -5), (6, 0)],
        [(12, -10), (10, 10), (-8, -5)]
    )

    test_Case24_results = [
        (-4, -4),
        (6, -7.1),
        (4, -5),
        (6, 0)
    ]

    test_Case24 = (
        "Case 24",
        test_Case24_results,
        test_Case24_calculations,
        test_Case24_shapes
    )

    tests.append(test_Case24)

# Test Case 30
if ((wanted_tests_length == 0 or "Case 30" in wanted_tests) and ("Case 30" not in unwanted_tests)):

    test_Case30_shapes = (
        [(-6, 5), (4, 5), (4, 15), (-6, 15)],
        [(-4, 10), (10, 10), (10, 20), (-4, 20)]
    )

    test_Case30_calculations = the2.minority_shape_intersect(
        [(-6, 5), (4, 5), (4, 15), (-6, 15)],
        [(-4, 10), (10, 10), (10, 20), (-4, 20)]
    )

    test_Case30_results = [
        (4.0, 10.0),
        (-4.0, 15.0),
        (-4, 10),
        (4, 15)
    ]

    test_Case30 = (
        "Case 30",
        test_Case30_results,
        test_Case30_calculations,
        test_Case30_shapes
    )

    tests.append(test_Case30)

# Test Case 31
if ((wanted_tests_length == 0 or "Case 31" in wanted_tests) and ("Case 31" not in unwanted_tests)):

    test_Case31_shapes = (
        [(-6, 5), (4, 5), (4, 15), (-6, 15)],
        [(10, 15), (10, 25), (-4.1, 25), (-4.1, 15)]
    )

    test_Case31_calculations = the2.minority_shape_intersect(
        [(-6, 5), (4, 5), (4, 15), (-6, 15)],
        [(10, 15), (10, 25), (-4.1, 25), (-4.1, 15)]
    )

    test_Case31_results = [
    ]

    test_Case31 = (
        "Case 31",
        test_Case31_results,
        test_Case31_calculations,
        test_Case31_shapes
    )

    tests.append(test_Case31)

# Test Case 32
if ((wanted_tests_length == 0 or "Case 32" in wanted_tests) and ("Case 32" not in unwanted_tests)):

    test_Case32_shapes = (
        [(7.9, 22.3), (-2.1, 22.3), (-2.1, 17.3), (7.9, 17.3)],
        [(10, 15), (10, 25), (-4.1, 25), (-4.1, 15)]
    )

    test_Case32_calculations = the2.minority_shape_intersect(
        [(7.9, 22.3), (-2.1, 22.3), (-2.1, 17.3), (7.9, 17.3)],
        [(10, 15), (10, 25), (-4.1, 25), (-4.1, 15)]
    )

    test_Case32_results = [
        (7.9, 22.3),
        (-2.1, 22.3),
        (-2.1, 17.3),
        (7.9, 17.3)
    ]

    test_Case32 = (
        "Case 32",
        test_Case32_results,
        test_Case32_calculations,
        test_Case32_shapes
    )

    tests.append(test_Case32)

# Test Case 33
if ((wanted_tests_length == 0 or "Case 33" in wanted_tests) and ("Case 33" not in unwanted_tests)):

    test_Case33_shapes = (
        [(7.9, 22.3), (-2.1, 22.3), (-2.1, 17.3), (7.9, 17.3)],
        [(6.0, 5.0), (10, 25), (-4.1, 25), (5.4, 19.9)]
    )

    test_Case33_calculations = the2.minority_shape_intersect(
        [(7.9, 22.3), (-2.1, 22.3), (-2.1, 17.3), (7.9, 17.3)],
        [(6.0, 5.0), (10, 25), (-4.1, 25), (5.4, 19.9)]
    )

    test_Case33_results = [
        (0.9294117647058838, 22.3),
        (5.504697986577181, 17.299999999999997),
        (5.4, 19.9),
        (7.9, 22.3),
        (7.9, 17.3)
    ]

    test_Case33 = (
        "Case 33",
        test_Case33_results,
        test_Case33_calculations,
        test_Case33_shapes
    )

    tests.append(test_Case33)

# Test Case 34
if ((wanted_tests_length == 0 or "Case 34" in wanted_tests) and ("Case 34" not in unwanted_tests)):

    test_Case34_shapes = (
        [(-10, 20), (15, 35), (-10.3, 36.1), (-5.0, 30.0)],
        [(5, 15), (5, 25), (15, 25), (2, 32.5)]
    )

    test_Case34_calculations = the2.minority_shape_intersect(
        [(-10, 20), (15, 35), (-10.3, 36.1), (-5.0, 30.0)],
        [(5, 15), (5, 25), (15, 25), (2, 32.5)]
    )

    test_Case34_results = [
        (6.503267973856209, 29.901960784313726),
        (2.8238341968911915, 27.694300518134714),
        (2, 32.5)
    ]

    test_Case34 = (
        "Case 34",
        test_Case34_results,
        test_Case34_calculations,
        test_Case34_shapes
    )

    tests.append(test_Case34)

# Test Case 35
if ((wanted_tests_length == 0 or "Case 35" in wanted_tests) and ("Case 35" not in unwanted_tests)):

    test_Case35_shapes = (
        [(-10, 20), (15, 35), (-10.3, 36.1), (-5.0, 30.0)],
        [(5, 15), (5, 25), (15, 25), (-5.0, 45.0)]
    )

    test_Case35_calculations = the2.minority_shape_intersect(
        [(-10, 20), (15, 35), (-10.3, 36.1), (-5.0, 30.0)],
        [(5, 15), (5, 25), (15, 25), (-5.0, 45.0)]
    )

    test_Case35_results = [
        (8.75, 31.25),
        (1.1111111111111112, 26.666666666666668),
        (4.545454545454546, 35.45454545454545),
        (-1.911764705882353, 35.73529411764706)
    ]

    test_Case35 = (
        "Case 35",
        test_Case35_results,
        test_Case35_calculations,
        test_Case35_shapes
    )

    tests.append(test_Case35)

# Test Case 36
if ((wanted_tests_length == 0 or "Case 36" in wanted_tests) and ("Case 36" not in unwanted_tests)):

    test_Case36_shapes = (
        [(-10, 20), (15, 35), (-10.3, 36.1), (-5.0, 30.0)],
        [(5, 15), (5, 25), (15, 25), (-5.0, 30.0)]
    )

    test_Case36_calculations = the2.minority_shape_intersect(
        [(-10, 20), (15, 35), (-10.3, 36.1), (-5.0, 30.0)],
        [(5, 15), (5, 25), (15, 25), (-5.0, 30.0)]
    )

    test_Case36_results = [
        (3.235294117647059, 27.941176470588236),
        (-1.6666666666666667, 25.0),
        (-5.0, 30.0)
    ]

    test_Case36 = (
        "Case 36",
        test_Case36_results,
        test_Case36_calculations,
        test_Case36_shapes
    )

    tests.append(test_Case36)

# Test Case 37
if ((wanted_tests_length == 0 or "Case 37" in wanted_tests) and ("Case 37" not in unwanted_tests)):

    test_Case37_shapes = (
        [(-30, 10), (33.5, 37.4), (-20, 50), (-10, 30)],
        [(50, 60), (5.6, 33.3), (50, 20), (40, 40)]
    )

    test_Case37_calculations = the2.minority_shape_intersect(
        [(-30, 10), (33.5, 37.4), (-20, 50), (-10, 30)],
        [(50, 60), (5.6, 33.3), (50, 20), (40, 40)]
    )

    test_Case37_results = [
        (16.459432053602182, 30.047062019979524),
        (18.350965093642007, 40.967810090095526),
        (5.6, 33.3),
        (33.5, 37.4)
    ]

    test_Case37 = (
        "Case 37",
        test_Case37_results,
        test_Case37_calculations,
        test_Case37_shapes
    )

    tests.append(test_Case37)

# Test Case 38
if ((wanted_tests_length == 0 or "Case 38" in wanted_tests) and ("Case 38" not in unwanted_tests)):

    test_Case38_shapes = (
        [(-30, 10), (33.5, 37.4), (-20, 50), (-10, 30)],
        [(50, 60), (5.6, 33.3), (50, 20), (100, 40)]
    )

    test_Case38_calculations = the2.minority_shape_intersect(
        [(-30, 10), (33.5, 37.4), (-20, 50), (-10, 30)],
        [(50, 60), (5.6, 33.3), (50, 20), (100, 40)]
    )

    test_Case38_results = [
        (16.459432053602182, 30.047062019979524),
        (18.350965093642007, 40.967810090095526),
        (5.6, 33.3),
        (33.5, 37.4)
    ]

    test_Case38 = (
        "Case 38",
        test_Case38_results,
        test_Case38_calculations,
        test_Case38_shapes
    )

    tests.append(test_Case38)

# Test Case 39
if ((wanted_tests_length == 0 or "Case 39" in wanted_tests) and ("Case 39" not in unwanted_tests)):

    test_Case39_shapes = (
        [(-30, 10), (33.5, 37.4), (-20, 50), (-62, 30)],
        [(50, 60), (5.6, 33.3), (50, 20), (100, 40)]
    )

    test_Case39_calculations = the2.minority_shape_intersect(
        [(-30, 10), (33.5, 37.4), (-20, 50), (-62, 30)],
        [(50, 60), (5.6, 33.3), (50, 20), (100, 40)]
    )

    test_Case39_results = [
        (16.459432053602182, 30.047062019979524),
        (18.350965093642007, 40.967810090095526),
        (5.6, 33.3),
        (33.5, 37.4)
    ]

    test_Case39 = (
        "Case 39",
        test_Case39_results,
        test_Case39_calculations,
        test_Case39_shapes
    )

    tests.append(test_Case39)

### End Of Kursat Vurusan ###


# Insert your own cool named test here

# Right below this comment


# Ok thats enough


import datetime

total_start_time = datetime.datetime.now()

failed_post_count = 0

for test in tests:

    start_time = datetime.datetime.now()

    willBePrintedResult = "\n"

    name, results, calculations, shapes = test

    results_length = len(results)
    calculations_length = len(calculations)

    is_failed = False

    willBePrintedResult += " Test " + name + "\n"
    willBePrintedResult += "-" * 30 + "\n"

    if show_minority_shapes:
        willBePrintedResult += "\t(@) First Shape: " + str(shapes[0]) + "\n"
        willBePrintedResult += "\t(@) Second Shape: " + str(shapes[1]) + "\n\n"

    if show_calculated_input:
        willBePrintedResult += "\t(@) Calculations: " + \
            str(calculations) + "\n\n"

    if results_length != calculations_length:
        willBePrintedResult += "\t(!) Failed: Correct results has " + str(
            results_length) + " items, but calculations has " + str(calculations_length)
        is_failed = True
    else:
        willBePrintedResult += "\t(~) Passed: Correct results has " + str(
            results_length) + " items, calculations also has " + str(calculations_length)

    willBePrintedResult += "\n\n"

    for result in results:

        is_calculated = False

        for calculation in calculations:
            if abs(result[0] - calculation[0]) <= SENSITIVITY and abs(result[1] - calculation[1]) <= SENSITIVITY:
                is_calculated = True
                break

        if is_calculated:
            willBePrintedResult += "\t(~) Passed: " + str(result)
        else:
            willBePrintedResult += "\t(!) Failed: " + str(result)
            is_failed = True
        willBePrintedResult += "\n"

    willBePrintedResult += "\n"

    finish_time = datetime.datetime.now()

    if is_failed:
        failed_post_count = failed_post_count + 1
        willBePrintedResult += "\t(!) Test " + name + " failed. (In " + str(
            (finish_time - start_time).total_seconds() * 1000) + " milliseconds)"

    else:
        willBePrintedResult += "\t(~) Test " + name + " passed. (In " + str(
            (finish_time - start_time).total_seconds() * 1000) + " milliseconds)"

    willBePrintedResult += "\n"

    if show_only_fails:
        if is_failed:
            print willBePrintedResult
    else:
        print willBePrintedResult

total_finish_time = datetime.datetime.now()

print "--- Tested", len(tests), "conditions,", failed_post_count, "failed", len(tests) - failed_post_count, "passed. (In " + str((total_finish_time - total_start_time).total_seconds() * 1000) + " milliseconds) ---"
