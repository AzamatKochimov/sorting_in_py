def merge_sort_packages(packages):
    if len(packages) > 1:
        mid = len(packages) // 2
        left_half = packages[:mid]
        right_half = packages[mid:]

        merge_sort_packages(left_half)
        merge_sort_packages(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i]["postal_code"] < right_half[j]["postal_code"]:
                packages[k] = left_half[i]
                i += 1
            else:
                packages[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements are left
        while i < len(left_half):
            packages[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            packages[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
packages = [
    {"package_id": 1, "postal_code": "10001", "sender": "Sender A", "recipient": "Recipient X", "contents": "Item 1", "weight_kg": 2.5},
    {"package_id": 2, "postal_code": "90210", "sender": "Sender B", "recipient": "Recipient Y", "contents": "Item 2", "weight_kg": 1.8},
    {"package_id": 3, "postal_code": "30305", "sender": "Sender C", "recipient": "Recipient Z", "contents": "Item 3", "weight_kg": 3.2},
    {"package_id": 4, "postal_code": "60601", "sender": "Sender D", "recipient": "Recipient W", "contents": "Item 4", "weight_kg": 2.0},
]

merge_sort_packages(packages)

# Now the 'packages' is sorted by destination postal code
for package in packages:
    print(f"Package ID: {package['package_id']}, Postal Code: {package['postal_code']}, Sender: {package['sender']}, Recipient: {package['recipient']}")
