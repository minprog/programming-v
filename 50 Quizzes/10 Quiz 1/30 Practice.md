### 1

Answer the questions with True or False.

#### 1.1

Floating point arithmetic behaves exactly like normal arithmetic on real
numbers

**A:** FALSE. Floating point provides only an approximation to real
numbers.

#### 1.2

On all inputs, a bisection search will run faster than a linear search.

**A:** FALSE. It has a higher asymptotic complexity, but there can be inputs on which it will run
more slowly. Consider, for example, searching for an element that happens to the
first element of the list.

### 2

What does this code print?

#### 2.1

    T = (0.1, 0.1)
    x = 0.0
    for i in range(len(T)):
      for j in T:
        x += i + j
        print x
    print i

**A:**

0.1

0.2

1.3

2.4

1

#### 2.2

    def f(s):
      if len(s) <= 1:
        return s
      return f(f(s[1:])) + s[0] #Note double recursion
    
    print f('mat')
    print f('math')

**A:**

atm

hatm

### 3

Implement the body of this function

    def findAll(wordList, lStr):
      """assumes: wordList is a list of words in lowercase.
          lStr is a str of lowercase letters.
          No letter occurs in lStr more than once
      returns: a list of all the words in wordList that contain
          each of the letters in lStr exactly once and no
          letters not in lStr."""

**A:**

    def findAll(wordList, letters):
      result = []
      letters = sorted(letters)
      for w in wordList:
        w = sorted(w)
        if w == letters:
          result.append(w)
      return result



