var wordPairs = [];
var rows = [];
function Word(langA, langB) { this.langA = langA; this.langB = langB };
function Row(row, word) { this.row = row, this.word = word };

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

	rows = [];
	for(var j = 0; j < pairs.length; j++) {
		var row = '<tr id="pair' + j + '"></tr>';
		var wordA = '<td><input type="text" class="editor-input" name="wordA' + j + '" id="wordA' + j + '" value="' + pairs[j].langA + '" placeholder="<insert language A here>" aria-describedby="exampleHelpTex"></td>';
		var wordB = '<td><input type="text" class="editor-input"  name="wordB' + j + '" id="wordB' + j + '" value="' + pairs[j].langB + '" placeholder="<insert language B here>" aria-describedby="exampleHelpTex"></td>';
		var deleteButton = '<td><button type="button" class="alert button editor-delete" id="editor-delete' + j + '">Delete</button></td></tr>';
		
		rows.push(new Row(j, pairs[j]));

		$('#editing-table').append(row);
		$('#pair' + j).append(wordA + wordB + deleteButton);

		$('#editor-delete' + j).click(function() {
			var num = $(this).attr('id').substring(13);
			pairs.splice(num, 1);
			addWordEditor(pairs);
		});

		$('#wordA' + j).on('input', function() {
			var num = parseInt($(this).attr('id').substring(5));
			rows[num].word.langA = $('#wordA' + num).val();
		});

		$('#wordB' + j).on('input', function() {
			var num = parseInt($(this).attr('id').substring(5));
			rows[num].word.langB = $('#wordB' + num).val();
		});
		
	}
	
	// adding add button
	$('#editing-table').append('<td><a class="button editor-add" id="add-pair-button">Add</a></td>');
	$('#add-pair-button').off('click');
	$('#add-pair-button').click(function() {
		pairs.push(new Word('', ''));
		addWordEditor(pairs);
	});

	//document.writeln(getPairs()[0].langA);

}

function printPairs() {
	for(var i = 0; i < rows.length; i++) {
		document.writeln('(' + rows[i].word.langA + ',' + rows[i].word.langB + ')');
	}
}



// USE THESE FUNCTIONS TO GET WORDS FOR BACKEND PURPOSES

function getPairs() {
	var array = [];
	for(var i = 0; i < rows.length; i++) {
		array.push(rows[i].word);
	}

	return array;
}

function getLefts() {
	var array = [];
	for(var i = 0; i < rows.length; i++) {
		array.push(rows[i].word.langA);
	}

	return array;
}

function getRights() {
	var array = [];
	for(var i = 0; i < rows.length; i++) {
		array.push(rows[i].word.langB);
	}

	return array;
}


