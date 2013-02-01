# Lecture 6: Recursion

<iframe width="640" height="360" src="http://www.youtube.com/embed/WbWb0u8bJrU?feature=player_detailpage" frameborder="0" allowfullscreen></iframe>

## Download

- [iTunes U](http://itunes.apple.com/us/itunes-u/lecture-6-recursion/id499270153?i=110101040)
- [Internet Archive](http://www.archive.org/download/MIT6.00SCS11/MIT6_00SCS11_lec06_300k.mp4)

## About

Topics covered: Dictionaries, modular abstraction, divide and conquer, recursion, tower of Hanoi, base case, Fibonacci sequence.



## Resources

- [Lecture code handout](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/MIT6_00SCS11_lec06.pdf)

- [Lecture code](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/lec06.py)



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

What is recursion?
<a href="#" onclick="show('answer-1'); return false;">show</a>

<div id="answer-1" style="display: none;">Recursion, or "divide-and-conquer", allows us to define a function that calls itself to solve a problem by breaking it into simpler cases.</div>

What is a recursive case?
<a href="#" onclick="show('answer-2'); return false;">show</a>

<div id="answer-2" style="display: none;">A recursive case calls the recursive procedure on a simpler case (usually a part of the input).</div>

What is a base case?
<a href="#" onclick="show('answer-3'); return false;">show</a>

<div id="answer-3" style="display: none;">A base case is necessary in recusion; it determines when the procedure returns a value (or terminates), rather than contiuing the recursive process.</div>



