def validate_position(fibonacci_function):
  def validate_and_execute(position, *args, **kwargs):
    if position < 0:
      raise ValueError("Position must be a positive integer")
  
    return fibonacci_function(position, *args, **kwargs)
  
  return validate_and_execute
