$(document).ready(function () {
    $('.like_form').submit(function (e) {
        e.preventDefault()

        const post_id = $(this).attr('id')

        const likeText = $(`.like-btn${post_id}`).text()
        const trim = $.trim(likeText)

        const url = $(this).attr('action')

        let res;
        const likes = $(`.like-count${post_id}`).text()
        const trimCount = parseInt(likes)

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id,
            },
            success: function (response) {
                if (trim === 'Unlike') {
                    $(`.like-btn${post_id}`).text('Like').removeClass('"btn btn-danger like-btn{{ item.id }}').addClass('btn btn-success like-btn{{ item.id }}');
                    res = trimCount - 1
                } else {
                    $(`.like-btn${post_id}`).text('Unlike').removeClass('"btn btn-success like-btn{{ item.id }}').addClass('btn btn-danger like-btn{{ item.id }}');
                    res = trimCount + 1
                }
                $(`.like-count${post_id}`).text(res)
            },
            error: function (response) {
                console.log('error', response)
            }
        })
    })
});