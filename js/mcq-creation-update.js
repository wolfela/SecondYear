var amount = 4;

$(document).ready(function() {
	$('#addField').click(function() {
		if(amount < 10){
			$("#addAnswer").append("<input type=\"checkbox\" class=\"checkbox\"> <input type=\"text\" class=\"mcqinputbox\" placeholder=\"Type your answer in here\"></br>");
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
