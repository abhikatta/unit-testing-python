"""Module for performing unit testing of the Metric Convertions."""
from math import ceil
from pytest import raises, fixture
from utils.metric_conversion import DistanceConversion


class TestUtils:
    """Class for unit testing the Utils module."""
    @fixture
    def dis_converter(self):
        """Function for creating a converter object for every unit test.

        Returns:
            object: DistanceConversion class's object.
        """

        self.dis_converter = DistanceConversion()
        return self.dis_converter

    def test_to_kilometers(self, dis_converter) -> None:
        """Test for converting miles to kilometers."""
        assert ceil(dis_converter.to_kilometers(100)) == 161
        assert dis_converter.to_kilometers(1) == 1.60934
        assert dis_converter.to_kilometers(2) == 1.60934*2
        assert dis_converter.to_kilometers(10) == 16.0934
        with raises(ValueError):
            assert dis_converter.to_kilometers('asdsad')
        assert dis_converter.to_kilometers(1) == 1.60934
        assert dis_converter.to_kilometers(102.3) == 164.635482

    def test_to_miles(self, dis_converter) -> None:
        """Test for converting kilometers to miles."""
        assert dis_converter.to_miles(1) == 1/1.60934
