$(document).ready(function() {
    var opener = window.opener;
    if(opener) {
        var answers = opener.document.getElementsByClassName("mcinputbox");
        var inputs = [];

        for(var i = 0; i < answers.length; i++){
            inputs.push(answers.item(i).value);
        }

        var shuffled = shuffle(inputs);

        for(var i = 0; i < shuffled.length; i++){

           var input = $('<input type="radio" class="checkbox" name="answers"> ' 
            + '<p class="answer" id=a1>'+ shuffled[i] +'</p></br>');

            $('#choices').append(input);
        }

        var value = opener.document.getElementById("title").value;
        var title = '<p class="questions" id=q>' + value + '</p></br>';
        $('#title').append(title);
  }

  function shuffle(array) {
  for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

	});

