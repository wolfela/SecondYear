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

	function getWordPair(key) {
		for(i = 0; i < wordPairs.length; i++) {
			if(key == wordPairs[i].langA) {
				return wordPairs[i];
			}
		}
		return null;
	}
	
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

	var pairsInWindow = 5;

	// IN ACTION
	var drawnBetween = [];	// to fill with Drawn objects for buttons to draw lines between
	function Drawn($leftButton, $rightButton) { this.$left = $leftButton; this.$right = $rightButton }
	function refreshLines() {

		context.clearRect(0, 0, $canvas.width(), $canvas.height());
		for(i = 0; i < drawnBetween.length; i++) {
			var link = drawnBetween[i];
			var leftPos = link.$left.position();
			var rightPos = link.$right.position();

			leftPos.left += link.$left.width();
			leftPos.top += (link.$left.height() / 2)

			rightPos.top += (link.$right.height() / 2)
			
			draw(leftPos, rightPos);		
		}

	}

	function removeIfExists($button) {
		for(i = 0; i < drawnBetween.length; i++) {
			var item = drawnBetween[i];	
			if($button.attr('id') == item.$left.attr('id') || $button.attr('id') == item.$right.attr('id')) {		
				drawnBetween.splice(i, 1);
			}
			
		}
		//drawBetween.filter(Object);
	}

	var langAregex = RegExp('langA');
	var langBregex = RegExp('langB');
	var $selectedButton = null;

	$('.button').click(function() {

		// for drawing lines
		if($selectedButton != null) {
			var firstButtonId = $selectedButton.attr('id');
			var secondButtonId = $(this).attr('id');

			// checks the ids of the buttons to see which side they are on
			// if the second button is on the same side as the first button, the first becomes de-selected
			//	without drawing
			if(!((langAregex.test(firstButtonId) && langAregex.test(secondButtonId)) || 
				(langBregex.test(firstButtonId) && langBregex.test(secondButtonId)))) {
				
				removeIfExists($selectedButton);
				removeIfExists($(this));

				if(langAregex.test(firstButtonId)) {
					drawnBetween.push(new Drawn($selectedButton, $(this)));
				} else {
					drawnBetween.push(new Drawn($(this), $selectedButton));
				}

				refreshLines();
		
			}
			$selectedButton = null;

		} else {
			$selectedButton = $(this);
		}


		// for checking if all buttons have been linked
		if(drawnBetween.length == pairsInWindow) {
            /*print('ob: ' + drawnBetween[0].$left.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[0].$right.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[1].$left.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[1].$right.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[2].$left.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[2].$right.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[3].$left.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[3].$right.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[4].$left.attr('id') + ' pairs: ' + pairsInWindow);
			print('ob: ' + drawnBetween[4].$right.attr('id') + ' pairs: ' + pairsInWindow);*/

			for(j = 0; j < drawnBetween.length; j++) {
				var $left = drawnBetween[j].$left;
				var $right = drawnBetween[j].$right;

				var pair = getWordPair($left.text());
				
				var answerText = pair.langB;
				
				$left.removeClass('success alert');
				$right.removeClass('success alert');

				if($right.text() == answerText) {
					$left.addClass('success');
					$right.addClass('success');
				} else {
					$left.addClass('alert');
					$right.addClass('alert');
				}
                
				
			}
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

function print(msg) {
	document.writeln(msg);
}





