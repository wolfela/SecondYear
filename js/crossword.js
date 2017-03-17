var container,
    grid,
    gridSize,
    crosswordId,
    cluesList =[],
    answerList =[],
    selectedRow,
    acrossClues,
    downClues;

//Used for making crossword editor
function initCrossword(id) {
    createCrossword(id, 16, false);
    editorActions();
}

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
            if($(grid[i][j]).hasClass('selected')) {
                xArr.push(i);
                yArr.push(j);
            }
        }
    }

    if(Math.max.apply(null,xArr)-Math.min.apply(null,xArr)!=0){
        if(Math.max.apply(null,yArr)-Math.min.apply(null,yArr)==0){
            if(Math.max.apply(null, xArr) - Math.min.apply(null, xArr) == xArr.length - 1){
                $('.answerBox').attr('maxlength',xArr.length);
                return true;
            }else{
                return false;
            }
        }else{
            return false;
        }
    }else{
        if(Math.max.apply(null,yArr)-Math.min.apply(null,yArr)!=0){
            if(Math.max.apply(null,yArr)-Math.min.apply(null,yArr)==yArr.length-1) {
                $('.answerBox').attr('maxlength',xArr.length);
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
    var newRow = $('<div class=crosswordClueRow tabindex=1 id='+cluesList.length+'></div>');
    $('<p class=wordRow>' + word + '</p>').appendTo(newRow);
    $('<p class=clueRow contenteditable=true>' + clue + '</p>').appendTo(newRow);
    $('.clueDiv').append(newRow);
    $(newRow).click(function() {
        selectedRow = this;
    })
}

function addAnswer(answer) {
    var chars = answer.split('');
    var charIndex = 0;
    for(var i=0;i<gridSize;i++){
        for(var j=0;j<gridSize;j++){
            if($(grid[i][j]).hasClass('selected')) {
                $(grid[i][j]).removeClass('selected').addClass('set');
                $(grid[i][j]).attr('id',answerList.length);
                $(grid[i][j]).append('<p class=crosswordLetter>'+chars[charIndex]+'</p>');
                if(charIndex==0){
                    $(grid[i][j]).prepend('<span class=crosswordNum>'+ answerList.length +'</span>')
                }
                charIndex+=1;
            }
        }
    }
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
            cluesList.push(clue);
            answerList.push(answer);
            addClueRow(answer, clue);
            addAnswer(answer);
            disableForm(true);
        }else{

        }
    });

    $('.deleteClue').click(function() {
        var index = $(selectedRow).attr('id');
        answerList.splice(index,1);
        cluesList.splice(index,1);
        for(var i=0;i<gridSize;i++){
            for(var j=0;j<gridSize;j++){
                if($(grid[i][j]).hasClass('set') && $(grid[i][j]).attr('id')==index){
                    $(grid[i][j]).empty().removeClass('set').addClass('blank');
                }
            }
        }
        $(selectedRow).remove();
        $('.clueDiv').children.length != 0 && $('.cluesBox').css({'opacity': '0.2', 'pointer-events': 'none'});
    })
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