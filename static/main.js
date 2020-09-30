var slider = document.getElementById('range')
var output = document.getElementById('value')

output.innerHTML = 2*(slider.value-50);

slider.oninput = function(){
	output.innerHTML = 2*(slider.value-50);
}

slider.addEventListener("mousemove", function(){
	var x = slider.value;
	var color = "linear-gradient(90deg, rgb(19, 39, 67)" +x + "%, rgb(200, 200, 200)" + x + "%)";
	slider.style.background = color;

})



