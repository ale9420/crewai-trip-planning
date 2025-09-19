# Gunicorn configuration file
import multiprocessing

# Worker processes
workers = 2  # App Engine recommends 2-4 workers
worker_class = 'uvicorn.workers.UvicornWorker'

# Socket
bind = '0.0.0.0:8080'

# Logging
accesslog = '-'
errorlog = '-'

# Restart workers after this many requests
max_requests = 1000
max_requests_jitter = 50

# Timeout
timeout = 120

# Keep the worker alive for this many seconds
keepalive = 5

# Process naming
proc_name = 'trip_planning'

# SSL (if needed)
# keyfile = '/path/to/keyfile'
# certfile = '/path/to/certfile'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Logging
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'