var amount = 4;

$(document).ready(function() {

	$('#addField').click(function() {
		if(amount < 10){
			$("#addAnswer").append(" <input type=\"text\" class=\"mcinputbox req\" name=\"answers[]\" placeholder=\"Type your answer in here\">");
			amount++;
		}
	});
	$('#removeField').click(function() {
		if(amount > 4){
			console.log("fsdfdsf");
			$("#addAnswer input:last").remove();
			amount--;
		}

	});

	$("#check").click(function () {
			var answer = document.querySelector('input[name="answers"]:checked').value;
			var correct = document.getElementById("correct").value;
			var id_checkbox = $('input[type=radio][name="answers"]:checked').attr('id');
			var id = id_checkbox.split("-");
			var id_text = id[1];
			$('#choices').children('input').each(function () {
				if(this.value!=answer){
					this.disabled=true;
				}
			});
			if(correct==answer){
				var field = document.getElementById(id_text);
				$(field).addClass('right');
			}
			else{
				var field = document.getElementById(id_text);
				$(field).addClass('wrong');
			}
	});

	$("#preview").click(function () {
		var allFilled = true;
		$('.req').each(function() {
			if($(this).val() == '') {
				allFilled = false;
			}
		});

		if(allFilled) {
			window.open("http://localhost:8000/mc/preview");

		} else {
			alert('You have missed out one or more fields :( Please fill all of them in');
		}

	});

	$('#post-form').on('submit', function(event) {

		var $btn = $(document.activeElement);
		if($btn.attr('name') == 'save_form') {
			var allFilled = true;
			$('.req').each(function() {
				if($(this).val() == '') {
					allFilled = false;
				}
			});

			if(!allFilled) {
				alert('You have missed out one or more fields :( Please fill all of them in');
				event.preventDefault();
			}
		}

	});

});
