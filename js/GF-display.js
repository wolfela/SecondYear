$("#check").click(function () {
    var correct = document.getElementById("correct").value;
    correct = correct.replace(/[\[\]\']+/g, '');
    var array = correct.split(", ");

    for(var i = 1; i <= array.length; i++){
        var field = document.getElementById(i);
        var answer = field.value;

        if(answer==array[i-1]){
            $(field).addClass('right');
            $(field).prop('readonly', true);

        }else{
            $(field).addClass('wrong');
            $(field).prop('readonly', true);
        }
    }

});