def quick_sort_packages(packages):
    if len(packages) <= 1:
        return packages

    # Choose a pivot postal code
    pivot = packages[len(packages) // 2]["postal_code"]
    left = [package for package in packages if package["postal_code"] < pivot]
    middle = [package for package in packages if package["postal_code"] == pivot]
    right = [package for package in packages if package["postal_code"] > pivot]

    return quick_sort_packages(left) + middle + quick_sort_packages(right)


# Example usage:
packages = [
    {"package_id": 1, "postal_code": "10001", "sender": "Sender A",
        "recipient": "Recipient X", "contents": "Item 1", "weight_kg": 2.5},
    {"package_id": 2, "postal_code": "90210", "sender": "Sender B",
        "recipient": "Recipient Y", "contents": "Item 2", "weight_kg": 1.8},
    {"package_id": 3, "postal_code": "30305", "sender": "Sender C",
        "recipient": "Recipient Z", "contents": "Item 3", "weight_kg": 3.2},
    {"package_id": 4, "postal_code": "60601", "sender": "Sender D",
        "recipient": "Recipient W", "contents": "Item 4", "weight_kg": 2.0},
]

sorted_packages = quick_sort_packages(packages)

# Now the 'sorted_packages' is sorted by destination postal code
for package in sorted_packages:
    print(
        f"Package ID: {package['package_id']}, Postal Code: {package['postal_code']}, Sender: {package['sender']}, Recipient: {package['recipient']}")
