# There are two ways we can import logging :
# Firstly from src.cnnClassifier.logging import logging ----> if i create a loggging folder like 
#entity and pipeline foler.

# Second method is to write the logging in __init__.py (constructor) file.

# Second method makes it easy to import the logging.Because awakes automatically.
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
# After you productionize the code, you won't be able to see the terminal,like what is happening in your code.
# You can check the logs in this below file and find the bugs. 
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
