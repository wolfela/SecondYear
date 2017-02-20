var wordPairs = [];
function Word(langA, langB, page) { this.langA = langA; this.langB = langB, this.page = page };
$(document).ready(function() {

	wordPairs.push(new Word('wordA1ddddddgrtrehth', 'wordB1ghpowh', 1));
	wordPairs.push(new Word('wordA2fbdfbd', 'wordB2drfbhdfhbd', 1));
	wordPairs.push(new Word('wordA3', 'wordB3', 1));
	wordPairs.push(new Word('wordA4edgfew', 'wordB4esfesf', 2));
	wordPairs.push(new Word('wordA5', 'wordB5', 3));

	addTable(wordPairs);
	
});

addIfNotExists = function(array, elem) {
	var exists = false;
	for(a = 0; a < array.length; a++) {
		if(array[a] == elem) {
			exists = true;
		}
	}

	if(!exists) {
		array.push(elem);
	}

	return array;
}

addTable = function(pairsArray) {
	$('#editing-div').hide();
	$('#word-sets-div').show();
	$('#table').empty();
	$('#table').append('<tr id="row1"></td>');

	var pageNumbers = [];
	var colLimit = 2;
	var pagesAdded = 0;

	

	for(i = 0; i < pairsArray.length; i++) {
		pageNumbers = addIfNotExists(pageNumbers, pairsArray[i].page);
	}

	// adding columns
	for(j = 0; j < pageNumbers.length; j++) {
		pagesAdded++;
		var rowNum = Math.ceil(pagesAdded / colLimit);
		if(pagesAdded % colLimit == 0) {
			$('#table').append('<tr id="row' + (rowNum + 1) + '"></tr>');
		} 

		var pageNum = pageNumbers[j];
		var elem = '<div class="div-col" id="page' + pageNum + '"></div>';
		$('#row' + rowNum).append('<td class="cell" id="set' + pageNum + '"></td>');
		$('#set' + pageNum).append(elem);
	}
		
	// adding words
	for(k = 0; k < pairsArray.length; k++) {
		var wordA = pairsArray[k].langA;
		var wordB = pairsArray[k].langB;
		var pageNum = pairsArray[k].page;

		var str = '<p>' + wordA + ' - ' + wordB + '</p>';
		
		$('#page' + pageNum).append(str);
	}

	// adding action buttons
	for(l = 0; l < pageNumbers.length; l++) {
		var pageNum = pageNumbers[l];
		var editButton = '<a class="button edit" id="edit-page' + pageNum + '">Edit</a>';
		var deleteButton = '<button type="button" class="alert button delete" id="delete' + pageNum + '">Delete</button>';
			
		

		var buttonGroup = '<div class=button-group>' + editButton + deleteButton + '</div>'; 
		$('#page' + pageNumbers[l]).append(buttonGroup);

		// click listener for edit buttons
		$('#edit-page' + pageNum).click(function() {
			var num = $(this).attr('id').substring(9);
			addWordEditor(wordPairs, num);
			
		});

		// click listener for delete buttons
		$('#delete' + pageNum).click(function() {
			var page = $(this).attr('id').substring(6);
			for(m = 0; m < wordPairs.length; m++) {
				if(wordPairs[m].page == page) {
					wordPairs.splice(m, 1);
					m--;
				}
			}
			addTable(wordPairs);		
		});
	}

}


addWordEditor = function(array, page) {
	$('#word-sets-div').hide();
	$('#editing-div').show();

	$('#editing-div').empty();
	$('#editing-div').append('<div id="editing-table-div"><div>');
	$('#editing-table-div').append('<table id="editing-table"></table>');

	var pairs = [];
	for(i = 0; i < array.length; i++) {
		if(array[i].page == page) {
			pairs.push(array[i]);
		}
	}

	for(j = 0; j < pairs.length; j++) {
		var row = '<tr id="pair' + j + '"></tr>';
		var wordA = '<td><input type="text" class="editor-input" id="wordA' + j + '" value="' + pairs[j].langA + '" placeholder="<insert language A here>" aria-describedby="exampleHelpTex"></td>';
		var wordB = '<td><input type="text" class="editor-input" id="wordB' + j + '" value="' + pairs[j].langB + '" placeholder="<insert language A here>" aria-describedby="exampleHelpTex"></td>';
		var deleteButton = '<td><button type="button" class="alert button editor-delete" id="editor-delete' + j + '">Delete</button></td></tr>';
		
		$('#editing-table').append(row);
		$('#pair' + j).append(wordA + wordB + deleteButton);

		$('#editor-delete' + j).click(function() {
			var num = $(this).attr('id').substring(13);
			pairs.splice(num, 1);
			addWordEditor(pairs, page);
		});
		
	}

	// adding add button
	$('#editing-table').append('<td><a class="button editor-add" id="add-pair-button">Add</a></td>');
	$('#add-pair-button').click(function() {
		pairs.push(new Word('', '', page));
		addWordEditor(pairs, page);
		
	});

	// adding save button
	$('#editing-div').append('<button type="button" class="success button" id="save-pairs-button">Save</button>');
	$('#save-pairs-button').click(function() {
		// updating words
		for(w = 0; w < pairs.length; w++) {
			pairs[w].langA = $('#wordA' + w).val();
			pairs[w].langB = $('#wordB' + w).val();
		}

		for(j = 0; j < pairs.length; j++) {
			wordPairs = addIfNotExists(wordPairs, pairs[j]);
			//document.write('(' + pairs[j].langA + ',' + pairs[j].langB + ',' + pairs[j].page + ') ');
		}
		
		addTable(wordPairs);
	});
	
}
