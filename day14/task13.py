import time

def timer(func):
    def wraping(*agrs):
        star_time= time.time()
        res=func(*agrs)
        end_time=time.time()
        excution_time=end_time - star_time
        print(f"function'{func.__name__}' excuted in {excution_time:.2f} seconds")
        return res
    return wraping
@timer
def slow_function():
    time.sleep(1)
    print("Done!")

slow_function()