import os
a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print os.path.join(a, "article\\templates")
