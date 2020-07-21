$(document).ready(function () {
    //首页顶部手机颜色切换
    $(".header_top b").hover( function(){
        $(this).find("img.phone").attr('src',$(this).find("img.phone").attr('src')=='images/phone.png'?'images/phone2.png':'images/phone.png');
    });
    //首页顶部右边下拉效果
    $(".header_top ul li.li_drop").mouseenter(function(){
        $(this).find("ul").show();
    }).mouseleave(function(){
        $(this).find("ul").hide();
    });
    //疗养线路页面向下箭头切换
    $(".route_select li").click(function(){
        if($(this).hasClass("active")){
            $(this).removeClass("active");
        }else{
            $(this).addClass("active");
            $(this).siblings().removeClass("active");
        }
    });
    //疗养线路详情页面，标题点击切换效果
    $(".anchor_title ul li").click( function(){
        $(".anchor_title ul li.active").removeClass("active");
        $(this).addClass("active");
    });
    //疗养线路详情页面，加减效果
    //+-颜色变化
    $(".count").find("button").click(function(){
        $(this).addClass("active");
        var _this =$(this);
        setTimeout(function(){
            _this.removeClass("active");
        },100);
    });
    //减的效果
    $(".book_city  .count").find("button.jian").click(function(){
        var n=$(this).next().text();
        var num=parseInt(n)-1;
        if(num==-1){ return}
        $(this).next().text(num);
    });
    //加的效果
    $(".book_city  .count").find("button.jia").click(function(){
        var n=$(this).prev().text();
        var num=parseInt(n)+1;
        if(num==1000){ return}
        $(this).prev().text(num);
    });
    //支付页面，预付卡选择框效果
    $(".pay_card ul li").find("b").click(function () {
        if($(this).hasClass("active")){
            $(this).removeClass("active");
        }else{
            $(this).addClass("active");
            $(this).parents("li").siblings().find("b").removeClass("active");
        }
    });
    //支付页面，支付平台选择
    $(".payment ul li").find("span").click(function () {
        $(".payment ul li").find("span").removeClass("active");
        $(this).addClass("active");
    });
    //登录注册点击页面切换
    $(".login .login_title ul li").each( function(index){
        var liode = $(this);
        $(this).click( function(){
            $(".login .login_content").removeClass("active");
            $(".login .login_title ul li").removeClass("active");
            $(".login .login_content").eq(index).addClass("active");
            liode.addClass("active");
        });
    });
    //机票页面单返程选择下拉
    $(".plane_way").find("span").click(function(){
        $(this).next().slideToggle();
        $(this).next().find("li").click(function(){
            var m=$(this).text();
            $(this).parent().prev().find("i").text(m);
            $(this).parent().slideUp();
        });
    });
/***************订单页面****************/
    //乘机人选择下拉效果
    $(".passenger_id").find("span").click(function(){
        $(this).next().slideToggle();
        $(this).next().find("li").click(function(){
            var m=$(this).text();
            $(this).parent().prev().find("i").text(m);
            $(this).parent().slideUp();
        });
        $(this).parent().siblings(".passenger_id").find("ul").slideUp();
        $(this).parents(".passenger").siblings(".passenger").find("ul").slideUp();
        $(this).parent().css("z-index","3");
        $(this).parent().siblings(".passenger_id").css("z-index","1");
        $(this).parents(".passenger").css("z-index","2");
        $(this).parents(".passenger").siblings().css("z-index","1");
        $(this).parents(".passenger").siblings().find(".passenger_id").css("z-index","1");
    });
    //联系人电话号码选择下拉效果
    $(".contact_li").find("span").click(function(){
        $(this).next().slideToggle();
        $(this).next().find("li").click(function(){
            var m=$(this).text();
            $(this).parent().prev().find("i").text(m);
            $(this).parent().slideUp();
        });
    });
    //保险选择效果
    $(".order_safe ul li").find("b").click(function () {
        $(".order_safe ul li").find("b").removeClass("active");
        $(this).addClass("active");
    });
    //协议选择效果
    $(".order_submit span").find("b").click(function () {
        if($(this).hasClass("active")){
            $(this).removeClass("active");
        }else{
            $(this).addClass("active");
        }
    });
/***************会员中心页面效果***************/
    //左侧二级导航下拉
    $(".left_nav ul li a").click(function () {
        $(this).parent().addClass("active");
        $(this).parent().siblings().removeClass("active");
        $(this).next("ul").slideToggle();
        $(this).parent().siblings().find("ul").slideUp();
    });
    $(".left_nav ul li ul").find("li").click(function () {
        $(".left_nav ul li ul").find("li>a").removeClass("active");
        $(this).find("a").addClass("active");
        $(this).removeClass("active");
    });
    //个人信息页面男女选择
    $(".personal_info  strong").find("img").click(function () {
        $(".personal_info  strong").removeClass("active");
        $(".personal_info  strong").find("img").attr({"src":"images/circle.png"});
        $(this).parent().addClass("active");
        $(this).attr({"src":"images/circle_after.png"})
    });
    //个人订单页面选择下拉
    $(".order_class .class").find("span").click(function(){
        $(this).next().slideToggle();
        $(this).next().find("li").click(function(){
            var m=$(this).text();
            $(this).parent().prev().find("i").text(m);
            $(this).parent().slideUp();
        });
    });
    //个人订单页面日期段选择
    $(".order_select_time ul li").click(function () {
        $(".order_select_time ul li").removeClass("active");
        $(this).addClass("active");
    });
    //个人订单页面选项卡切换
    $(".order_title ul li").each( function(index){
        var liode = $(this);
        $(this).click( function(){
            $(".personal_order .order_ul").removeClass("active");
            $(".order_title ul li").removeClass("active");
            $(".personal_order .order_ul").eq(index).addClass("active");
            liode.addClass("active");
        });
    });
/*****************酒店列表页面************************/
    $(".filter_li ul li").click(function () {
        // $(this).siblings().removeClass("active");
        if($(this).hasClass("active")){
            $(this).removeClass("active");
            $(this).parents("ul").prev().removeClass("on");
        }else{
            $(this).addClass("active");
            $(this).parents("ul").prev().addClass("on");
        }
    });
    $(".filter_li i").click(function () {
        if($(this).hasClass("on")){
            $(this).removeClass("on");
            $(this).next().find("li").removeClass("active");
        }else{
            $(this).next().find("li").removeClass("active");
        }
    });
    //筛选酒店位置效果
    //一级筛选
    $(".filter_site ul li").each( function(index){
        var liode = $(this);
        $(this).click( function(){
            if($(this).hasClass("active")){
                $(this).removeClass("active");
                $(".site_contain").removeClass("block");
            }else{
                $(".site_contain").removeClass("block");
                $(".filter_site ul li").removeClass("active");
                $(".site_contain").eq(index).addClass("block");
                liode.addClass("active");
            }
        });
    });
    //二级筛选
    $(".site_contain_title ul li").click( function(){
        var index=$(this).index();
        $(this).parents(".site_contain").find(".site_contain_content").removeClass("block");
        $(this).parents(".site_contain").find(".site_contain_title").find("li").removeClass("active");
        $(this).parents(".site_contain").find(".site_contain_content").eq(index).addClass("block");
    });
    //三级选中状态
    $(".site_contain_content ul li").click(function () {
        if($(this).hasClass("active")){
            $(this).removeClass("active");
        }else{
            $(this).addClass("active");
            $(this).siblings().removeClass("active");
        }
    });
    //酒店及入住要求点击效果
    $(".filter_down").click(function () {
        if($(this).hasClass("active")){
            $(this).removeClass("active");
            $(this).find("span").text("酒店类型及入住要求");
            $(".filter .filter_li.none").hide();
        }else{
            $(this).addClass("active");
            $(this).find("span").text("收起更多");
            $(".filter .filter_li.none").show();
        }
    });
    //酒店类型更多弹框开关效果
    $(".filter_more").click(function () {
        $(".filter_li .filter_brand_alert").hide();
        $(".filter_li .brand_close").hide();
        $(".filter_brand_more").removeClass("active");
        if($(this).hasClass("active")){
            $(this).removeClass("active");
            $(".filter_li .filter_alert").hide();
            $(".filter_li .close").hide();
        }else{
            $(this).addClass("active");
            $(".filter_li .filter_alert").show();
            $(".filter_li .close").show();
        }
    });
    $(".filter_li .close").click(function () {
        $(".filter_li .filter_alert").hide();
        $(".filter_li .close").hide();
        $(".filter_more").removeClass("active");
    });
    $(".filter_alert .more_li").click(function () {
        if($(this).hasClass("active")){
            $(this).removeClass("active");
        }else{
            $(this).addClass("active");
        }
    });
    //连锁品牌更多弹框开关效果
    $(".filter_brand_more").click(function () {
        $(".filter_li .filter_alert").hide();
        $(".filter_li .close").hide();
        $(".filter_more").removeClass("active");
        if($(this).hasClass("active")){
            $(this).removeClass("active");
            $(".filter_li .filter_brand_alert").hide();
            $(".filter_li .brand_close").hide();
            $(".filter_down").css("z-index","3");
        }else{
            $(this).addClass("active");
            $(".filter_li .filter_brand_alert").show();
            $(".filter_li .brand_close").show();
            $(".filter_down").css("z-index","1");
        }
    });
    $(".filter_li .brand_close").click(function () {
        $(".filter_li .filter_brand_alert").hide();
        $(".filter_li .brand_close").hide();
        $(".filter_brand_more").removeClass("active");
        $(".filter_down").css("z-index","3");
    });
    $(".filter_brand_alert .brand_li").click(function () {
        if($(this).hasClass("active")){
            $(this).removeClass("active");
        }else{
            $(this).addClass("active");
        }
    });






















});