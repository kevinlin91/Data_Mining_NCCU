import time

def decorator_example(f):
    def my_warp(*args, **kwargs):
        start_time = time.time()
        result = f()
        end_time = time.time()
        time_interval = end_time - start_time
        print "function execute time", time_interval
    return my_warp

@decorator_example
def hello_world():
    print "hello_world"
    return

hello_world()

    
