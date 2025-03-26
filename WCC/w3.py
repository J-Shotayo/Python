def large_power(base, exponent):
    """
    Determines if base raised to exponent is greater than 5000
    
    Parameters:
    base (int or float): The base number
    exponent (int or float): The exponent
    
    Returns:
    bool: True if base^exponent > 5000, False otherwise
    """
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False