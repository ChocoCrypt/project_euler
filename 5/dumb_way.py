import time


def is_divided_by(k, n):
    for i in range(1,n):
        if(k%i != 0):
            return(False)
    return True

no_result = True
i = 1

start = time.time()
while(no_result):
    i+=1
    if(is_divided_by(i , 21)):
        print(f"result : {i}")
        no_result = False

end = time.time()
total_time = end-start
total_time_minutes = total_time/60

print(f"total time took {total_time_minutes} minutes")
