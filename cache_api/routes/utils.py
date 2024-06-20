def get_chunk_id_least_accessed(data):
    # Initialize variables to hold the minimum last_accessed_time time and corresponding chunk_id
    min_access_time = float('inf')  # Initialize with positive infinity
    least_accessed_chunk_id = None
    
    # Iterate through the list of dictionaries
    for entry in data:
        # Extract last_accessed_time time and chunk_id from each dictionary
        last_accessed_time = entry.get('entry_info', {}).get('last_access_time')
        chunk_id = entry.get('chunk_id')
        
        # Check if the last_accessed_time time is smaller than the current minimum
        if last_accessed_time is not None and last_accessed_time < min_access_time:
            min_access_time = last_accessed_time
            least_accessed_chunk_id = chunk_id
    
    return least_accessed_chunk_id