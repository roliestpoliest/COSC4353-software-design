import os

def fetch_criteria(path='src/criteria'):
  return (
    file.replace('evaluate_', '').replace('.py', '')
    for file in os.listdir(path)
    if file.startswith('evaluate_') and file.endswith('.py')
  )
