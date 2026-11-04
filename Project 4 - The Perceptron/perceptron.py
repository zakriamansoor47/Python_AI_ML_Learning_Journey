from vector_engine import Vector

class Perceptron:
    def __init__(self, num_features, learning_rate=0.1):
        self.weights = Vector([0.0] * num_features) 
        self.bias = 0.0
        self.lr = learning_rate

    def predict(self, x):
        if isinstance(x, Vector):
            z = (self.weights * x) + self.bias
            if z >= 0:
                return 1
            else:
                return 0
        else:
            raise ValueError("Input Should be a Vector")
        
    def train(self, training_data, epochs=10):
        for epochs in range(epochs):
            mistakes = 0
            for (x, target_y) in training_data:
                y = self.predict(x)
                error = target_y - y
                if error != 0:
                    self.weights = self.weights + (self.lr * error) * x
                    self.bias = self.bias + (self.lr * error)
                    mistakes += 1

            if mistakes == 0: 
                print(f"Epoch {epochs}: {mistakes} mistakes (Converged!)")
                break
            else: 
                print(f"Epoch {epochs}: {mistakes} mistakes")

# The "OR" Gate Dataset:
# [0, 0] -> 0
# [0, 1] -> 1
# [1, 0] -> 1
# [1, 1] -> 1
or_data = [
    (Vector([0, 0]), 0),
    (Vector([0, 1]), 1),
    (Vector([1, 0]), 1),
    (Vector([1, 1]), 1)
]

brain = Perceptron(num_features=2, learning_rate=0.1)
print("Before training:")
for x, y in or_data:
    print(f"Input: {x} -> Predicted: {brain.predict(x)} (Actual: {y})")

# Train the model!
brain.train(or_data, epochs=15)
print("\nAfter training:")
for x, y in or_data:
    print(f"Input: {x} -> Predicted: {brain.predict(x)} (Actual: {y})")