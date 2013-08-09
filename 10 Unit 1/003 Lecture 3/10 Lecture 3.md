# Lecture 3: Problem Solving

<iframe width="640" height="360" src="http://www.youtube.com/embed/ggxY20cXql8?feature=player_detailpage" frameborder="0" allowfullscreen></iframe>

## Download

- [iTunes U](http://itunes.apple.com/us/itunes-u/lecture-3-problem-solving/id499270153?i=110101035)
- [Internet Archive](http://www.archive.org/download/MIT6.00SCS11/MIT6_00SCS11_lec03_300k.mp4)

## About

Topics covered: Termination, decrementing functions, exhaustive enumeration, brute force, while loop, for loop, approximation, specifications, bisection search.




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

What does it mean for a program to terminate?
<a href="#" onclick="show('answer-1'); return false;">show</a>

<div id="answer-1" style="display: none;">Either the program will return a value, or throw an exception. A program that does not terminate runs indefinitely, typically because it's gotten stuck in a loop.</div>

What is a for loop?
<a href="#" onclick="show('answer-2'); return false;">show</a>

<div id="answer-2" style="display: none;">A for loop takes some sort of iterable object (a list, tuple, or string) and performs its function once for each item in that object. Any function that depends on the input can have a different result at each step, since the input is the current item.</div>



