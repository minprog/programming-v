# Lecture 1: Introduction to 6.00

<iframe width="640" height="360" src="http://www.youtube.com/embed/bX3jvD7XFPs?feature=player_detailpage" frameborder="0" allowfullscreen></iframe>

## Download

- [iTunes U](http://itunes.apple.com/us/itunes-u/lecture-1-introduction-to/id499270153?i=110101056)
- [Internet Archive](http://www.archive.org/download/MIT6.00SCS11/MIT6_00SCS11_lec01_300k.mp4)

## About

Topics covered: Purposes of the course, declarative and imperative knowledge, flow of control, algorithms, fixed program and stored program computers, termination conditions, interpretation, compilation, syntax, static semantics, semantics, and types of errors.

## Resources

- [Lecture slides](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-1-introduction-to-6.00/MIT6_00SCS11_lec01_slides.pdf)

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

What is the difference between declarative and imperative knowledge? <a href="#" onclick="show('answer-1'); return false;">show</a>

<div id="answer-1" style="display: none;">
Declarative knowledge is statements of fact; imperative knowledge is "how to" knowledge.
</div>

What is the advantage of a stored-program computer? <a href="#" onclick="show('answer-2'); return false;">show</a>

<div id="answer-2" style="display: none;">
It's far more versatile than a fixed-program computer, since it interprets a program given to it and carries out those instructions, as opposed to being built to do one thing.
</div>

What are the syntax, static semantics, and semantics of a language? <a href="#" onclick="show('answer-3'); return false;">show</a>

<div id="answer-3" style="display: none;">
Syntax determines whether a string is legal, static semantics determine whether the string has meaning, and semantics assigns a meaning to a legal sentence (assuming no static semantic errors).
</div>

What sorts of errors can occur in a program? <a href="#" onclick="show('answer-4'); return false;">show</a>

<div id="answer-4" style="display: none;">
It can crash, run forever, or give a wrong answer.
</div>
