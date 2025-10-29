
# Decision Tree Classifier Implementation Without sklearn

import math

# Sample dataset (Outlook, Temperature, Humidity, Wind, Play)
dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

# Attributes
features = ['Outlook', 'Temperature', 'Humidity', 'Wind']

# --- Helper functions ---
def entropy(data):
    total = len(data)
    if total == 0:
        return 0
    positives = len([d for d in data if d[-1] == 'Yes'])
    negatives = total - positives
    p_pos = positives / total
    p_neg = negatives / total
    e = 0
    if p_pos > 0:
        e -= p_pos * math.log2(p_pos)
    if p_neg > 0:
        e -= p_neg * math.log2(p_neg)
    return e

def info_gain(data, col):
    total_entropy = entropy(data)
    values = set([d[col] for d in data])
    weighted_entropy = 0
    for v in values:
        subset = [d for d in data if d[col] == v]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    return total_entropy - weighted_entropy

# --- Build Tree ---
def build_tree(data, features):
    classes = [d[-1] for d in data]
    if classes.count(classes[0]) == len(classes):
        return classes[0]
    if not features:
        return max(set(classes), key=classes.count)

    gains = [info_gain(data, i) for i in range(len(features))]
    best = gains.index(max(gains))
    best_feature = features[best]

    tree = {best_feature: {}}
    values = set([d[best] for d in data])
    for v in values:
        subset = [d for d in data if d[best] == v]
        sub_features = features[:best] + features[best+1:]
        subtree = build_tree([s[:best] + s[best+1:] for s in subset], sub_features)
        tree[best_feature][v] = subtree
    return tree

# --- Classification ---
def classify(tree, features, sample):
    if not isinstance(tree, dict):
        return tree
    root = next(iter(tree))
    value = sample[features.index(root)]
    if value in tree[root]:
        return classify(tree[root][value], features, sample)
    else:
        return 'Unknown'

# --- Build and Test ---
tree = build_tree(dataset, features)
print("Decision Tree:\n", tree)

# Test sample
sample = ['Sunny', 'Cool', 'Normal', 'Strong']
result = classify(tree, features, sample)
print("\nClassified result for", sample, "=>", result)

# --- Accuracy ---
correct = 0
for row in dataset:
    pred = classify(tree, features, row[:-1])
    if pred == row[-1]:
        correct += 1
accuracy = correct / len(dataset) * 100
print("\nAccuracy:", round(accuracy, 2), "%")
