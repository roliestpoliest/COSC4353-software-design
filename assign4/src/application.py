from dataclasses import dataclass

@dataclass
class Application:
  has_employment: bool = False
  has_no_criminal_record: bool = False
  has_good_credit_record: bool = False
  has_security_clearance: bool = False
