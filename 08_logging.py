# importing the logging module
# import logging as log

'''
5 levels of logging
1. debug
2. info 
3. warning
4. error
5. critical
'''

'''
log.basicConfig(filename = 'test.log', level = log.INFO)
log.info("store a message")
log.debug("this is a debug message")
log.warning("this is my warning")
log.error("this is an error message")
log.critical("this is a critical message")
'''

# setting up a new log

import logging
logging.basicConfig(filename = 'exceptionHandling.log', level = logging.DEBUG, format = '%(asctime)s - %(message)s - %(levelname)s ')

'''
best practice to not use print function in production env
'''

try:
  logging.info("This is a start of my programme")
  logging.info("asking user to enter ag ")
  age = int(input("Enter your age: "))
  logging.info("user has entered the age: %d", age)
  if age < 0:
    logging.info("I am checking the negative condition")
    raise ValueError("User has entered a negative age which is not valid!")
  elif age < 18:
    logging.info("I am trying to check underage condition")
    raise Exception("User is underage")
  else:
    logging.info("Valid User")
except Exception as e:
  logging.error(e)
