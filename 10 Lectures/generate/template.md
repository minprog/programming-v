# Lecture {{ id }}: {{ title }}

{{ embed }}

## About
Topics covered: {{ topics|join(', ') }}.

## Download

- [iTunes U]({{ iTunes }})
- [Internet Archive]({{ inetarchive }})

{% if slides is defined or code is defined %}
## Resources
{% if slides is defined %} - [Slides]({{ slides }}) {% endif %}
{% if code is defined %} - [Slides]({{ code }}) {% endif %}
{% endif %}

{% if reading is defined %}
## Further reading
{% for item in readings %}
- [{{ item[0] }}]({{ item[1] }})
{% endfor %}
{% endif %}
