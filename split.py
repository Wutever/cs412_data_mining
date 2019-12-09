import pandas as pd

data = pd.read_csv('hotel_cleaned.csv')

netherlands = data.loc[data['Hotel_Country'] == 'Netherlands']
united_kingdom = data.loc[data['Hotel_Country'] == 'United Kingdom']
france = data.loc[data['Hotel_Country'] == 'France']
spain = data.loc[data['Hotel_Country'] == 'Spain']
italy = data.loc[data['Hotel_Country'] == 'Italy']
austria = data.loc[data['Hotel_Country'] == 'Austria']

netherlands.to_csv('netherlands.csv')
united_kingdom.to_csv('united_kingdom.csv')
france.to_csv('france.csv')
spain.to_csv('spain.csv')
italy.to_csv('italy.csv')
austria.to_csv('austria.csv')