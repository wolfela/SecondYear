var container,
    grid,
    gridSize,
    crosswordId,
    cluesList =[],
    answerList =[],
    selectedRow,
    selectionData={},
    crosswordData={};


//Used for making crossword editor
function initCrossword(id) {
    createCrossword(id, 16, false);
    editorActions();
    crosswordData.data = [];
    crosswordData.q = [];
}

$(document).ready(function() {
    initCrossword('#crosswordEditor')
});



//Used to make crossword quiz
function initCrosswordQuestion(id) {
    createCrossword(id,16, true);
    actions();
}


//Called to create crossword div
function createCrossword(id, size, question){
    crosswordId = id;
    container = $('<div class=crossword></div>').appendTo($(crosswordId));
    drawGrid(size, question)
}


//Draws blank crossword grid
function drawGrid(size, bool){
    gridSize = size;
    grid = [];
    for(var r=0; r<size; r++){
        var row = $('<div class="row"></div>').appendTo(container);
        grid[r] = [];
        for(var c=0; c<size; c++){
            var box = $('<div class="box blankBox"></div>').appendTo(row);
            if(bool) {
                $(box).append('<input type=text class=crosswordLetter maxlength=1/>');
                $(box).children().css({
                    'background':'none',
                    'border':'none',
                    '-webkit-box-shadow':'none',
                    'box-shadow':'none',
                    '-moz-box-shadow':'none',
                    'pointer-events':'none'
                });

                $(box).removeClass('blankBox').addClass('emptyBox');
            }
            grid[r][c] = box;
        }
    }
    drawBorders();
}

function drawBorders() {
    for(var i=0;i<gridSize;i++){
        $(grid[0][i]).css({'border-top':'1px solid #000'});
        $(grid[i][0]).css({'border-left':'1px solid #000'});
    }
}


/**

 QUESTION EDITOR METHOD

 **/

function disableForm(toggle) {
    if(toggle) {
        $('.clueInputBox').css({'opacity': '0.3', 'pointer-events': 'none'});
        $('.answerBox').val('');
        $('.clueInput').val('');
    }else{
        $('.clueInputBox').css({'opacity': '1', 'pointer-events': 'auto'});
        $('.cluesBox').css({'opacity': '1', 'pointer-events': 'auto'});
    }
}

function validSelection() {
    var xArr = [],
        yArr = [];

    for(var i=0;i<gridSize;i++){
        for(var j=0;j<gridSize;j++){
            if($(grid[i][j]).hasClass('selected') || $(grid[i][j]).hasClass('doubleSelect')) {
                xArr.push(i);
                yArr.push(j);
            }
        }
    }

    var minX = Math.min.apply(null,xArr),
        maxX = Math.max.apply(null,xArr),
        minY = Math.min.apply(null,yArr),
        maxY = Math.max.apply(null,yArr);

    if(maxX-minX!=0){
        if(maxY-minY==0){
            if(maxX - minX == xArr.length - 1){
                $('.answerBox').attr('maxlength',xArr.length);
                selectionData.direction = 'D';
                selectionData.x = minX;
                selectionData.y = minY;
                return true;
            }else{
                return false;
            }
        }else{
            return false;
        }
    }else{
        if(maxY-minY!=0){
            if(maxY-minY==yArr.length-1) {
                $('.answerBox').attr('maxlength',xArr.length);
                selectionData.direction = 'A';
                selectionData.x = minX;
                selectionData.y = minY;
                return true;
            }else{
                return false;
            }
        }else{
            return false;
        }
    }
}

function addClueRow(word, clue) {
    cluesList.push(clue);
    answerList.push(word);
    console.log('Got here');
    var newRow = $('<div class=crosswordClueRow tabindex=1 id='+cluesList.length+'></div>');
    $('<p class=wordRow>' + word + '</p>').appendTo(newRow);
    $('<p class=clueRow contenteditable=true>' + clue + '</p>').appendTo(newRow);
    console.log('And here');
    $('.clueDiv').append(newRow);
    $(newRow).click(function() {
        selectedRow = this;
    });
    console.log($('.'));
    disableForm(true);
    addToCrosswordData(selectionData.x,selectionData.y,word,selectionData.direction,clue);
}

function addAnswer(answer,clue) {
    var chars = answer.split('');
    var charIndex = 0;
    for(var i=0;i<gridSize;i++){
        for(var j=0;j<gridSize;j++){
            if($(grid[i][j]).hasClass('selected')) {
                $(grid[i][j]).removeClass('selected').addClass('set');
                $(grid[i][j]).attr('id',(answerList.length+1));
                $(grid[i][j]).append('<p class=crosswordLetter>'+chars[charIndex]+'</p>');
                if(charIndex==0){
                    $(grid[i][j]).prepend('<span class=crosswordNum>'+ (answerList.length+1) +'</span>')
                }
                charIndex+=1;
            }else if($(grid[i][j]).hasClass('doubleSelect')){
                if($(grid[i][j]).find('p').text()==chars[charIndex]){
                    $(grid[i][j]).removeClass('doubleSelect').addClass('set');
                    if(charIndex==0 && $(grid[i][j]).find('span').length==0){
                        $(grid[i][j]).prepend('<span class=crosswordNum>'+ (answerList.length+1) +'</span>')
                    }
                    $(grid[i][j]).attr('id',$(grid[i][j]).attr('id')+','+ (answerList.length+1));
                    charIndex+=1;
                }else{
                    //errorDialog('Incorrect Letter','Please change letter to the letter in the overlap',1);
                    return;
                }
            }
        }
    }
    console.log('YEAH BOI');
    addClueRow(answer,clue);
}

function addToCrosswordData(x,y,answer, direction, clue) {
    var entry = {};
    entry.direction = direction;
    entry.length = answer.length;
    entry.x = x;
    entry.y = y;
    entry.clue = clue;
    entry.word = answer;
    crosswordData.data.push(entry);
}

function clearBox(x,y,index) {
    var ids = $(grid[x][y]).attr('id').split(',');
    if(ids.indexOf(index)!=-1){
        if(ids.length ==1) {
            $(grid[x][y]).empty().removeClass('set').addClass('blankBox');
            $(grid[x][y]).removeAttr("id");
        }else{
            ids.splice(ids.indexOf(index),1);
            $(grid[x][y]).attr('id',ids.join(','));
        }
    }
}

function correctIndexes(index) {
    $('.crosswordNum').each(function(){
        if(parseInt($(this).text()) >index){
            $(this).text(parseInt($(this).text()) -1);
        }
    });

    $('.set').each(function() {
        if(parseInt($(this).attr('id')) >index){
            $(this).attr('id',parseInt($(this).attr('id'))-1);
        }
    });

    $('.crosswordClueRow').each(function() {
        if(parseInt($(this).attr('id')) >index){
            $(this).attr('id',parseInt($(this).attr('id'))-1);
        }
    })
}

function editorActions(){
    $(document).ready(function() {
        disableForm(true);
        $('.cluesBox').css({'opacity': '0.3', 'pointer-events': 'none'});
    });

    $('.box').click(function() {
        if($(this).hasClass('blankBox')){
            $(this).addClass('selected').removeClass('blankBox');
        }else if($(this).hasClass('selected')){
            $(this).removeClass('selected').addClass('blankBox');
        }else if($(this).hasClass('set')){
            $(this).removeClass('set').addClass('doubleSelect');
        }else if($(this).hasClass('doubleSelect')){
            $(this).removeClass('doubleSelect').addClass('set');
        }
        if(validSelection()) {
            disableForm(false);
        }else{
            disableForm(true);
        }
    });

    $('.addClue').click(function() {
        var clue = $('.clueInput').val();
        var answer = $('.answerBox').val();
        if(answer.length == $('.answerBox').attr('maxlength')){
            addAnswer(answer,clue);
        }else{

        }
    });

    $('.deleteClue').click(function() {
        var index = $(selectedRow).attr('id');
        answerList.splice(index-1,1);
        cluesList.splice(index-1,1);
        for(var i=0;i<gridSize;i++){
            for(var j=0;j<gridSize;j++){
                if($(grid[i][j]).hasClass('set')){
                    clearBox(i,j,index)
                }
            }
        }
        correctIndexes(index);
        $(selectedRow).remove();
        $('.clueDiv').children.length == 0 && $('.cluesBox').css({'opacity': '0.2', 'pointer-events': 'none'});
    })
}

function getCrosswordData() {
    console.log(crosswordData);
    return crosswordData;
}

window.getPreviewData = function() {
    console.log(crosswordData);
    return crosswordData;
}

/**

 QUESTION DISPLAY METHODS

 **/

//Will be used to display crossword questions when provided question data
function drawQuestions(crosswordData){
    var data = crosswordData.data;
    for(var i=0;i<data.length;i++){
        drawQuestionBox(data[i].x,data[i].y,data[i].length,data[i].direction,i+1);
        drawClues(data[i].clue,data[i].direction,data[i].x,data[i].y)
    }
}

function drawQuestionBox(startX,startY,size,direction,number){
    var x = parseInt(startX),
        y = parseInt(startY);
    console.log('start at: ('+x+','+y+')');
    for(var i =0;i<parseInt(size);i++){
        if(direction=="D"){
            $(grid[x+i][y]).children().css('pointer-events','auto');
            $(grid[x+i][y]).removeClass('emptyBox').addClass('blankBox');
            if(i==0){
                $(grid[x+i][y]).prepend('<span class=crosswordNum>'+ number +'</span>');
            }
        }else{
            $(grid[x][y+i]).children().css('pointer-events','auto');
            $(grid[x][y+i]).removeClass('emptyBox').addClass('blankBox');
            if(i==0){
                $(grid[x][y+i]).prepend('<span class=crosswordNum>'+ number +'</span>');
            }
        }
    }
}

function drawClues(clue, direction,startX, startY) {
    console.log('Here');
    var clueRow = $('<p>'+clue+'</p>'),
        x = parseInt(startX),
        y = parseInt(startY);
    clueRow.click(function() {
        gridReplaceClass();
        $(grid[x][y]).addClass('selected').removeClass('blankBox');
        $(grid[x][y]).children().focus();
    });
    (direction=="D")? $('.acrossClueBox').append(clueRow):$('.downClueBox').append(clueRow);
}

function gridReplaceClass() {
    for(var i=0;i<gridSize;i++){
        for(var j=0;j<gridSize;j++){
            if($(grid[i][j]).hasClass('selected')) {
                $(grid[i][j]).removeClass('selected').addClass('blankBox')
            }
        }
    }
}

function getIndex() {
    for(var i=0;i<gridSize;i++){
        for(var j=0;j<gridSize;j++){
            if($(grid[i][j]).hasClass('selected')) {
                return {
                    x:i,
                    y:j
                };
            }
        }
    }
}

function actions(){
    $('.box').click(function() {
        if($(this).hasClass('blankBox')){
            gridReplaceClass();
            $(this).addClass('selected').removeClass('blankBox');
        }
    });

    $(document).bind('keydown',function(event) {
        var index = getIndex();
        if(index!=null) {
            var x = index.x;
            var y = index.y;
            while (true) {
                if (grid[x][y].hasClass('blankBox')) {
                    gridReplaceClass();
                    $(grid[x][y]).addClass('selected').removeClass('blankBox');
                    $(grid[x][y]).children().focus();
                    return;
                } else {
                    switch (event.which) {
                        case 8:
                            $(grid[x][y]).children().val('');
                            // if(y!=0){
                            //     gridReplaceClass();
                            //     $(grid[x][y-1]).addClass('selected').removeClass('blankBox');
                            //     $(grid[x][y-1]).children().focus();
                            //     return;
                            // }
                            return;
                            break;
                        case 37:
                            if (y == 0) {
                                return;
                            } else {
                                y -= 1;
                            }
                            break;
                        case 38:
                            if (x == 0) {
                                return;
                            } else {
                                x -= 1;
                            }
                            break;
                        case 39:
                            if (y == gridSize - 1) {
                                return;
                            } else {
                                y += 1;
                            }
                            break;
                        case 40:
                            if (x == gridSize - 1) {
                                return;
                            } else {
                                x += 1;
                            }
                            break;
                        case 46:
                            $(grid[x][y]).children().val('');
                            return;
                            break;
                        default:
                            return;
                    }
                }
            }
        }
    });
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


$("#save").click(function () {

    var crossword_data = getCrosswordData();
    var url = window.location.pathname;
    var s = url.split("/");

    crossword_data.q.push({'quiz':s[2],'pos':s[3]});
    var data = JSON.stringify(crossword_data);
    console.log(data);

    $.ajax({
        url : '../../submit/',
        type: 'POST',
        data: data,
        contentType:'application/json',
        dataType: 'text',
        success: function(message){

            window.location.href = message;
        },
        error: function(){
            alert('nope');
        }
    });
});

$("#preview").click(function () {
    window.open("http://localhost:8000/cw/preview");
});

$("#cancel").click(function () {
    var url = window.location.pathname;
    var s = url.split("/");
    var rurl = "../../../quiz/edit/" + s[2];
    window.location.href = rurl;
});


