var loginUrl = "./login";

$(document).ready(function() {
	$('#login-form').attr('action', loginUrl);

	$('#login-form').on('submit', function(e) {
		e.preventDefault();
		var details = $('#login-form').serialize();
		// submit form
		$.post(loginUrl, details, function(data) {
			// TODO callback depending on success response
			document.writeln('sucess');
			var success = false;

			if(success) {
				document.writeln(data);
			} else {
				alert('You put the wrong email or password :( Please try again');
			}
		});
	});
});

