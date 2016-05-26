from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict

Point = namedtuple('Point', 'x y')
point1 = Point(2, 3)
point2 = Point(5, 7)

print point1
print point2

deq = deque()
ddict = defaultdict()
odict = OrderedDict()
