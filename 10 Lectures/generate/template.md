# Lecture {{ id }}: {{ title }}

{{ embed }}

## About
Topics covered: {{ topics|join(', ') }}.

## Download

- [iTunes U]({{ iTunes }})
- [Internet Archive]({{ inetarchive }})

{% if resources is defined %}
## Resources
{% for item in resources %}
- [{{ item[0] }}]({{ item[1] }})
{% endfor %}
{% endif %}

{% if reading is defined %}
## Further reading
{% for item in readings %}
- [{{ item[0] }}]({{ item[1] }})
{% endfor %}
{% endif %}
