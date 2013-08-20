# Lecture 5: Objects in Python

<iframe width="640" height="360" src="http://www.youtube.com/embed/B8is52oxHBw?feature=player_detailpage" frameborder="0" allowfullscreen></iframe>

## Download

- [iTunes U](http://itunes.apple.com/us/itunes-u/lecture-5-objects-in-python/id499270153?i=110101054)
- [Internet Archive](http://www.archive.org/download/MIT6.00SCS11/MIT6_00SCS11_lec05_300k.mp4)

## About

Topics covered: Tuples, lists, dictionaries, methods, identifiers, modifying
objects, aliasing, mutability.

## Resources

- [Lecture code handout](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-5-objects-in-python/MIT6_00SCS11_lec05.pdf)
- [Lecture code](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-5-objects-in-python/lec05.py)

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

What is mutability? <a href="#" onclick="show('answer-1'); return false;">show</a>

<div id="answer-1" style="display: none;">
A mutable object's values can be changed; we must be careful when working with mutable objects not to inadvertently change them.
</div>

What is the important difference between a list and a tuple? <a href="#" onclick="show('answer-2'); return false;">show</a>

<div id="answer-2" style="display: none;">
Tuples are immutable (as are strings).
</div>

What is cloning? <a href="#" onclick="show('answer-3'); return false;">show</a>

<div id="answer-3" style="display: none;">
Cloning creates a copy of a mutable object, so that the values can be manipulated without mutating the original object.
</div>

What are the important aspects of a dictionary? <a href="#" onclick="show('answer-4'); return false;">show</a>

<div id="answer-4" style="display: none;">
A dictionary mutable, with immutable keys, and unordered.
</div>
