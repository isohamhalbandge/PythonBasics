import logging
def log_fun(func):
  def log_inner(*args):
    logging.basicConfig(filename = 'test.log', level = logging.INFO)
    logging.info("this is start of my function")
    func(*args)
    logging.info("this is end of my function")

  return log_inner

@log_fun
def print_list(l: list):
  for i in l:
    print(i)
    
print_list([1,2,3,4,5])
