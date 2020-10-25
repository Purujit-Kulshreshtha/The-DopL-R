var slider = document.getElementById('range')
var output = document.getElementById('value')
var video_element = document.getElementById('video_element')
var test_div = document.getElementById('test_div')


slider.oninput = function(){
	output.innerHTML = 2*(slider.value-50);
}

slider.addEventListener("mousemove", function(){
	var x = slider.value;
	var color = "linear-gradient(90deg, rgb(19, 39, 67)" +x + "%, rgb(200, 200, 200)" + x + "%)";
	slider.style.background = color;
	
	temp = (2*(slider.value-50));

	if (temp > 0){
		alpha = (2*(slider.value-50)/100)-0.3
	}

	else if (temp < 0 ){
		alpha = (2*(slider.value-50)/100)+0.3
		alpha = -1*alpha

		console.log(alpha)
	}

	no_shift = 'rgba(0, 0, 0, 0)'
	red_shift = 'rgba(255, 0, 0,'
	blue_shift = 'rgba(0, 0, 255,'

	color_overlay = no_shift;

    is_blue = x<50;
    is_red = x>50;

    if (is_red) {
    	color_overlay = red_shift + alpha + ')';
    }

    else if (is_blue){
    	color_overlay = blue_shift + alpha + ')';
    }

    test_div.style.backgroundColor = color_overlay

})



