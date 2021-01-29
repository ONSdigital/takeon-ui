bind = "0.0.0.0:5000"
# set the workers to 2*CPU cores +1, setting it to 1 makes minikube response fast
workers = 1
worker_class = "gevent"
timeout = 240
