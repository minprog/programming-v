# Lecture 2: Core Elements of a Program

<iframe width="640" height="360" src="http://www.youtube.com/embed/SLvTCHhu5SE?feature=player_detailpage" frameborder="0" allowfullscreen></iframe>

## Download

- [iTunes U](http://itunes.apple.com/us/itunes-u/lecture-2-core-elements-program/id499270153?i=110101057)
- [Internet Archive](http://www.archive.org/download/MIT6.00SCS11/MIT6_00SCS11_lec02_300k.mp4)

## About

Topics covered: IDLE, types of objects, operators, overloading, commands, variables, assignment, input, straight line and branching programs, looping constructs, Turing completeness, conditionals, nesting.



## Resources

- [Lecture code handout](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-2-core-elements-of-a-program/MIT6_00SCS11_lec02.pdf)

- [Lecture code](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-2-core-elements-of-a-program/lec02.py)



<script>
function hide(id)
{
    document.getElementById(id).style.display = 'none';
}

function show(id)
{
    document.getElementById(id).style.display = 'block';
}
</script>


## Check Yourself

What is a 'type'? <a href="#" onclick="show('answer-1'); return false;">show</a>

<div id="answer-1" style="display: none;">
Types are classifications of objects, which is what Python, as an OOP language, deals with. They determine how those objects are dealt with (for example, adding two integers results in an integer, two strings results in a concatenated string, and an integer and a string results in an error).
</div>

What is an 'expression'? <a href="#" onclick="show('answer-2'); return false;">show</a>

<div id="answer-2" style="display: none;">
An expression is composed of objects (or operands) and operators, and can be interpreted into a value.
</div>

What is a type conversion? <a href="#" onclick="show('answer-3'); return false;">show</a>

<div id="answer-3" style="display: none;">
A type conversion turns one type of object into another. For example, applying str to the integer 3 results in the string '3'.
</div>

What is a keyword? <a href="#" onclick="show('answer-4'); return false;">show</a>

<div id="answer-4" style="display: none;">
Keywords are words that have special meanings within a language. Many editors will display them in special colors. These words cannot be used as variables.
</div>

What is the difference between a straight line program and a branching program? <a href="#" onclick="show('answer-5'); return false;">show</a>

<div id="answer-5" style="display: none;">
A straight line program simply goes through and carries out each step. A branching program will do different things depending on conditions set within the program.
</div>

What is a conditional? <a href="#" onclick="show('answer-6'); return false;">show</a>

<div id="answer-6" style="display: none;">
A conditional statement starts with an if statement, and can also include elif and else statements.
</div>
