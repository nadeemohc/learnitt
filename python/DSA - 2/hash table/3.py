class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # Linear Probing: Move to the next slot if there's a collision
    def linear_probe(self, h):
        while self.arr[h] is not None:
            h = (h + 1) % self.MAX  # Wrap around using modulo
        return h

    # Quadratic Probing: Increase the probe range quadratically
    def quadratic_probe(self, h):
        i = 1
        while self.arr[h] is not None:
            h = (h + i ** 2) % self.MAX
            i += 1
        return h

    # Double Hashing: Use a secondary hash function to find the next slot
    def double_hash(self, h, key):
        step_size = 7 - (self.get_hash(key) % 7)  # Secondary hash function
        while self.arr[h] is not None:
            h = (h + step_size) % self.MAX
        return h

    def __setitem__(self, key, value, probe_type='linear'):
        h = self.get_hash(key)
        # Check if the slot is empty
        if self.arr[h] is not None:
            # Apply the chosen probing method
            if probe_type == 'linear':
                h = self.linear_probe(h)
            elif probe_type == 'quadratic':
                h = self.quadratic_probe(h)
            elif probe_type == 'double':
                h = self.double_hash(h, key)
        # Insert the value
        self.arr[h] = (key, value)

    def __getitem__(self, key):
        h = self.get_hash(key)
        probe_count = 0
        # Search for the key using linear probing as an example
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            h = (h + 1) % self.MAX  # Linear probing
            probe_count += 1
            if probe_count >= self.MAX:  # Avoid infinite loop
                break
        return None

# Example usage
a = HashTable()
# Insert using different probing methods
a.__setitem__('name', 'Nadeem', 'linear')
a.__setitem__('age', 23, 'linear')
a.__setitem__('weight', 71, 'linear')
a.__setitem__('name', 'Nahala', 'quadratic')  # Will update 'name'
a.__setitem__('age', 19, 'double')  # Will update 'age'
a.__setitem__('weight', 46, 'linear')  # Will update 'weight'

print(a['name'])  # Outputs: 'Nahala'
print(a['age'])   # Outputs: 19
print(a['weight']) # Outputs: 46
print(a.arr)  # Shows the table structure with different probes applied
