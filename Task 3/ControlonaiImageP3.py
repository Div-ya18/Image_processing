import csv
class WarehouseParcelDetail:
    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category

    @staticmethod
    def save_and_display_parcel_details(parcels):
        categories = {}
        for parcel in parcels:
            if parcel.parcel_category not in categories:
                categories[parcel.parcel_category] = []
            categories[parcel.parcel_category].append(parcel)

        for category, category_parcels in categories.items():
            # Display the parcel numbers
            print(category)
            for parcel in category_parcels:
                print(parcel.parcel_number)

            # Save to a single CSV file
            with open(f'{category}.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Parcel Number', 'Parcel Weight'])
                for parcel in category_parcels:
                    writer.writerow([parcel.parcel_number, parcel.parcel_weight])


# Example Usage
parcels = [
    WarehouseParcelDetail(23456, 10, 'Filters'),
    WarehouseParcelDetail(66234, 25, 'Automobil_parts'),
    WarehouseParcelDetail(98432, 50, 'Cargo_containeer'),
    WarehouseParcelDetail(96355, 8, 'Filters'),
    WarehouseParcelDetail(86643, 30, 'Automobil_parts'),
    WarehouseParcelDetail(53463, 45, 'Cargo_containeer'),
    WarehouseParcelDetail(83722, 15, 'Filters'),
    WarehouseParcelDetail(64326, 20, 'Automobil_parts'),
    WarehouseParcelDetail(87653, 60, 'Cargo_containeer')
]

WarehouseParcelDetail.save_and_display_parcel_details(parcels)
