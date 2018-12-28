/**
 * Created by Administrator on 2017/7/4.
 */
$(function(){

/*
*
* */
    $('.header_nav .nav_list li a').css({'color':'#333333'});
    $(window).scroll(function () {
        var srollPos = $(window).scrollTop();
        $('.header_nav').removeClass('bg');
        $('.header_nav .nav_list  li a').css({'color':'#333333'});
        if(srollPos-10>0){
            $('.header_nav').addClass('bg');
            $('.header_nav .nav_list li a').css({'color':'#ffffff'});
        }


    });
    /*
    * news下的动态判断
    * */
    if($('.trends_main_title_news_ul li').length<4&&$('.trends_main_title_news_ul li').length){
        $('.footer').css({'position':'fixed','bottom':'0'})
    }
    /*
    * news_details下的动态判断
    * */
    function  cHange(){
        if($('.news_details')[0].offsetHeight<$(window).height()-40){
            $('.footer').css({'position':'fixed','bottom':'0'})
        }
    }
    cHange();
   window.onresize=function(){
       cHange();
    };
})