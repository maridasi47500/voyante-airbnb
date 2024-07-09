

if (window.location.pathname === "/meet" && somelat.innerHTML !== "") {
somebtnpost.onclick=function(){
	overlay.style.display="block";
    const latitude = somelat.innerHTML;
    const longitude = somelon.innerHTML;
	if (musicianf.checked){
		$(".unetelle").html("une telle")
	}else{
		$(".unetelle").html("un tel")
	}
		$(".unetelle").append(" qui vient aussi de "+$(".pays1").html())
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);

var map = L.map('map').setView([latitude, longitude], 13);
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
setTimeout(function () {
    map.invalidateSize();
}, 0);
	return false;
}
}else if(window.location.pathname === "/meet" && somelat.innerHTML === ""){
	window.location="/";
}


if ((window.location.pathname === "/sign_up") && latuser.innerHTML === "" && lonuser.innerHTML === "" && myuserid.innerHTML == "") {
if (navigator.geolocation) {
	overlay.style.display="block";
  navigator.geolocation.getCurrentPosition(function(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);

var map = L.map('map').setView([latitude, longitude], 13);
membre_lat.value=latitude;
membre_lon.value=longitude;
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
setTimeout(function () {
    map.invalidateSize();
}, 0);
	  map.on('mouseup', function(e) {
    const latitude = e.latlng.lat;
    const longitude = e.latlng.lng;
membre_lat.value=latitude;
membre_lon.value=longitude;
var popup = L.popup()
    .setLatLng([parseFloat(latitude), parseFloat(longitude)])
    .setContent("vous etes ici")
    .openOn(map);
	  });
  });


} else {
  console.log("Geolocation is not supported by this browser.");
}


}
if (document.getElementById("somepic")){
    function readFile() {
	          if (this.files && this.files[0]) {
			          var FR= new FileReader();
			          FR.onload = function(e) {
					            document.getElementById("imgupload").src = e.target.result;
					            document.getElementById("imgupload").style.width = "80px";

					          };
			          FR.readAsDataURL( this.files[0] );
			        }
	        }

    document.getElementById("somepic").addEventListener("change", readFile, false);

}
