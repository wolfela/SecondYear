Answer = function(question, answer, isCorrect) {
	this.question = question;
	this.answer = answer;
	this.isCorrect = isCorrect
};

var answers = [];

$(document).ready(function() {

	// answer retrieval should be done before this comment


	// if no answers were retrieved, some filler ones will be added to be shown as an example
	if(answers.length === 0) {
		answers.push(new Answer('What is 9 + 10?', '21', false));
		answers.push(new Answer('Bonjour', 'Hello', true));
		answers.push(new Answer('Faire', 'To Do', true));
	}

	var correct = 0;

	for(var i = 0; i < answers.length; i++) {
		if(answers[i].isCorrect) {
			correct++;
		}
	}

	var correctPercent = correct / answers.length;

	$('#results-progress').css('width', (correctPercent * 100 + '%'));
	$('#results-progress-text').text(Math.trunc(correctPercent * 100) + '%');

	if(correctPercent < 0.4) {
		$('#progress-div').addClass('alert');
	} else if (correctPercent < 0.7) {
		$('#progress-div').addClass('warning');
	} else {
		$('#progress-div').addClass('success');
	}
	
	// adding answers to details table
	for(var i = 0; i < answers.length; i++) {
		$('#details-table').append(newDetailsRow(answers[i]));
	}

	
});

function newDetailsRow(answer) {
	var row = "<tr>";
	row += '<th>' + answer.question + '</th>';
	row += '<td>' + answer.answer + '</td>';
	row += '<td>' + (answer.isCorrect ? '&#10004' : '&#10060') + '</td>';
	row += '</tr>';
	return row;
}
