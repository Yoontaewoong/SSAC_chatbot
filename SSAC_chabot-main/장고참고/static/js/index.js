var me = {};

var you = {};


function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}            

//-- No use time. It is a javaScript effect.
function insertChat(who, text,time){
    var control = "";
    var date = formatAMPM(new Date());
    
    if (who == "you"){
        control = '<li style="width:100%">' +
                        '<div class="msj macro">' +
                            '<div class="text text-l">' +
                                '<p id="youmsg">'+ text +'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';                    
    }else{
        control = '<li style="width:100%;">' +
                        '<div class="msj-rta macro">' +
                            '<div class="text text-r">' +
                                '<p id="memsg">'+text+'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                  '</li>';
    }
    setTimeout(
        function(){                        
            $("ul").append(control).scrollTop($("ul").prop('scrollHeight'));
        }, time);
    
}

function resetChat(){
    $("ul").empty();
}

// $(".mytext").on("keydown", function(e){
//     if (e.which == 13){
//         var text = $(this).val();
//         if (text !== ""){
//             insertChat("me", text);              
//             $(this).val('');
//         }
//     }
// });

// $('body > div > div > div:nth-child(2) > span').click(function(){
//     $(".mytext").trigger({type: 'keydown', which: 13, keyCode: 13});
// })

//-- Clear Chat
resetChat();

//-- Print Messages
// insertChat("you", '{{response_greeting}}',0);
// insertChat("you", '{{response}}',0);  
// insertChat("you", "Hi, Pablo",1500);
// insertChat("me", "What would you like to talk about today?", 3500);
// insertChat("you", "Tell me a joke",7000);
// insertChat("me", "Spaceman: Computer! Computer! Do we bring battery?!", 9500);
// insertChat("you", "LOL", 12000);


//-- NOTE: No use time on insertChat.

function textToAudio(msg){

    let speech=new SpeechSynthesisUtterance();
    speech.lang="en-US";

    speech.text = msg;
    speech.volume = 2;
    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}