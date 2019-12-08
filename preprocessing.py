import pandas as pd
data = pd.read_csv('Hotel_Reviews.csv')

def last_word(string):
    return string.split(' ')[-1]

data['Hotel_Country'] = data['Hotel_Address'].map(last_word)
data.loc[data['Hotel_Country'] == 'Kingdom', 'Hotel_Country'] = 'United Kingdom'

def trim(string):
    ret = []
    for word in string.split(','):
        ret.append(word[3:-2])
    return ret

data['Tags'] = data['Tags'].map(trim)

data['Has_Pet'] = ''

def has_pet_check(tags):
    if len(tags) != 0:
        return 'With a pet' in tags[0]

def has_pet_fill(tags):
    if len(tags) != 0:
        return tags[0]

def has_pet_trim(tags):
    if len(tags) != 0:
        return tags[1:]

data.loc[data['Tags'].map(has_pet_check), 'Has_Pet'] = data['Tags'].map(has_pet_fill)
data.loc[data['Tags'].map(has_pet_check), 'Tags'] = data['Tags'].map(has_pet_trim)

data['Trip_Type'] = ''

def trip_type_check(tags):
    if len(tags) != 0:
        return 'trip' in tags[0]
    return False

def trip_type_fill(tags):
    if len(tags) != 0:
        return tags[0]

def trip_type_trim(tags):
    if len(tags) != 0:
        return tags[1:]

data.loc[data['Tags'].map(trip_type_check), 'Trip_Type'] = data['Tags'].map(trip_type_fill)
data.loc[data['Tags'].map(trip_type_check), 'Tags'] = data['Tags'].map(trip_type_trim)

data['Traveler_Type'] = ''

def traveler_type_check(tags):
    if len(tags) != 0:
        return 'Couple' in tags[0] or 'Family with young children' in tags[0] or 'Family with older children' in tags[0] or 'Solo traveler' in tags[0] or 'Travelers with friends' in tags[0] or 'Group' in tags[0]
    return False
    
def traveler_type_fill(tags):
    if len(tags) != 0:
        return tags[0]

def traveler_type_trim(tags):
    if len(tags) != 0:
        return tags[1:]

data.loc[data['Tags'].map(traveler_type_check), 'Traveler_Type'] = data['Tags'].map(traveler_type_fill)
data.loc[data['Tags'].map(traveler_type_check), 'Tags'] = data['Tags'].map(traveler_type_trim)

data['Room_Type'] = ''

def room_type_check(tags):
    if len(tags) != 0:
        return 'Room' in tags[0] or 'Apartment' in tags[0] or 'Suite' in tags[0] or 'room' in tags[0] or 'rooms' in tags[0] or 'Twin' in tags[0] or 'Queen' in tags[0] or 'King' in tags[0] or 'View' in tags[0] or 'Studio' in tags[0] or 'Bedroom' in tags[0] or 'Guestroom' in tags[0] or 'Atrium' in tags[0] or 'Double' in tags[0] or 'Designer' in tags[0] or 'Square' in tags[0] or 'Exchange' in tags[0] or 'Deluxe' in tags[0] or 'Standard' in tags[0] or 'Family' in tags[0] or 'Duplex' in tags[0] or 'Cottage' in tags[0] or 'Loft' in tags[0] or 'Maisonette' in tags[0] or 'Offer' in tags[0] or 'Superior' in tags[0] or 'Club' in tags[0] or 'Luxury' in tags[0] or 'floor' in tags[0] or 'Presidential' in tags[0] or 'Nest' in tags[0] or 'house' in tags[0] or 'Premium' in tags[0] or 'Maison' in tags[0] or 'Canal' in tags[0]
    return False

def room_type_fill(tags):
    if len(tags) != 0:
        return tags[0]

def room_type_trim(tags):
    if len(tags) != 0:
        return tags[1:]

data.loc[data['Tags'].map(room_type_check), 'Room_Type'] = data['Tags'].map(room_type_fill)
data.loc[data['Tags'].map(room_type_check), 'Tags'] = data['Tags'].map(room_type_trim)

data['Stay_Period'] = ''

def stay_period_check(tags):
    if len(tags) != 0:
        return 'Stayed' in tags[0]
    return False

def stay_period_fill(tags):
    if len(tags) != 0:
        return tags[0]

def stay_period_trim(tags):
    if len(tags) != 0:
        return tags[1:]

data.loc[data['Tags'].map(stay_period_check), 'Stay_Period'] = data['Tags'].map(stay_period_fill)
data.loc[data['Tags'].map(stay_period_check), 'Tags'] = data['Tags'].map(stay_period_trim)

data['Mobile_Submission'] = ''

def mobile_submission_check(tags):
    if len(tags) != 0:
        return 'Submitted from a mobile device' in tags[0]
    return False

def mobile_submission_fill(tags):
    if len(tags) != 0:
        return tags[0]

def mobile_submission_trim(tags):
    if len(tags) != 0:
        return tags[1:]

data.loc[data['Tags'].map(mobile_submission_check), 'Mobile_Submission'] = data['Tags'].map(mobile_submission_fill)
data.loc[data['Tags'].map(mobile_submission_check), 'Tags'] = data['Tags'].map(mobile_submission_trim)

data = data.drop(['Tags'], axis=1)
data.to_csv('hotel_cleaned.csv')