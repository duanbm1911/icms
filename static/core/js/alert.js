{% if messages %}
{% for message in messages %}
{% if message.tags == 'error' %}
<script>
  Swal.fire({
    text: "{{ message }}",
    icon: "error"
  });
</script>
{% else %}
<script>
  Swal.fire({
    text: "{{ message }}",
    icon: "success"
  });
</script>
{% endif %}
{% endfor %}
{% endif %}