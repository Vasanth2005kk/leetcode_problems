import pandas as pd
from tabulate import tabulate

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> str:
    result_df = pd.merge(person, address[['personId', 'city', 'state']], on='personId', how='left')

    # Select only the required columns: firstName, lastName, city, and state
    result_df = result_df[['firstName', 'lastName', 'city', 'state']]
    result_list = result_df.values.tolist()
    
    # Use tabulate to return a formatted table string
    return tabulate(result_list, headers=result_df.columns, tablefmt='grid')

person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}

# Sample data for Address table
address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}
person_df = pd.DataFrame(person_data)
address_df = pd.DataFrame(address_data)

print(combine_two_tables(person_df, address_df))
