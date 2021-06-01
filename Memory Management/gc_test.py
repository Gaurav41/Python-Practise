# gc_test.py
import gc
found_objects = gc.get_objects()
print('%d objects before' % len(found_objects))
ref = 'Sarah ' * 512000
abc = "ahsgdj" * 512000
found_objects = gc.get_objects()
print('%d objects after' % len(found_objects))
for obj in found_objects[:3]:
    print(repr(obj)[:100])