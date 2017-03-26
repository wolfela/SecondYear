
	$('#post-form').on('submit', function(event) {

		var $btn = $(document.activeElement);
		if($btn.attr('name') == 'add_question') {
			var allFilled = true;
			if (!$("input[name='type']:checked").val()) {
   				allFilled = false;
			}

			if(!allFilled) {
				alert('You have not selected a question type!');
				event.preventDefault();
			}
		}


		if($btn.attr('name') == 'save_form') {
			var t = document.getElementById('titles').value;
			if(t=="[]"){
				alert('You need to add at least one question!');
				event.preventDefault();
			}
		}
	});


