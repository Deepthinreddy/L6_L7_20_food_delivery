
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# Delivery charge test cases

def test_invalid_distance_zero():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)


def test_invalid_distance_above_limit():
    with pytest.raises(ValueError):
        delivery_charge(16, 200, False)


def test_free_delivery():
    assert delivery_charge(5, 500, False) == 0


def test_nearby_delivery_rain():
    assert delivery_charge(2, 200, True) == 50


def test_medium_distance_delivery():
    assert delivery_charge(5, 200, False) == 40


def test_long_distance_delivery_rain():
    assert delivery_charge(10, 200, True) == 90


# Coupon test cases

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300


def test_invalid_coupon():
    with pytest.raises(ValueError):
        apply_coupon(300, "INVALID", True)


def test_welcome_coupon_not_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)


def test_order_below_minimum():
    assert apply_coupon(150, "SAVE50", True) == 150


def test_save50_coupon():
    assert apply_coupon(300, "SAVE50", True) == 250


def test_welcome_coupon():
    assert apply_coupon(300, "WELCOME", True) == 200


# Estimated delivery time test cases

def test_normal_delivery():
    assert estimated_time(5, False, False) == 35


def test_peak_hour_delivery():
    assert estimated_time(5, True, False) == 45


def test_busy_restaurant_peak_hour():
    assert estimated_time(5, True, True) == 65
