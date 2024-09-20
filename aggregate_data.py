data_list = [
    {'category': 'A', 'value': 100},
    {'category': 'B', 'value': 20},
    {'category': 'A', 'value': 30},
    {'category': 'B', 'value': 40}
]

def aggregate_data(data_list, specified_key, aggregator):
    """
    Aggregates data based on the specified key using the given aggregator
    """
    di = {}
    for data in data_list:
        key = data[specified_key]
        value = data['value']
        
        if key in di:
            di[key] = aggregator(di[key], value)
        else:
            di[key] = value  
    
    return di

def max_aggregator(existing_value, new_value):
    return max(existing_value, new_value)

result = aggregate_data(data_list, 'category', max_aggregator)
print(result) 
