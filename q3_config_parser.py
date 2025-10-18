import configparser # Default Python library for reading INI-style configuration files.
import json         # Default Python library for working with JSON data (converting between dictionary and JSON text).
import os           # Default Python library for interacting with the operating system (checking if files exist).
import sys

CONFIG_FILE = 'config.ini'

# This GLOBAL VARIABLE (a dictionary) SIMULATES an in-memory database store. 
# It holds the data after parsing, mimicking saving data to a server.
DATABASE_STORE = {} 

# ------------------------- FUNCTION 1: READING CONFIG ----------------------------------

def read_and_parse_config(file_path: str) -> dict:
    """Reads and parses the configuration file, handling errors gracefully."""
    
    # configparser.ConfigParser() creates an OBJECT (a tool) specialized for reading INI files.
    config = configparser.ConfigParser()
    # Initializes an empty DICTIONARY {} to store our structured results.
    parsed_data = {} 
    
    print(f"Attempting to read configuration from: {file_path}")

    # Use try...except for robust error handling during file access.
    try:
        # os.path.exists() is a DEFAULT PYTHON FUNCTION that checks if the file is present.
        if not os.path.exists(file_path):
            # If not found, we 'raise' an exception (an intentional error)
            raise FileNotFoundError(f"Configuration file not found at: {file_path}")
            
        # The 'read' method loads the configuration data from the file.
        config.read(file_path)
        
        # We loop through each SECTION header (like '[Database]' or '[Server]').
        for section in config.sections():
            # config.items(section) pulls all key-value pairs for that section.
            # We convert that raw data into a clean Python dictionary structure.
            parsed_data[section] = dict(config.items(section))
            
        print("✅ Configuration file successfully parsed.")
        return parsed_data
        
    except FileNotFoundError as e:
        # Handles the error if 'config.ini' is missing.
        print(f"❌ Error: {e}")
        sys.exit(1)
    except configparser.Error as e:
        # Handles errors if the file is found but contains bad formatting.
        print(f"❌ Error parsing configuration file: {e}")
        sys.exit(1)

# ------------------------- FUNCTION 2: SAVING TO DB ----------------------------------

def save_to_database(data: dict):
    """Simulates saving the parsed data as JSON to a database."""
    global DATABASE_STORE # We use 'global' because we are modifying the variable defined outside this function.
    
    # Requirement: Save the output file data as JSON data.
    # json.dumps() is the DEFAULT PYTHON FUNCTION that converts a Python dictionary (data) into a JSON string format.
    json_data = json.dumps(data, indent=4) 
    
    # Store the JSON string in our simulated database variable.
    DATABASE_STORE['app_config'] = json_data
    
    print("\n--- Database Save Simulation ---")
    print("✅ Data successfully converted to JSON and 'saved' to the database.")

# ------------------------- FUNCTION 3: FETCHING (GET REQUEST SIMULATION) ----------------------------------

def fetch_from_database():
    """Simulates a GET request (fetching information) from the database."""
    global DATABASE_STORE 
    
    print("\n--- Simulated GET Request (Fetching Data) ---")
    
    # .get() safely retrieves the JSON string from the store.
    json_string = DATABASE_STORE.get('app_config')
    
    if json_string:
        # json.loads() is the DEFAULT PYTHON FUNCTION that converts the JSON string back into a Python dictionary 
        # (ready to be used by the application).
        fetched_data = json.loads(json_string)
        print("✅ Data fetched successfully via simulated GET Request.")
        return fetched_data
    else:
        print("⚠️ No configuration data found in the database store.")
        return {}

# ------------------------- FUNCTION 4: DISPLAYING OUTPUT ----------------------------------

def display_output(data: dict):
    """Prints the final configuration data in the desired format."""
    
    print("\nConfiguration File Parser Results:")
    # Outer loop: 'section' is the key (e.g., 'Database'), 'items' is the inner dictionary value.
    for section, items in data.items():
        # .capitalize() is a built-in string method to make the section title look clean.
        print(f"\n{section.capitalize()}:") 
        # Inner loop: 'key' (e.g., 'host'), 'value' (e.g., 'localhost').
        for key, value in items.items():
            print(f"- {key}: {value}")

# ------------------------- SCRIPT EXECUTION ----------------------------------
if __name__ == "__main__":
    config_data = read_and_parse_config(CONFIG_FILE)
    
    if config_data:
        save_to_database(config_data)
        
        fetched_data = fetch_from_database()
        
        display_output(fetched_data)
