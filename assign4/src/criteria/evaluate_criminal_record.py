from status import Status

def evaluate_criminal_record(application):
  return (Status.PASS, "Applicant has no criminal record.") if application.has_no_criminal_record else \
    (Status.FAIL, "Applicant has a criminal record.")
