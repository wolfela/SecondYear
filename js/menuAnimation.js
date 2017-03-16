$(document).ready(function() {

    var $menuButton = $(".hamburger"),
        $content = $(".container"),
        $menu = $(".menu-content"),
        $sidebar = $(".sidebar"),
        $title = $(".title-bar-title"),
        isOpen = false;

    $(document).foundation();
    $menuButton.click(function(){
        $menuButton.prop("disabled",true);
        if(isOpen){
            $menuButton.toggleClass('collapse');
            $menuButton.one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend',
                function() {
                    $menuButton.animate(
                        {opacity:0}, 100, 'linear', setTimeout((function() {
                        $content.animate({left: "-=110px",opacity:1},350);
                        $menu.animate({opacity:0, 'z-index': -1},200);
                        $sidebar.animate({width: "0px"},350)}), 100)
                    )}
            );
        }else{
            $menuButton.toggleClass('collapse');
            $menuButton.fadeIn(100);
            $menuButton.one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend',
                function() {
                    $menuButton.animate(
                        {opacity:0}, 100, 'linear' ,setTimeout((function() {
                            $content.animate({left: "+=110px", opacity: 0.5}, 350);
                            $menu.animate({opacity: 1, 'z-index': 1}, 200);
                            $sidebar.animate({width: "170px"}, 350)}), 100)
                    )
                }
            );
        }
        isOpen=!isOpen;
        $menuButton.prop("disabled",false);
    });
});
