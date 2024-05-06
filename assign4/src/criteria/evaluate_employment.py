from status import Status

def evaluate_employment(application):
  return (Status.PASS, "Applicant has had previous employment.") if application.has_employment else \
    (Status.FAIL, "Applicant has no previous employment.")
