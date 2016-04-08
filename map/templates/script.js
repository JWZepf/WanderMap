{% extends "index.html" %}

{% block js %}
		// Here's the bulk of the google maps API
		// this file is only for JS but it also has the django template magic
		// The structure is as follows:
		// base.html <- index.html <- script.js
      var map;
      
      {% for this_marker in marker_list %}
      var marker{{ this_marker.id }}, title{{ this_marker.id }};
      var shorttitle{{ this_marker.id }}, linkto{{ this_marker.id }}, imgsrc{{ this_marker.id }};
      {% endfor %}
      
      function initMap() { 
		
		map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 0, lng: 0},
          mapTypeId: google.maps.MapTypeId.HYBRID,
          zoom: 2
        });
		
		{% for this_marker in marker_list %}
		
		coordinates = {lat: {{ this_marker.latitude }}, lng: {{ this_marker.longitude }}};
		title{{ this_marker.id }} = "{{ this_marker.longTitle }}";
		linkto{{ this_marker.id }} = "{{ this_marker.redditLink }}";
		shorttitle{{ this_marker.id }} = "{{ this_marker.shortTitle }}";
		imgsrc{{ this_marker.id }} = "{{ this_marker.imageLink }}";
		
		marker{{ this_marker.id }} = new google.maps.Marker({
		  position: coordinates,
		  map: map,
		  animation: google.maps.Animation.DROP,
		  title: shorttitle{{ this_marker.id }}
		  
		});
		marker{{ this_marker.id }}.addListener('click', showPhoto{{ this_marker.id }});
		
		{% endfor %}
      }
      
      {% for this_marker in marker_list %}
      function showPhoto{{ this_marker.id }}() {
		  $('#image-modal').modal('show');
		  var s = "<a href=" + imgsrc{{ this_marker.id }} + "><span class=\"glyphicon glyphicon-fullscreen\""
		  + "aria-label=\"full size image\"></span></a>" // little fullscreen icon that will give them link to picture
		  + "&nbsp;&nbsp;<b>" + title{{ this_marker.id }} + "</b>&nbsp;&nbsp;" + // Bold title of the reddit post (or whatever title we end up wanting)
		  "<a href=" + linkto{{ this_marker.id }} + ">View this on Reddit</a>"; // and finally a link to the specific post on reddit
		  document.getElementById("image-modal-title").innerHTML = s;
		  document.getElementById("imgmodal").src = imgsrc{{ this_marker.id }};
		}
	  {% endfor %}
{% endblock js %}
