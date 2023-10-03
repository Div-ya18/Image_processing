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


# Read data from CSV and create WarehouseParcelDetail objects
parcels = []
with open('WarehouseDetails.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        parcel = WarehouseParcelDetail(
            int(row['Parcel Number']),
            float(row['Parcel Weight']),
            row['Parcel Category']
        )
        parcels.append(parcel)

# Call the method to save and display parcel details
WarehouseParcelDetail.save_and_display_parcel_details(parcels)
