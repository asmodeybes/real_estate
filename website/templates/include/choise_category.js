/**
 * Created by student on 21.01.2017.
 */
window.addEventListener('load', function () {
    var cat = document.getElementById("id_category");
    if (cat) {
        cat.onchange = function () {
            console.log(cat.value);
            switch (cat.value) {
                case '1':
                    window.location = '{% url "house_add" %}';
                    break;
                case '2':
                    window.location = '{% url "apartment_add" %}';
                    break;
                case '3':
                    window.location = '{% url "garage_add" %}';
                    break;
                case '4':
                    window.location = '{% url "parcel_add" %}';
                    break;
            }
        };
        switch(window.location.pathname) {
            case '/house_add/':
                cat.value = 1;
                break;
            case '/apartment_add/':
                cat.value = 2;
                break;
            case '/garage_add/':
                cat.value = 3;
                break;
            case '/parcel_add/':
                cat.value = 4;
                break;
        }

    }
    console.log(window.location);

});