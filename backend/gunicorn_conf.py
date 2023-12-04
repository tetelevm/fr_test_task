workers = 4
max_requests = 1000
timeout = 30
preload_app = True
worker_class = "uvicorn.workers.UvicornWorker"

bind = "0.0.0.0:8000"
