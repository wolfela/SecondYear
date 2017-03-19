function toggleCross(toggle) {
    if(toggle) {
        $('.crossPositive').css({
            '-webkit-transform': 'rotate(45deg)',
            '-moz-transform': 'rotate(45deg)',
            '-o-transform': 'rotate(45deg)',
            'transform': 'rotate(45deg)'
        });
        $('.crossNegative').css({
            '-webkit-transform': 'rotate(-45deg)',
            '-moz-transform': 'rotate(-45deg)',
            '-o-transform': 'rotate(-45deg)',
            'transform': 'rotate(-45deg)'
        });
    }else{
        $('.crossNegative, .crossPositive').css({
            '-webkit-transform': 'rotate(0deg)',
            '-moz-transform': 'rotate(0deg)',
            '-o-transform' : 'rotate(0deg)',
            'transform': 'rotate(0deg)'
        });
    }
}

$(document).ready(function() {

    var $menuButton = $(".hamburger"),
        $content = $(".container"),
        $menu = $(".menu-content"),
        $sidebar = $(".sidebar"),
        $menuCross = $('.cross');

    $(document).foundation();
    $menuButton.click(function(){
        $menuButton.toggleClass('collapse');
        $menuButton.css('pointer-events','none');
        $menuButton.one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend',
            function() {
                $menuButton.animate(
                    {opacity:0}, 150, 'linear' ,setTimeout((function() {
                        $content.animate({opacity: 0.5}, 350);
                        $menu.animate({opacity: 1, 'z-index': 1}, 200);
                        $sidebar.animate({width: "170px"}, 350);
                        $menuCross.animate({opacity:'1'},300,'linear',function() {
                            $menuCross.css('pointer-events','auto');
                            toggleCross(true);
                        });
                    }), 100)
                )
            }
        );
    });

    $menuCross.click(function() {
        toggleCross(false);
        $menuCross.css('pointer-events','none');
        $menuCross.animate(
            {opacity: '0'}, 150,'linear',setTimeout((function() {
                $content.animate({opacity: 1}, 350);
                $menu.animate({opacity: 1, 'z-index': -1}, 200);
                $sidebar.animate({width: "0px"}, 350);
                $menuButton.animate({opacity: 1},300,'linear',function() {
                    $menuButton.css('pointer-events','auto');
                    $menuButton.toggleClass('collapse')
                })
            }),200)
        );
    })
});
