### 1

#### 1.1

FALSE. Floating point provides only an approximation to real
numbers.

#### 1.2

FALSE. It has a higher asymptotic complexity, but there can be inputs on which it will run
more slowly. Consider, for example, searching for an element that happens to the
first element of the list.

### 2

#### 2.1

    0.1
    0.2
    1.3
    2.4
    1

#### 2.2

    atm
    hatm

### 3

    def findAll(wordList, letters):
        result = []
        letters = sorted(letters)
        for w in wordList:
            w = sorted(w)
            if w == letters:
                result.append(w)
        return result

### 4

insert the lines

    v1 = v1[:]
    v2 = v2[:]

before the first line of executable code.

