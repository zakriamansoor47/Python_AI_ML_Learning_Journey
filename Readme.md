# 🧠 Python AI & Machine Learning Journey

Welcome to my **Python AI & Machine Learning Learning Journey** repository! 🚀

This repository documents my structured, hands-on progression from core Python fundamentals and software engineering patterns to mathematical foundations, natural language processing (NLP), classical machine learning, and neural networks—built **from scratch** without relying on black-box high-level frameworks.

---

## 📑 Table of Contents

- [Repository Overview](#-repository-overview)
- [Projects in Detail](#-projects-in-detail)
  - [Project 1: Persistent CLI Task Manager](#project-1-persistent-cli-task-manager)
  - [Project 2: Mini-NLP Corpus Analyzer & Next-Word Predictor](#project-2-mini-nlp-corpus-analyzer--next-word-predictor)
  - [Project 3: Custom Math Vector Engine](#project-3-custom-math-vector-engine)
  - [Project 4: The Perceptron (Single-Layer Neural Network)](#project-4-the-perceptron-single-layer-neural-network)
- [Prerequisites & Setup](#-prerequisites--setup)

---

## 🔭 Repository Overview

The philosophy behind this learning journey is **first-principles mastery**:
1. **Core Engineering**: Clean Python programming, state management, persistent storage, and error handling.
2. **Applied NLP & Statistics**: Understanding text tokenization, corpora statistics, vocabulary analysis, and n-gram language models.
3. **Linear Algebra & Vector Math**: Writing mathematical building blocks (vectors, dot products, norms, cosine similarities) manually to understand what libraries like NumPy do under the hood.
4. **Machine Learning from Scratch**: Constructing algorithmic foundations—starting with Rosenblatt's Perceptron, advancing toward multi-layer neural networks, backpropagation, and deep learning architectures.

---

## 🛠️ Projects in Detail

### Project 1: Persistent CLI Task Manager

#### 📖 Overview
An interactive command-line task manager that allows you to create, organize, and track tasks with persistent storage across sessions.

#### 🚀 Key Features
- Add, view, complete, and delete tasks easily.
- Assign priorities (`high`, `medium`, `low`) and update them anytime.
- Automatically saves and loads tasks from a local `tasks.json` file.
- Formatted tabular terminal display with user-friendly input validation.

---

### Project 2: Mini-NLP Corpus Analyzer & Next-Word Predictor

#### 📖 Overview
A text analysis and predictive NLP tool built in pure Python to analyze text files and predict subsequent words using statistical patterns without external libraries.

#### 🚀 Key Features
- Cleans and normalizes text (strips punctuation and converts to lowercase).
- Computes corpus stats (total words, unique vocabulary, and lexical diversity).
- Identifies top most frequent words with optional stopword filtering.
- Predicts the most likely next word using 2-word patterns (bigrams).

---

### Project 3: Custom Math Vector Engine

#### 📖 Overview
A lightweight vector mathematics library built completely from scratch in pure Python (without NumPy) to serve as the mathematical foundation for machine learning algorithms.

#### 🚀 Key Features
- Supports basic vector arithmetic (`+`, `-`, and scalar multiplication).
- Calculates vector dot products and Euclidean magnitude (length).
- Normalizes vectors into unit vectors.
- Computes Cosine Similarity to measure directional similarity between vectors (used in AI embeddings).

---

### Project 4: The Perceptron (Single-Layer Neural Network)

#### 📖 Overview
An implementation of Frank Rosenblatt's classic 1958 Perceptron—the earliest building block of neural networks—built from scratch using the custom vector engine.

#### 🚀 Key Features
- Built using the custom `Vector` class for inputs and weights.
- Calculates linear combinations and applies a step activation function ($0$ or $1$).
- Implements the Perceptron Learning Rule to update weights and bias on errors.
- Automatically detects convergence and successfully learns linearly separable binary logic (tested on the OR gate).

---

## ⚙️ Prerequisites & Setup

### Environment Requirements
- **Python**: Version `3.8+` recommended.
- **Dependencies**: The projects currently use standard Python libraries and custom implementations (no third-party packages required).

### Quick Clone & Run
```bash
# Clone the repository
git clone https://github.com/your-username/python-ai-ml-learning-journey.git

# Navigate into the workspace
cd "Python AI & ML learning Journey"

# Run any project directly
python "Project 4 - The Perceptron/perceptron.py"
```

---

## 👨‍💻 Author

**Zakria**  
*Exploring the inner workings of AI & Machine Learning from the ground up.*
