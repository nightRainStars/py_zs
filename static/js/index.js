/**
 * Created by Administrator on 2017/6/27.
 */

$(document).ready(function() {
    /*
     * 导航滑过
     * */
    $('.nav_list a').mouseenter(function () {
        $(this).siblings().css('background','#fd0037')
    })
    $('.nav_list a').mouseleave(function () {
        $('.nav_list a').siblings().css('background','rgba(0,0,0,0)');
    })
    $('.word a').css('border-radius', '50%')
    /*
     * 导航点击效果
     * */
    $('.nav_list a').click(function () {
        $('.nav_list a').removeClass('active');
        $(this).addClass('active');
    })


    /*
     * 翻译变图
     * */
    /*$('.word-EN').click(function () {
        $('.word-CN img')[0].src = 'image/CN_nomal.png'
        $('.word-EN img')[0].src = 'image/EN_selected.png'
    })
    $('.word-CN').click(function () {
        $('.word-EN img')[0].src = 'image/EN_nomal.png'
        $('.word-CN img')[0].src = 'image/CN_selected.png'
    })*/

    /*
     * 公司简介
     * */
    $(".item1").show()
    $(".item2").hide()
    $("#main_sider_sty1 .main_sider_sty").animate({width: '250px'})
    $("#main_sider_sty2 a").css({'color': '#333333', 'border-left': '3px solid #fd0037'});
    $("#main_sider_sty1 a").css({'color': '#ffffff', 'border-left': '3px solid #fd0037'});
    $("#main_sider_sty2").click(function () {
        $("#main_sider_sty1 .main_sider_sty").css({width: '0px'});
        $("#main_sider_sty2 .main_sider_sty").animate({width: '250px'});
        $("#main_sider_sty2 a").css({'color': '#ffffff'});
        $("#main_sider_sty1 a").css({'color': '#333333'});
        $(".item2").show()
        $(".item1").hide()
    })
    $("#main_sider_sty1").click(function () {
        $("#main_sider_sty2 .main_sider_sty").css({width: '0px'});
        $("#main_sider_sty1 .main_sider_sty").animate({width: '250px'});
        $("#main_sider_sty1 a").css({'color': '#ffffff'});
        $("#main_sider_sty2 a").css({'color': '#333333'});
        $(".item1").show()
        $(".item2").hide()
    })
    /*
     * 滑过图片新闻内容改变
     * */
    $('.pic_show_sec a').mouseenter(function () {
        $(this).children('.pic_show_word').animate({'bottom': '0px'})
    })
    $('.pic_show_sec a').mouseleave(function () {
        $('.pic_show_word').animate({'bottom': '-50px'}, 0)
    })
    /*
     * 滑过图标图片改变
     * */
   /* $('.pic_icon_1').mouseenter(function () {
        $(".pic_icon_1 img")[0].src = "static/image/left.png";
    })
    $('.pic_icon_1').mouseleave(function () {
        $(".pic_icon_1 img")[0].src = "static/image/left_normal.png";
    })
    $('.pic_icon_2').mouseenter(function () {
        $(".pic_icon_2 img")[0].src = "static/image/right-_selected.png";
    })
    $('.pic_icon_2').mouseleave(function () {
        $(".pic_icon_2 img")[0].src = "static/image/right.png";
    })*/
    /*
     * 页面向下滑动式时出发事件
     * */
    $(window).scroll(function () {
        var srollPos = $(window).scrollTop();
        if (srollPos - 10 > 0) {
            $('.header_nav').addClass('bg');
        } else {
            $('.header_nav').removeClass('bg');
        }
    });
    /*
     * job页面的js效果
     * */
    $('.jobs_cont_ul').hide()
    $('.jobs_cont_ul1').show()


    /*
     * 点击置顶事件
     * */
    $(window).scroll(function () {
        var w_height = $(window).height();//浏览器高度
        var scroll_top = $(document).scrollTop();//滚动条到顶部的垂直高度
        if (scroll_top > w_height / 3) {
            $("#goto-top").fadeIn(0);
        } else {
            $("#goto-top").fadeOut(0);
        }
    });
    //置顶
    $("#goto-top").click(function (e) {
        e.preventDefault();
        $(document.documentElement).animate({
            scrollTop: 0
        }, 200);
        //支持chrome
        $(document.body).animate({
            scrollTop: 0
        }, 200);
    });

    /*
     * ie浏览器兼容性问题
     *
     * */
    function isIE() { //ie?
        if (!!window.ActiveXObject || "ActiveXObject" in window)
            return true;
        else
            return false;
    }
    if (isIE()) {
        $('.jobs_cont_ul_div span').css({'top': '-31px'})
        $('.nav_list li a').css({'padding-top': '24px'})
    }
})


