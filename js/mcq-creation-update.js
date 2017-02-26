var amount = 4;

$(document).ready(function() {
	$('#addField').click(function() {
		if(amount < 10){
			addFields();			
		}
	});
	$('#removeField').click(function() {
		if(amount > 4){
			$("#addAnswer").empty();
			amount--;
			
			for(i = 0; i < amount; i++){
				addSingleField();
			}	
		}
	});
});

function addFields(){
	if(amount < 10){
		$("#addAnswer").append("<input type=\"checkbox\" class=\"checkbox\"> <input type=\"text\" class=\"mcqinputbox\" placeholder=\"Type your answer in here\"></br>");
		amount++;			
	}
}

function addSingleField(){
	$("#addAnswer").append("<input type=\"checkbox\" class=\"checkbox\"> <input type=\"text\" class=\"mcqinputbox\" placeholder=\"Type your answer in here\"></br>");			
}
