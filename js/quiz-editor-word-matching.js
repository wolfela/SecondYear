var wordPairs = [];
var rows = [];
function Word(langA, langB) { this.langA = langA; this.langB = langB };
function Row(row, word) { this.row = row, this.word = word };

$(document).ready(function() {

	if(wordPairs.length === 0) {
		wordPairs.push(new Word('Kinga', 'Bojarczuk'));
		wordPairs.push(new Word('Ajeya', 'Jog'));
		wordPairs.push(new Word('Tatiana', 'Kmita'));
		wordPairs.push(new Word('Jared', 'Leto'));
		wordPairs.push(new Word('Mehdi', 'Ramadgdfgg'));
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
		var wordA = '<td><input type="text" class="editor-input" name="listA[]" id="wordA' + j + '" value="' + pairs[j].langA + '" placeholder="<insert language A here>" aria-describedby="exampleHelpTex"></td>';
		var wordB = '<td><input type="text" class="editor-input"  name="listB[]" id="wordB' + j + '" value="' + pairs[j].langB + '" placeholder="<insert language B here>" aria-describedby="exampleHelpTex"></td>';
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


}

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
}

window.getLefts=function() {
	var array = [];
	for(var i = 0; i < rows.length; i++) {
		array.push(rows[i].word.langA);
	}

	return array;
}

window.getRights= function() {
	var array = [];
	for(var i = 0; i < rows.length; i++) {
		array.push(rows[i].word.langB);
	}

	return array;
}


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// $("#save").click(function () {

// var wordmatch_data = getCrosswordData();
// var data = JSON.stringify(crossword_data);

// $.ajax({
//     url : './submit/',
//     type: 'POST',
//     data: data,
//     contentType:'application/json',
//     dataType: 'text',
//     success: function(message){

//         alert("saved!");
//         window.location.href = "/wherever/quiz/create/is";
//     },
//     error: function(){
//         alert('nope');
//     }
// });
// });

$("#preview").click(function () {

 window.open("http://localhost:8000/wm/preview");

});

