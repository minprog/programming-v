# Lecture 7: Debugging

<iframe width="640" height="360" src="http://www.youtube.com/embed/5gt2WDBl8-0?feature=player_detailpage" frameborder="0" allowfullscreen></iframe>

## Download

- [iTunes U](http://itunes.apple.com/us/itunes-u/lecture-7-debugging/id499270153?i=110101037)
- [Internet Archive](http://www.archive.org/download/MIT6.00SCS11/MIT6_00SCS11_lec07_300k.mp4)

## About

Topics covered: Binary, float, floating point, approximations, debugging, runtime error.

## Resources

- [Lecture code handout](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/MIT6_00SCS11_lec07.pdf)
- [Lecture code](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/lec07.py)
- [Lecture slides](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-7-debugging/MIT6_00SCS11_lec07_slides.pdf)

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

Why do computers use binary representations? <a href="#" onclick="show('answer-1'); return false;">show</a>

<div id="answer-1" style="display: none;">
It's easy to build hardware with two states, on and off.
</div>

Why shouldn't we test for equality with floats? <a href="#" onclick="show('answer-2'); return false;">show</a>

<div id="answer-2" style="display: none;">
Because computers use binary, floats are actually very close approximations of the actual values. Testing for equality can result in an unexpected error, so it's better to determine whether two numbers are close enough for our purpose rather than precisely equal.
</div>

When debugging, how can you ensure that the values in your program are the ones you think they are? <a href="#" onclick="show('answer-3'); return false;">show</a>

<div id="answer-3" style="display: none;">
Use print statements.
</div>
