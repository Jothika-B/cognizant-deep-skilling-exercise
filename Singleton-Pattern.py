class SingletonClassic:
    _instance = None  
 
    def __new__(cls):
        if cls._instance is None:
            print("[SingletonClassic] Creating new instance...")
            cls._instance = super().__new__(cls)
        else:
            print("[SingletonClassic] Returning existing instance.")
        return cls._instance
 
    def __init__(self):
        # Guard to avoid re-initializing attributes on repeated calls
        if not hasattr(self, "initialized"):
            self.initialized = True
            self.value = "I am the only instance!"

Output:
Creating new instance...
Returning existing instance.
obj1 is obj2: True
obj1.value: I am the only instance!

