$('.player-bottom-hand .playing-card').click(function() {
	$(this).toggleClass('selected');
});

$('.player-bottom-hand .playing-card-image').click(function() {
	$(this).toggleClass('selected');
});

$('.clear-selection').click(function() {
	$('.selected').removeClass('selected');
});