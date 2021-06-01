import line_profiler

def  fun(ar):
    print(ar)


ar = "hello world"
profile = LineProfiler(fun(ar))

print(profile.print_stats())
