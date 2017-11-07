import time

def function_execute_time(f):
    def my_warp(*args, **kwargs):
        start_time = time.time()
        result = f()
        end_time = time.time()
        time_interval = end_time - start_time
        print "function execute time", time_interval
    return my_warp

@function_execute_time
def hello_world():
    print "hello_world"
    pass


if __name__=='__main__':
    hello_world()

    
