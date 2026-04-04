import pandas as pd

class DonorModel:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.data = pd.read_csv(file_path)
        except:
            self.data = pd.DataFrame(columns=[
                "Name", "Blood Group", "City", "Contact"
            ])

    def add_donor(self, name, blood_group, city, contact):
        new_data = pd.DataFrame([[name, blood_group, city, contact]],
                                columns=self.data.columns)
        self.data = pd.concat([self.data, new_data], ignore_index=True)
        self.data.to_csv(self.file_path, index=False)

    def search_donor(self, blood_group, city):
        result = self.data[
            (self.data["Blood Group"] == blood_group) &
            (self.data["City"].str.lower() == city.lower())
        ]
        return result