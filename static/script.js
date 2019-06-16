
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    if (xmlHttp.status === 200){
        var data = JSON.parse(xmlHttp.responseText);
        return data['real_googlebots'];
    } else {
        console.log(xmlHttp.status);
        return ['Failed'];
    }
}

function wait(ms){
    var start = new Date().getTime();
    var end = start;
    while(end < start + ms) {
      end = new Date().getTime();
   }
 }

function showResults(googlebots, not_googlebots) {
    if (googlebots.length > 0) {
        let returnData = googlebots.join('<br>');
        document.getElementById('results').innerHTML = returnData;
    } else {
        let returnData = 'No Googlebot IP addresses found.';
        document.getElementById('results').innerHTML = returnData;
    }
    document.getElementById('loading-spinner').style.display = 'none';
    document.getElementById('results-area').style.display = 'block';

    if (not_googlebots.length > 0) {
        document.getElementById('not-googlebots').innerHTML = not_googlebots.join('<br>');
        document.getElementById('fake-bots').style.display = 'block';
    }
}

function confirm_ips(ip_list){
    googlebots = [];
    not_googlebots = [];
    for (i = 0; i<ip_list.length; ++i) {
        ip = JSON.stringify(ip_list[i]);
        ip = ip.replace(/"/g, "");
        ip = ip.replace(/\./g, "_")
        let api_url = `/confirm_googlebot/${ip}`;
        var bot = httpGet(api_url);
        if (ip_list[i] === bot[0]) {
            googlebots.push(bot[0]);
        } else {
            not_googlebots.push(ip_list[i]);
        }
    
    setTimeout(function() {showResults(googlebots, not_googlebots);}, 0);

    }
}
function run() {
    gtag('event', 'run', {
    'event_category': 'Submissions',
    'event_label': 'Confirm Googlebot'
    });
    let ip_list = '';
    let ip_count = 0;
    let data = {};
    ip_list = document.getElementById('ip-input').value;
    ip_list = ip_list.split('\n');
    if (ip_list[0].length < 1){
        document.getElementById('qa-button').style.display = 'none';
        document.getElementById('error-message').style.display = 'block';
    } else {
        showLoader();
    setTimeout(function() {confirm_ips(ip_list);}, 0);
    }
}

function showLoader(){
    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById("input-area").style.display = 'none';
    
}