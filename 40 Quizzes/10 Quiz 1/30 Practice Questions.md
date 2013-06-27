
### 1

Answer the questions with True or False.

#### 1.1

Floating point arithmetic behaves exactly like normal arithmetic on real
numbers

#### 1.2

On all inputs, a bisection search will run faster than a linear search.

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

#### 2.2

    def f(s):
        if len(s) <= 1:
            return s
        return f(f(s[1:])) + s[0] #Note double recursion
    
    print f('mat')
    print f('math')

### 3

Implement the body of this function

    def findAll(wordList, lStr):
      """assumes: wordList is a list of words in lowercase.
          lStr is a str of lowercase letters.
          No letter occurs in lStr more than once
      returns: a list of all the words in wordList that contain
          each of the letters in lStr exactly once and no
          letters not in lStr."""

### 4

The following code does not meet its specification. Correct it.

    def addVectors(v1, v2):
        """assumes v1 and v2 are lists of ints.
            Returns a list containing the pointwise sum of
            the elements in v1 and v2. For example,
            addVectors([4,5], [1,2,3]) returns [5,7,3],and
            addVectors([], []) returns []. Does not modify inputs."""
        if len(v1) > len(v2):
            result = v1
            other = v2
        else:
            result = v2
            other = v1
        for i in range(len(other)):
            result[i] += other[i]
        return result

