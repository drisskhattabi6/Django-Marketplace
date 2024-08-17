import { countries } from 'countries-list';

window.onload = function() {
    const countrySelect = document.getElementById('countrySelect');
    console.log(countrySelect.target);
    

    Object.keys(countries).forEach((code) => {
        const option = document.createElement('option');
        option.value = countries[code].name;
        option.textContent = countries[code].name;
        countrySelect.appendChild(option);
    });
};