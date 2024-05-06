from importlib import import_module

def fetch_criterion(criterion, path='criteria'):
  criterion_module = import_module(f'{path}.evaluate_{criterion}')
  
  return getattr(criterion_module, f'evaluate_{criterion}')
