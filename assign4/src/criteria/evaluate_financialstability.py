from status import Status

def evaluate_financialstability(application):
  return (Status.PASS, "Applicant is good financially.") if application.has_employment or application.has_good_credit_record else \
    (Status.FAIL, "Applicant not good financially.")
