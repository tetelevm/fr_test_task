import os

workers = 4
max_requests = 1000
timeout = 30
preload_app = True
worker_class = "uvicorn.workers.UvicornWorker"

reload = os.getenv("DEBUG", "0") in ["1", "True", "true"]
bind = "0.0.0.0:8000"
