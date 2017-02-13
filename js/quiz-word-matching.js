$(document).ready(function() {

	// SETUP
	var canvas = document.getElementById('my-canvas');
	var context = canvas.getContext('2d');
	canvas.width = window.innerWidth;
	canvas.height = window.innerHeight;
	context.lineWidth = 2;

	var $canvas = $('#my-canvas');
	var canvasOffset = $canvas.offset();
	var offsetX = canvasOffset.left;
	var offsetY = canvasOffset.top;

	function draw(fromPos, toPos) {
		context.beginPath();
		context.moveTo(fromPos.left - offsetX, fromPos.top - offsetY);
		context.lineTo(toPos.left - offsetX, toPos.top - offsetY);
		context.stroke();
	}

	var wordPairs = [];
	function Word(langA, langB) { this.langA = langA; this.langB = langB };

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

	// IN ACTION
	var drawnBetween = [];	// to fill with Drawn objects for buttons to draw lines between
	function Drawn(left, right) { this.left = left; this.right = right }
	function refreshLines() {

		context.clearRect(0, 0, $canvas.width(), $canvas.height());
		for(i = 0; i < drawnBetween.length; i++) {
			draw(drawnBetween[i].left, drawnBetween[i].right);		
		}

	}

	function removeIfExists(pos) {
		for(i = 0; i < drawnBetween.length; i++) {
			var item = drawnBetween[i];');
			if((item.left.left == pos.left && item.left.top == pos.top) || 
				(item.right.left == pos.left && item.right.top == pos.top)) {			
				drawnBetween.splice(i, 1);
			}
			
		}
	}

	var langAregex = RegExp('langA');
	var langBregex = RegExp('langB');
	var $selectedButton = null;

	$('.button').click(function() {
		if($selectedButton != null) {
			var firstButtonId = $selectedButton.attr('id');
			var secondButtonId = $(this).attr('id');

			// checks the ids of the buttons to see which side they are on
			// if the second button is on the same side as the first button, the first becomes de-selected
			//	without drawing
			if(!((langAregex.test(firstButtonId) && langAregex.test(secondButtonId)) || 
				(langBregex.test(firstButtonId) && langBregex.test(secondButtonId)))) {

				var from = $selectedButton.position();
				from.top += ($selectedButton.height() / 2);

				var to = $(this).position();
				to.top += ($(this).height() / 2);
				

				if(langAregex.test(firstButtonId)) {
					from.left += $selectedButton.width();
					removeIfExists(from);
					removeIfExists(to);
					drawnBetween.push(new Drawn(from, to));
				} else {
					to.left += $selectedButton.width();
					removeIfExists(from);
					removeIfExists(to);
					drawnBetween.push(new Drawn(to, from));
				}

				refreshLines();
		
			}
			$selectedButton = null;

		} else {
			$selectedButton = $(this);
		}
	});

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





