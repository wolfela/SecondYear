
$(document).ready(function() {
    var correct = document.getElementById('questions-correct-td').innerText;
    var questioncount = document.getElementById('questions-total-td').innerText;
	var correctPercent = correct / questioncount;
	$('#results-progress').css('width', (correctPercent * 100 + '%'));
	$('#results-progress-text').text(Math.trunc(correctPercent * 100) + '%');

	if(correctPercent < 0.4) {
		$('#progress-div').addClass('alert');
	} else if (correctPercent < 0.7) {
		$('#progress-div').addClass('warning');
	} else {
		$('#progress-div').addClass('success');
	}
	
});

