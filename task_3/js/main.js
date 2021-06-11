
function checkParams() {
    var card1 = $('#card_1').val();
    var card2 = $('#card_2').val();
    var card3 = $('#card_3').val();
    var card4 = $('#card_4').val();

    if(card1.length >= 4 && card1.match(/\D/) == null && card2.length >= 4 && card2.match(/\D/) == null && card3.length
    >= 4 && card3.match(/\D/) == null && card4.length >= 4 && card4.match(/\D/) == null) {
        $('#submit').removeAttr('disabled');
    } else {
        $('#submit').attr('disabled');
    }
}
