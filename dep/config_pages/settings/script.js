// General
var theme = document.getElementById('themes');

// Blocking
const Blocking_ad_blocker = document.getElementById("ad_blocker");
const Blocking_privacy_blocker = document.getElementById("privacy_blocker");
const Blocking_cookie_blocker = document.getElementById("cookie_blocker");
const Blocking_youtube_ad_blocker = document.getElementById("youtube_ad_blocker");

// User-Agent
const defaultUserAgent = document.getElementById("default_user_agent");
const randomUserAgent = document.getElementById("random_user_agent");
const customUserAgent = document.getElementById("custom_user_agent");
const customUserAgentInput = document.getElementById("custom_user_agent_input");

// Privacy
const routeThroughTor = document.getElementById("routetrafficthroughtor");
const torSearchEngineBypass = document.getElementById("torsearchenginebypass");
const trackingLinkProtection = document.getElementById("trackinglinkprotection");

// Proxy
const offProxy = document.getElementById("offproxy");
const customProxy = document.getElementById("customproxy");
const customProxyAddressInput = document.getElementById("custom_proxy_address_input");
const customProxyPortInput = document.getElementById("custom_proxy_port_input");


// loading
const loaderContainer = document.querySelector('.loader-container');
window.addEventListener('load', () => {
    setTimeout(() => {
        loaderContainer.style.display = 'none';
    }, 200);
});


// proxy gray out box
const contentDiv = document.getElementById('proxy-content');
// Create the overlay div
const overlay = document.createElement('div');
overlay.className = 'proxy-overlay';
contentDiv.appendChild(overlay);


// gray out proxy when tor is active
document.addEventListener('DOMContentLoaded', function() {
    // Event listener for the checkbox
    routeThroughTor.addEventListener('change', function() {
        if (routeThroughTor.checked) {
            overlay.style.display = 'block';
        } else {
            overlay.style.display = 'none';
        }
    });
});


// Load settings from localStorage
window.onload = (event) => {
    var storedTheme = localStorage.getItem('theme_name');
    if (storedTheme === null) {
        // If not found, default to "Dark"
        theme.value = "Dark";
    } else {
        // Parse the stored theme name (if necessary, in case it was stringified)
        storedTheme = JSON.parse(storedTheme);
    
        // Loop through each option in the select element
        for (var i = 0; i < theme.options.length; i++) {
            var option = theme.options[i];
            // Check if the current option's value matches the stored theme
            if (option.value === storedTheme) {
                option.selected = true;
                break;
            }
        }
    }

    // Blocking
    Blocking_ad_blocker.checked = JSON.parse(localStorage.getItem('ad_blocker'));
    Blocking_privacy_blocker.checked = JSON.parse(localStorage.getItem('privacy_blocker'));
    Blocking_cookie_blocker.checked = JSON.parse(localStorage.getItem('cookie_blocker'));
    Blocking_youtube_ad_blocker.checked = JSON.parse(localStorage.getItem('youtube_ad_blocker'));

    // User-Agent
    const userAgentOption = JSON.parse(localStorage.getItem('userAgentOption'));
    if (userAgentOption === 'default') {
        defaultUserAgent.checked = true;
    } else if (userAgentOption === 'random') {
        randomUserAgent.checked = true;
    } else if (userAgentOption === 'custom') {
        customUserAgent.checked = true;
    }
    customUserAgentInput.value = JSON.parse(localStorage.getItem('custom_userAgent'));

    // Privacy
    routeThroughTor.checked = JSON.parse(localStorage.getItem('routeThroughTor'));
    torSearchEngineBypass.checked = JSON.parse(localStorage.getItem('torSearchEngineBypass'));
    trackingLinkProtection.checked = JSON.parse(localStorage.getItem('trackingLinkProtection'));

    // Proxy
    const proxyOption = JSON.parse(localStorage.getItem('proxyOption'));
    if (proxyOption === 'off') {
        offProxy.checked = true;
    } else if (proxyOption === 'custom') {
        customProxy.checked = true;
    }
    customProxyAddressInput.value = JSON.parse(localStorage.getItem('customProxyAddress'));
    customProxyPortInput.value = JSON.parse(localStorage.getItem('customProxyPort'));

    // show proxy options or not
    if (routeThroughTor.checked) {
        overlay.style.display = 'block';
    } else {
        overlay.style.display = 'none';
    }
};



// Save settings to localStorage
document.getElementById("save_btn").addEventListener('click', () => {
    // General
    localStorage.setItem('javascript', JSON.stringify(true));
    localStorage.setItem('theme_name', JSON.stringify(theme.value));

    // Blocking
    localStorage.setItem('ad_blocker', JSON.stringify(Blocking_ad_blocker.checked));
    localStorage.setItem('privacy_blocker', JSON.stringify(Blocking_privacy_blocker.checked));
    localStorage.setItem('cookie_blocker', JSON.stringify(Blocking_cookie_blocker.checked));
    localStorage.setItem('youtube_ad_blocker', JSON.stringify(Blocking_youtube_ad_blocker.checked));

    // User-Agent
    if (defaultUserAgent.checked) {
        localStorage.setItem('userAgentOption', JSON.stringify('default'));
    } else if (randomUserAgent.checked) {
        localStorage.setItem('userAgentOption', JSON.stringify('random'));
    } else if (customUserAgent.checked) {
        localStorage.setItem('userAgentOption', JSON.stringify('custom'));
    }
    localStorage.setItem('custom_userAgent', JSON.stringify(customUserAgentInput.value));

    // Privacy
    localStorage.setItem('routeThroughTor', JSON.stringify(routeThroughTor.checked));
    localStorage.setItem('torSearchEngineBypass', JSON.stringify(torSearchEngineBypass.checked));
    localStorage.setItem('trackingLinkProtection', JSON.stringify(trackingLinkProtection.checked));

    // Proxy
    if (offProxy.checked) {
        localStorage.setItem('proxyOption', JSON.stringify('off'));
    } else if (customProxy.checked) {
        localStorage.setItem('proxyOption', JSON.stringify('custom'));
    }
    localStorage.setItem('customProxyAddress', JSON.stringify(customProxyAddressInput.value));
    localStorage.setItem('customProxyPort', JSON.stringify(customProxyPortInput.value));

    alert("settings changed!");
});
