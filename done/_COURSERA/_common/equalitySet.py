class Grab:
    def __init__(self, value): 
        self.obj= value
        self.match = None

    def __hash__(self):
        return hash(self.obj)

    def __eq__(self, other):
    	result = (self.obj == other)
    	if result:
    		self.match = other
    	return result

    def __getattr__(self, name):
        return getattr(self.obj, name)

def itemFromSet(item, items):
    eq = Grab(item)
    if eq in items:
        return eq.match
    else:
        items.add(item)
        return item