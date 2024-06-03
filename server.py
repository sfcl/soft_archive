import uvicorn

from cool_counters.wsgi import application


if __name__ == "__main__":
    uvicorn.run(application, host="127.0.0.1", port=5000, log_level="error", interface='wsgi')
    #uvicorn.run(application, host="127.0.0.1", uds='counter.socket', log_level="info", interface='wsgi')
