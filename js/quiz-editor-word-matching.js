var wordPairs = [];
var rows = [];
function Word(langA, langB) { this.langA = langA; this.langB = langB };
function Row(row, word) { this.row = row, this.word = word };

$(document).ready(function() {

	if(wordPairs.length === 0) {
		wordPairs.push(new Word('Example', 'Word'));
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
};

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
		var wordA = '<td><input type="text" class="editor-input req" name="listA[]" id="wordA' + j + '" value="' + pairs[j].langA + '" placeholder="<insert language A here>" aria-describedby="exampleHelpTex"></td>';
		var wordB = '<td><input type="text" class="editor-input req"  name="listB[]" id="wordB' + j + '" value="' + pairs[j].langB + '" placeholder="<insert language B here>" aria-describedby="exampleHelpTex"></td>';
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
				alert('You have missed out one of more fields :( Please fill all of them in');
				event.preventDefault();
			}
		}

	});


};

function printPairs() {
	for(var i = 0; i < rows.length; i++) {
		document.writeln('(' + rows[i].word.langA + ',' + rows[i].word.langB + ')');
	}
}



// USE THESE FUNCTIONS TO GET WORDS FOR BACKEND PURPOSES

window.getPairs = function() {
	var array = [];
	for(var i = 0; i < rows.length; i++) {
		array.push(rows[i].word);
	}

	return array;
};

window.getLefts=function() {
	var array = [];
	for(var i = 0; i < rows.length; i++) {
		array.push(rows[i].word.langA);
	}

	return array;
};

window.getRights= function() {
	var array = [];
	for(var i = 0; i < rows.length; i++) {
		array.push(rows[i].word.langB);
	}

	return array;
};

$("#preview").click(function () {

 window.open("http://localhost:8000/wm/preview");

});
