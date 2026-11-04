class Vector:
    def __init__(self, components):
        self.components = [float(x) for x in components]

        if len(self.components) == 0:
            raise ValueError("A vector must have at least one dimension")
        
    def __repr__(self):
        return f"Vector({[round(x, 3) for x in self.components]})"

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have same length")

        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have same length")

        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([other * x for x in self.components])

        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same dimensions")

            return sum(a * b for a, b in zip(self.components, other.components))

        return NotImplemented

    def __rmul__(self, other):
        return self * other
    
    def __eq__(self, other):
        if not isinstance(other, Vector) or len(self) != len(other):
            return False

        return self.components == other.components
    
    def magnitude(self):
        return sum(a * a for a in self.components) ** 0.5
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")

        return Vector([x / mag for x in self.components])
    
    def cosine_similarity(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")
    
        selfmag = self.magnitude()
        othermag = other.magnitude()

        if selfmag == 0 or othermag == 0:
            raise ValueError("Cosine similarity is undefined for zero vectors")
    
        result = (self * other) / (selfmag * othermag)

        return max(-1.0, min(1.0, result))

if __name__ == "__main__":
    # Initialization & Printing
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print(v1)                # Output: Vector([1.0, 2.0, 3.0])
    print(len(v1))           # Output: 3
    print(v1[0])             # Output: 1.0

    # Basic Operations
    print(v1 + v2)           # Output: Vector([5.0, 7.0, 9.0])
    print(v2 - v1)           # Output: Vector([3.0, 3.0, 3.0])
    print(v1 * 2)            # Output: Vector([2.0, 4.0, 6.0])
    print(3 * v1)            # Output: Vector([3.0, 6.0, 9.0])
    print(v1 == v2)          # Output: False

    # Dot Product
    print(v1 * v2)           # Output: 32.0 (1*4 + 2*5 + 3*6)

    # Magnitude & Normalization
    v3 = Vector([3, 4])
    print(v3.magnitude())    # Output: 5.0
    print(v3.normalize())    # Output: Vector([0.6, 0.8])

    # AI Embedding Similarity Test
    # Suppose word A = [1, 1, 0] and word B = [2, 2, 0] (same direction)
    # and word C = [0, 0, 5] (completely orthogonal / different topic)
    emb_a = Vector([1, 1, 0])
    emb_b = Vector([2, 2, 0])
    emb_c = Vector([0, 0, 5])

    print(emb_a.cosine_similarity(emb_b)) # Output: 1.0 (identical direction)
    print(emb_a.cosine_similarity(emb_c)) # Output: 0.0 (completely dissimilar)
