def logban(fieldlog,error):
    import logging
    import logstash
    logger = logging.getLogger(fieldlog)
    logger.setLevel(logging.INFO)
    host_demo = "10.120.14.204"
    logger.addHandler(logstash.TCPLogstashHandler(host_demo,5000))
    logger.error(error)

logban("udn","被ban了")