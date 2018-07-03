import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from hello_world import sum

print "############# Unit Test Script"

print "############# Test case 1"
total = sum(3, 4)
print "Total:", total


print "############# Test case 2"
total = sum(10, 4)
print "Total:", total

