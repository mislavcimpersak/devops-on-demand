from django.test import SimpleTestCase
from maintenance.logic import (
    single_center_de_needs,
    other_center_de_needs,
    optimal_devops_coverage,
)


class SingleCenterDeNeedsTestCase(SimpleTestCase):
    def test_single_center_de_needs__remainder_below_point_five(self):
        SERVERS = 30
        DE_CAPACITY = 7
        RESULT = 5

        assert single_center_de_needs(SERVERS, DE_CAPACITY) == RESULT

    def test_single_center_de_needs__remainder_above_point_five(self):
        SERVERS = 34
        DE_CAPACITY = 7
        RESULT = 5

        assert single_center_de_needs(SERVERS, DE_CAPACITY) == RESULT

    def test_single_center_de_needs__no_remainder_(self):
        SERVERS = 35
        DE_CAPACITY = 7
        RESULT = 5

        assert single_center_de_needs(SERVERS, DE_CAPACITY) == RESULT


class OtherCenterDeNeedsTestCase(SimpleTestCase):
    def test_other_center_de_needs__one_center(self):
        CURRENT_DATA_CENTER = "Foo"
        DE_CAPACITY = 7
        DATA_CENTERS = [{"name": CURRENT_DATA_CENTER, "servers": 20}]
        RESULT = 0

        assert other_center_de_needs(CURRENT_DATA_CENTER, DE_CAPACITY, DATA_CENTERS) == RESULT

    def test_other_center_de_needs__two_centers(self):
        CURRENT_DATA_CENTER = "Foo"
        DE_CAPACITY = 7
        DATA_CENTERS = [
            {"name": CURRENT_DATA_CENTER, "servers": 20},
            {"name": "Bar", "servers": 12},
        ]
        RESULT = 2

        assert other_center_de_needs(CURRENT_DATA_CENTER, DE_CAPACITY, DATA_CENTERS) == RESULT

    def test_other_center_de_needs__three_centers(self):
        CURRENT_DATA_CENTER = "Foo"
        DE_CAPACITY = 7
        DATA_CENTERS = [
            {"name": CURRENT_DATA_CENTER, "servers": 20},
            {"name": "Bar", "servers": 12},
            {"name": "Baz", "servers": 47},
        ]
        RESULT = 9

        assert other_center_de_needs(CURRENT_DATA_CENTER, DE_CAPACITY, DATA_CENTERS) == RESULT


class OptimalDevOpsCoverage(SimpleTestCase):
    def test_optimal_devops_coverage__one_data_center(self):
        DM_CAPACITY = 10
        DE_CAPACITY = 7
        DATA_CENTERS = [{"name": "Foo", "servers": 20}]
        RESULT = {"DE": 2, "DM_data_center": "Foo"}

        assert optimal_devops_coverage(DM_CAPACITY, DE_CAPACITY, DATA_CENTERS) == RESULT

    def test_optimal_devops_coverage__two_data_centers_high_dm_capacity(self):
        DM_CAPACITY = 10
        DE_CAPACITY = 7
        DATA_CENTERS = [{"name": "Foo", "servers": 20}, {"name": "Bar", "servers": 12}]
        RESULT = {"DE": 4, "DM_data_center": "Foo"}

        assert optimal_devops_coverage(DM_CAPACITY, DE_CAPACITY, DATA_CENTERS) == RESULT

    def test_optimal_devops_coverage__two_data_centers_low_dm_capacity(self):
        DM_CAPACITY = 7
        DE_CAPACITY = 10
        DATA_CENTERS = [{"name": "Foo", "servers": 20}, {"name": "Bar", "servers": 12}]
        RESULT = {"DE": 3, "DM_data_center": "Bar"}

        assert optimal_devops_coverage(DM_CAPACITY, DE_CAPACITY, DATA_CENTERS) == RESULT

    def test_optimal_devops_coverage__two_data_centers_one_empty(self):
        DM_CAPACITY = 7
        DE_CAPACITY = 10
        DATA_CENTERS = [{"name": "Foo", "servers": 0}, {"name": "Bar", "servers": 12}]
        RESULT = {"DE": 1, "DM_data_center": "Bar"}

        assert optimal_devops_coverage(DM_CAPACITY, DE_CAPACITY, DATA_CENTERS) == RESULT
