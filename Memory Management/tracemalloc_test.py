import tracemalloc
tracemalloc.start(5)  # save upto 5 stack frames
time1 = tracemalloc.take_snapshot()
obj1 = ['10' * 8000]
obj12 = 'Sarah ' * 51200
time2 = tracemalloc.take_snapshot()
stats = time2.compare_to(time1, 'lineno',"traceback")
for stat in stats[:]:
    print(stat,stat.traceback.format())
