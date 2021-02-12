function openTab(evt, details) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(details).style.display = "block";
    evt.currentTarget.className += " active";
	}

var isLockedBy = "{{ locked }}"
if (isLockedBy != ""){
    document.getElementById("saveFormButton").disabled = true;
    document.getElementById("saveFormButton").style.color = "grey";
    var bar = document.getElementById("lockedInfo");
    bar.style.display = "block";
}

document.getElementById("Form2").style.display = "block"

function popup() {
    var w = window.open('','','width=auto,height=auto')
    w.document.write(`<!doctype html>
    <html lang="en-gb" dir="ltr" class="no-js">
    ​   
    <head>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title></title>
        <link rel="stylesheet" href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/css/main.css">
        <meta name="msapplication-config"
            content="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/browserconfig.json">
        <link rel="icon" type="image/x-icon" href="https://cdn.ons.gov.uk/sdc/design-system/24.0.1/favicons/favicon.ico">
        <link rel="icon" type="image/png"
            href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/favicon-32x32.png" sizes="32x32">
        <link rel="icon" type="image/png"
            href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/favicon-16x16.png" sizes="16x16">
        <link rel="mask-icon" color="#5BBAD5"
            href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/safari-pinned-tab.svg">
        <link rel="apple-touch-icon" type="image/png"
            href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/apple-touch-icon.png" sizes="180x180">
        <link rel="manifest" href="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/favicons/manifest.json">
        <link rel="stylesheet" href="https://cdn.ons.gov.uk/sdc/design-system/16.1.0/css/main.css" media="all"
            type="text/css">
        <link rel="stylesheet" href="{{ url_for('static',filename='css/custom.css') }}" media="all" type="text/css">
        <script>var ONS_assets_base_URL='https://cdn.ons.gov.uk/sdc/design-system/24.0.3/';</script>
        <script src="https://cdn.ons.gov.uk/sdc/design-system/24.0.3/scripts/main.js"></script>
        <script type="text/javascript"
                src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
        <script type="text/javascript" src="{{ url_for('static', filename='js/industry-range.js') }}"></script>

    </head>

    <body>
    <div class="mainContent"> 
    <div class="phase-banner mainContent">
        <div class="grid grid--flex grid--gutterless grid--vertical-center grid--no-wrap">
            <div class="grid__col col-auto u-flex-no-grow">
                <h3 class="phase-banner__badge">BETA</h3>
            </div>
            <div class="grid__col col-auto u-flex-shrink">
                <p class="phase-banner__desc u-fs-s u-mb-no">This is a work in progress</p>
            </div>
        </div>
    </div>

    <header class="header header--internal header--thin">
        <div class="header__top mainContent" role="banner">
            <div class="header__grid-top grid grid--gutterless grid--flex grid--between grid--vertical-center grid--no-wrap">
                <div class="grid__col col-auto">
                </div>
            </div>
        </div>
        <div class="header__main">
            <div class="grid grid--gutterless grid--flex grid--between grid--vertical-center grid--no-wrap mainContent">
                <div class="grid__col col-auto u-flex-shrink">
                    <div class="header__title">
                        Data Clearing
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    <br>
    <br>
    <body> 
        <h2>Loading, please wait</h2>
    </body>
    <br>
    <br>
    <br>


    <footer class="footer " data-ga-element="footer">
        <div class="container">
            <div class="grid">
                <div class="grid__col col-4@m">
                    <!-- Footer text here -->
                </div>
                <div class="grid__col u-mt-m u-mb-m">
                    <hr class="footer__hr">
                </div>
                <div class="grid__col">
                    <div class="footer__license">
                        <img alt="OGL" class="footer__ogl-img"
                            src="{{ url_for('static',filename='img/UKOpenGovernmentLicence-grey.svg') }}">
                        All content is available under the <a
                            href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
                            class="footer__link">Open Government Licence v3.0</a>, except where otherwise stated
                    </div>
                </div>
            </div>
        </div>
    </footer>
    </div>
    </body>

    </html>`)

    w.focus()
    setTimeout(function() {w.close();}, 5000)
    }