# Lecture {{ id }}: {{ title }}

{{ embed }}

## Download

- [iTunes U]({{ iTunes }})
- [Internet Archive]({{ inetarchive }})

## About
{% if topics is defined %}
Topics covered: {{ topics|join(', ') }}.
{% elif about is defined %}
{{ about }}
{% endif %}

{% if resources is defined %}
## Resources
{% for item in resources %}
- [{{ item[0] }}]({{ item[1] }})
{% endfor %}
{% endif %}

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

{% if questions is defined %}
## Check Yourself
{% for question, answer in questions %}
{{ question }}
<a href="#" onclick="show('answer-{{ loop.index }}'); return false;">show</a><div id="answer-{{ loop.index }}" style="display: none;">{{ answer }}</div>
{% endfor %}
{% endif %}

{% if reading is defined %}
## Further reading
{% for item in readings %}
- [{{ item[0] }}]({{ item[1] }})
{% endfor %}
{% endif %}
