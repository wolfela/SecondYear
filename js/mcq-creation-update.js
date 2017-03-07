var amount = 4;

$(document).ready(function() {
	$('#addField').click(function() {
		if(amount < 10){
			var $newcheckbox = $("<input type=\"checkbox\" class=\"checkbox\">");
			var $newinputbox = $("<input type=\"text\" class=\"mcqinputbox\" placeholder=\"Type your answer in here\"></br>");
			var inputboxid = "mcqinputbox" + (amount);
			var checkboxid = "mcqcheckbox" + (amount);
			$newcheckbox.attr("id", checkboxid);
			$newinputbox.attr("id", inputboxid);
			$("#addAnswer").append($newcheckbox, $newinputbox);
			amount++;			
		}
	});
	$('#removeField').click(function() {
		if(amount > 4){
			$("#addAnswer input:last").remove();
			$("#addAnswer input:last").remove();
			$("#addAnswer br:last").remove();
			amount--;
		}
	});
});
