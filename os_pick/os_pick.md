{% macro ospick(linuxURL, windowsURL, macosURL) %}
# Please select your operating system:

[Linux]({{linuxURL}}){ .md-button }
[MacOS]({{macosURL}}){ .md-button }
[Windows]({{windowsURL}}){ .md-button }
{% endmacro %}
