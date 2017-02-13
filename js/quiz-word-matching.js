$(document).ready(function() {

	// SETUP
	var wordPairs = [];
	function Word(langA, langB) {
						this.langA = langA;
						this.langB = langB;
					  };

	wordPairs.push(new Word('wordA1', 'wordB1'));
	wordPairs.push(new Word('wordA2', 'wordB2'));
	wordPairs.push(new Word('wordA3', 'wordB3'));
	wordPairs.push(new Word('wordA4', 'wordB4'));
	wordPairs.push(new Word('wordA5', 'wordB5'));
	
	var wordsLangA = [];
	var wordsLangB = [];

	for(i = 0; i < 5; i++) {
		wordsLangA.push(wordPairs[i].langA);
		wordsLangB.push(wordPairs[i].langB);
	}

	wordsLangA = shuffle(wordsLangA);
	wordsLangB = shuffle(wordsLangB);
	


	for(i = 0; i < wordPairs.length; i++) {
		var wordA = wordsLangA[i];
		var wordB = wordsLangB[i];
	
		var $buttonA = $('#langA-word' + (i + 1) + '-button');
		var $buttonB = $('#langB-word' + (i + 1) + '-button');

		$buttonA.text(wordA);
		$buttonB.text(wordB);
	}

});

function shuffle(array) {
	for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}




