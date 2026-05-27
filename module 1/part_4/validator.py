class DataValidator:
  def __init__ (self):
    self.errors = []
    
  def validate_email(self, email):
    if '@' not in email: 
      self.errors.append("Invalid email")
      return False
    return True
  
  def validate_age(self, age): 
    if age < 18:
      self.errors.append("underage")
      return False
    return True
  
  def get_errors(self): 
    return self.errors


# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=10)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(19)

print(validator.get_errors())
#['Invalid email', 'underage', 'Invalid email']