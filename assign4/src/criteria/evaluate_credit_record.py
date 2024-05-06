from status import Status

def evaluate_credit_record(application):
  return (Status.PASS, "Applicant has a good credit record.") if application.has_good_credit_record else \
    (Status.FAIL, "Applicant has a poor credit record.")
