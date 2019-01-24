import logging
import logstash
logger = logging.getLogger("your_news_name")
logger.setLevel(logging.INFO)
host_demo = "ip_address"#xx.xx.xx.xx
logger.addHandler(logstash.TCPLogstashHandler(host_demo,5000))#logstash port 5000

def logerror(error_message):
    logger.error(error_message)

def loginfo(message):
    logger.info(message)


logerror("被ban了")