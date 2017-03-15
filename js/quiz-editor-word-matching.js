var wordPairs = [];
function Word(langA, langB) { this.langA = langA; this.langB = langB };

$(document).ready(function() {

	if(wordPairs.length === 0) {
		wordPairs.push(new Word('wordA1ddddddgrtrehth', 'wordB1ghpowh'));
		wordPairs.push(new Word('wordA2fbdfbd', 'wordB2drfbhdfhbd'));
		wordPairs.push(new Word('wordA3', 'wordB3'));
		wordPairs.push(new Word('wordA4edgfew', 'wordB4esfesf'));
		wordPairs.push(new Word('wordA5', 'wordB5'));
	}

	addWordEditor(wordPairs);
	
});

var addIfNotExists = function(array, elem) {
	var exists = false;
	for(var a = 0; a < array.length; a++) {
		if(array[a] == elem) {
			exists = true;
		}
	}

	if(!exists) {
		array.push(elem);
	}

	return array;
}

var addWordEditor = function(array) {
	$('#word-sets-div').hide();
	$('#editing-div').show();

	$('#editing-div').empty();
	$('#editing-div').append('<div id="editing-table-div"><div>');
	$('#editing-table-div').append('<table id="editing-table"></table>');

	var pairs = [];
	for(var i = 0; i < array.length; i++) {
		pairs.push(array[i]);
	
	}

	for(var j = 0; j < pairs.length; j++) {
		var row = '<tr id="pair' + j + '"></tr>';
		var wordA = '<td><input type="text" class="editor-input" name="listA[]" id="wordA' + j + '" value="' + pairs[j].langA + '" placeholder="<insert language A here>" aria-describedby="exampleHelpTex"></td>';
		var wordB = '<td><input type="text" class="editor-input"  name="listB[]" id="wordB' + j + '" value="' + pairs[j].langB + '" placeholder="<insert language B here>" aria-describedby="exampleHelpTex"></td>';
		var deleteButton = '<td><button type="button" class="alert button editor-delete" id="editor-delete' + j + '">Delete</button></td></tr>';
		
		$('#editing-table').append(row);
		$('#pair' + j).append(wordA + wordB + deleteButton);

		$('#editor-delete' + j).click(function() {
			var num = $(this).attr('id').substring(13);
			pairs.splice(num, 1);
			addWordEditor(pairs);
		});
		
	}

	// adding add button
	$('#editing-table').append('<td><a class="button editor-add" id="add-pair-button">Add</a></td>');
	$('#add-pair-button').click(function() {
		var newPairs = [];
		for(var w = 0; w < pairs.length; w++) {
			pairs[w].langA = $('#wordA' + w).val();
			pairs[w].langB = $('#wordB' + w).val();
		}
		pairs.push(new Word('', ''));
		addWordEditor(pairs);
		
	});

	
}
