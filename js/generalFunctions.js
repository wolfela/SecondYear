function checkTextField(field) {
    return ($(field).val() == '');
}

/*
For this error dialog method you need to provide a the title and message it needs to carry.
Type takes three values:
    1:User trying something that'll break the functionality
    2:User trying something that they might not want to, eg not answering a question
    3:Something messes up on our side
*/
function errorDialog(Title,warning,type) {
    var dialog = $('<div class="modalDialog"></div>');
    var closeButton = $('<input type=button class="modalClose" value="Close"/>');
    switch (type){
        case 1:
            dialog.addClass('error');
            break;
        case 2:
            dialog.addClass('uDerp');
            break;
        case 3:
            dialog.addClass('weDerp');
    }
    dialog.append('<h4 class="modalTitle">'+ Title+'</h4>');
    dialog.append('<p class="modalText">'+warning+'</p>');
    closeButton.appendTo(dialog);

    closeButton.click(function () {
        $(dialog).remove();
    });

    $('.container').append(dialog);
}