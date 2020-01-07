function modal() {
    $("#modal-trigger").animatedModal({
        modalTarget:'js-modal',
        animatedIn:'lightSpeedIn',
        animatedOut:'bounceOutDown',
        color:'#3498db',
        // Callbacks
        beforeOpen: function() {
            console.log("The animation was called");
        },
        afterOpen: function() {
            console.log("The animation is completed");
        },
        beforeClose: function() {
            console.log("The animation was called");
        },
        afterClose: function() {
            console.log("The animation is completed");
        }
    });
}

$(".like-btn").click(function(e){
    e.preventDefault();
    var this_ = $(this);
    var likeUrl = this_.attr("data-href");
    var likeCount = parseInt(this_.attr("data-likes")) | 0;
    var addLike = likeCount + 1; 
    var removeLike = likeCount - 1;
    $.ajax({
        url: likeUrl,
        method: "get",
        data: {},
        success: function(data){
            console.log(data);
            var NewLikes;
            if (data.liked){
                $(".likes_count").text(addLike + " likes");
                // add one like 
            } else {
                $(".likes_count").text(removeLike + " likes");
                // remove one like 
            }
        }, error: function(error){
            console.log(error);
            console.log("error");
        }
    });
});

$(".follow_button").click(function(e){
    e.preventDefault(); 
    var thiss_ = $(this);
    var follow_url = thiss_.attr("follow-href");
    var follow_count = parseInt(thiss_.attr("data-follow")) | 0;
    var addfollow = follow_count + 1;
    var removefollow = follow_count - 1;
    if (follow_url){
        $.ajax({
            url: follow_url,
            method: "get",
            data: {},
            success: function(data){
                console.log(data);
                if (data.follow){
                    $(".number_of_followers").text(addfollow);
                    $(".follow_button").text("Following");
                } else {
                    $(".number_of_followers").text(removefollow);
                    $(".follow_button").text("Follow");
                }

            }, error: function(error){
            console.log(error);
            console.log("error");}

        });
    }

});