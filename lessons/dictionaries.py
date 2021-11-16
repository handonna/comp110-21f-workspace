"""Demonstrations of dictionary capabilities"""


# Declaring type of dictionary
schools: dict[str, int]

# Initialize to empty dictionary
schools = dict()

# Set a key value pairing in dictionary
schools['UNC'] = 19400
schools['Duke'] = 6717
schools['NCSU'] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key == 'lookup'
print(f"UNC has {schools['UNC']} students")

# Remove a key value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools
# print(f"Duke is present: {is_duke_present}")

# print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {} # Same as dict()
# print(schools)

# Also could initialize key value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
# print(schools)

# Key doesn't exist
# print(schools['UNCC'])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
