import pgeocode  # Library to look up location data from zipcodes

# Load ZIP database for US
nomi = pgeocode.Nominatim("us")

def zipcode_to_city(zipcode):
    result = nomi.query_postal_code(zipcode) # Query pgeocode using the zipcode
        # If zipcode is invalid, return empty values
    if not isinstance(result.place_name, str):
        return None, None
    
        # Get city and state from result
    city = result.place_name 
    state = result.state_name  

    return city, state