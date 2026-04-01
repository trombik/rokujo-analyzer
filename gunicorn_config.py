# import multiprocessing

bind = "127.0.0.1:8000"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 2
worker_class = "uvicorn.workers.UvicornWorker"

preload_app = True
max_requests = 1000
max_requests_jitter = 50
