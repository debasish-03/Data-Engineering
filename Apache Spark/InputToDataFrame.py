from typing import List, Tuple


def convert_input_to_df(input_data: str) -> List[Tuple]:

    # Split input data into lines
    lines = input_data.strip().split('\n')

    # Extract column names
    columns = [col.strip() for col in lines[0].split('\t')]

    # Initialize the list to store the converted data
    data = []

    # Process each line of data
    for line in lines[1:]:
        values = [value.strip() for value in line.split('\t')]
        data.append(tuple(values))

    # Print the converted data
    # print("data =", data)
    return data