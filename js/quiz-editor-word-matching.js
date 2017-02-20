var wordPairs = [];

$(document).ready(function() {
	$('#word-sets-div').hide();
	$('#editing-div').show();
	
	function Word(langA, langB, page) { this.langA = langA; this.langB = langB, this.page = page };

	wordPairs.push(new Word('wordA1ddddddgrtrehth', 'wordB1ghpowh', 1));
	wordPairs.push(new Word('wordA2fbdfbd', 'wordB2drfbhdfhbd', 1));
	wordPairs.push(new Word('wordA3', 'wordB3', 1));
	wordPairs.push(new Word('wordA4edgfew', 'wordB4esfesf', 2));
	wordPairs.push(new Word('wordA5', 'wordB5', 3));

	//addTable(wordPairs);
	addWordEditor(1);
	
});

addIfNotExists = function(array, elem) {
	var exists = false;
	for(a = 0; a < array.length; a++) {
		if(array[a] === elem) {
			exists = true;
		}
	}

	if(!exists) {
		array.push(elem);
	}

	return array;
}

addTable = function(pairsArray) {
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


