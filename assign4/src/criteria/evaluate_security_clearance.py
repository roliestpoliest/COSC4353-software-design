from status import Status

def evaluate_security_clearance(application):
  return (Status.PASS, "Applicant has security clearance.") if application.has_security_clearance else \
    (Status.FAIL, "Applicant has no security clearance.")
