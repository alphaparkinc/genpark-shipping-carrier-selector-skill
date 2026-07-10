"""
example_usage.py -- Demonstrates ShippingCarrierSelectorClient
"""
from client import ShippingCarrierSelectorClient

def main():
    client = ShippingCarrierSelectorClient()
    result = client.select_carrier(
        country_code="US",
        package_weight_lbs=12.5,
        delivery_urgency="standard"
    )
    print("[Carrier Selector Result]")
    print(f"Courier: {result['selected_carrier']}")
    print(f"Method: {result['shipping_method_label']}")

if __name__ == "__main__":
    main()
