$(document).ready(function() {

	// SETUP

	// canvas setup for drawing lines between boxes
	var canvas = document.getElementById('my-canvas');
	var context = canvas.getContext('2d');
	context.lineWidth = 2;

	var $canvas = $('#my-canvas');
	var canvasOffset = $canvas.offset();
	var offsetX = canvasOffset.left - 20;
	var offsetY = canvasOffset.top + 10;

	$(window).resize(function() {
		refreshLines();
	});

	var wordPairs = [];	// array that will be used to display words. Words stored here should be CORRECTLY paired
	function Word(langA, langB) { this.langA = langA; this.langB = langB };
	var drawingIsBlocked = false;

	// ADD ACTUAL WORD PAIRS BETWEEN HERE...

	// ...AND HERE


    var left = [];
    var right = [];
    $('#leftwords').children('input').each(function () {
    	left.push(this.value);
	});

	$('#rightwords').children('input').each(function () {
    	right.push(this.value);
	});


    for (var a=0; a < left.length; a++){

    	wordPairs.push(new Word(left[a], right[a]));
    }



	// if no words were added, the below ones will be used to demonstrate the display
	if(wordPairs.length === 0) {
		wordPairs.push(new Word('SAMPLE', 'WORDS'));
	}

	// actual arrays used for displaying words
	var wordsLangA = [];	// left column words
	var wordsLangB = [];	// right column words

	// every word pair that exists in the initial wordPairs array gets added to the two above arrays, and then shuffled
	for(var i = 0; i < wordPairs.length; i++) {
		wordsLangA.push(wordPairs[i].langA);
		wordsLangB.push(wordPairs[i].langB);
	}

	wordsLangA = shuffle(wordsLangA);
	wordsLangB = shuffle(wordsLangB);


	// associating buttons to words that were shuffled.
	// this is done in order of rows that the words appear in AFTER they have been shuffled

	// every button gets an id depending on what column they will be display on, and their position in the column
	// words on the left column have langA in the id, words on the right have langB instead
	// the number after 'word' in the id represents the column number, starting from 1

	// e.g.:
	// 	first word on left column gets id #langA-word1-button
	//	first word on right column gets id #langB-word1-button
	//	third word on right column gets id #langB-word3-button
	for(var i = 0; i < wordPairs.length; i++) {
		var wordA = wordsLangA[i];
		var wordB = wordsLangB[i];

		var $buttonA = addWordButton(true, i + 1, wordA);
		var $buttonB = addWordButton(false, i + 1, wordB);
	}

	var pairsInWindow = wordPairs.length;


	// IN ACTION

	var drawnBetween = [];	// to fill with Drawn objects for BUTTONS to draw lines between
	function Drawn($leftButton, $rightButton) { this.$left = $leftButton; this.$right = $rightButton };

	var langAregex = RegExp('langA');	// to check if word is on left column
	var langBregex = RegExp('langB');	// to check if word is on right column
	var $selectedButton = null;	// it is assumed that no buttons have been clicked before the document is open

	$('.button').click(function() {
		// if the 'Check Answer' button was clicked, don't do anything
		if($(this).attr('id') != 'check') {
			// for drawing lines
			if($selectedButton != null) {
				var firstButtonId = $selectedButton.attr('id');
				var secondButtonId = $(this).attr('id');

				// checks the ids of the buttons to see which side they are on
				// if the second button is on the same side as the first button, the first becomes de-selected
				//	without drawing
				if(!(	// negate result of the two checks below
					(langAregex.test(firstButtonId) && langAregex.test(secondButtonId)) || // if both buttons are on left column
					(langBregex.test(firstButtonId) && langBregex.test(secondButtonId)))) { // if both buttons are on right column

					// if the check above passes, then a new link is made while removing links for the two buttons to be used for the new link
					removeIfExists($selectedButton);	// button that was clicked on first
					removeIfExists($(this));	// button that was clicked on second (or the one that was clicked to fire this event)

					// when inserting Drawn objects in the drawnBetween array, buttons on the left should come first
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

		}
	});

	$('#check').click(function() {

				var right = getRightLinked();
		var left = getLeftLinked();
		document.getElementById('listA').value = left;
		console.log(document.getElementById('listA').value);
		document.getElementById('listB').value = right;

		drawingIsBlocked = true;
		// for checking if all buttons have been linked
		if(drawnBetween.length == pairsInWindow) {
			var correct = 0;

			for(var j = 0; j < drawnBetween.length; j++) {
				var $left = drawnBetween[j].$left;
				var $right = drawnBetween[j].$right;
				var pair = getWordPair($left.text());

				var answerText = pair.langB;

				$left.removeClass('success alert');
				$right.removeClass('success alert');

				if($right.text() == answerText) {
		            		correct++;
					$left.addClass('success');
					$right.addClass('success');
				} else {
					$left.addClass('alert');
					$right.addClass('alert');
				}

			}

		}
	});

	// creates a button for a word, adds it to the button grid, and returns it for use with jQuery
	function addWordButton(isLeft, row, text) {
		var id = '';
		if(isLeft) {
			id += 'langA-word' + row + '-button';
		} else {
			id += 'langB-word' + row + '-button';
		}

		var html = $('<button type="button" id="' + id + '" class="button grid-button">' + text + '</button>');

		if(isLeft) {
			$('#button-grid-left').append(html);
		} else {
			$('#button-grid-right').append(html);
		}
	}

	// function for drawing lines between boxes
	// when calling this function, it should be given two position objects, which can be retrieved
	// by invoking .position() on a jQuery object
	function draw(fromPos, toPos) {
		context.beginPath();
		context.moveTo(fromPos.left, fromPos.top);
		context.lineTo(toPos.left, toPos.top);
		context.stroke();

		var right = getRightLinked();
		var left = getLeftLinked();
		document.getElementById('listA').value = left;

		document.getElementById('listB').value = right;
	}

	// checks to see if there are any word pairs that exist with the given key.
	// if so, then the Word object containg the pair is returned
	function getWordPair(key) {
		for(var i = 0; i < wordPairs.length; i++) {
			if(key == wordPairs[i].langA) {
				return wordPairs[i];
			}
		}
		return null;
	}

	// clears the canvas, and redraws the lines depending on the contents of the drawnBetween array
	function refreshLines() {
		if(!drawingIsBlocked) {
			context.clearRect(0, 0, $canvas.width(), $canvas.height());
			for(var i = 0; i < drawnBetween.length; i++) {
				var link = drawnBetween[i];
				var leftPos = link.$left.position();
				var rightPos = link.$right.position();

				leftPos.left += link.$left.width();
				leftPos.top += (link.$left.height() / 2)

				rightPos.top += (link.$right.height() / 2)

				draw(leftPos, rightPos);
			}
		}

	}

	// this function should be used to remove buttons from links to other buttons
	function removeIfExists($button) {
		for(var i = 0; i < drawnBetween.length; i++) {
			var item = drawnBetween[i];	// Drawn pair
			if($button.attr('id') == item.$left.attr('id') || $button.attr('id') == item.$right.attr('id')) {
				drawnBetween.splice(i, 1);
			}

		}
	}

	// creates an array containing linked Word objects and returns it.
	// for each Word object, you should use .langA to retrieve the left word, and .langB to retrieve the right word
	function getLinks() {
		var linked = [];

		for(var i = 0; i < drawnBetween.length; i++) {
			var db = drawnBetween[i];
			linked.push(new Word(db.$left.text(), db.$right.text()));
		}

		return linked;
	}

	function getLeftLinked() {
		var linked = [];

		for(var i = 0; i < drawnBetween.length; i++) {
			var db = drawnBetween[i];
			linked.push(db.$left.text());
		}

		return linked;
	}
	function getRightLinked() {
		var linked = [];

		for(var i = 0; i < drawnBetween.length; i++) {
			var db = drawnBetween[i];
			linked.push(db.$right.text());
		}

		return linked;
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




