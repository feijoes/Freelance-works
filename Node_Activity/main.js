import ATTRACTIONS from "./attractions.js"
import filter from "./filter.js";
const button = document.getElementById('submit');
const age = document.getElementById('age');
const height =  document.getElementById('height');
const container = document.getElementById('container');

button.onclick = function () {
    let attractions = ATTRACTIONS.filter(function(attraction){
        return filter(attraction, age.value, height.value);
    });
    console.log(attractions)
    attractions.forEach(function(attraction){
        const newElement = document.createElement('div');
        newElement.innerHTML = `\
        <ul>\
            <li>Name: ${attraction.name}</li>\
            <li>Description: ${attraction.Description}</li>\
        <ul>`;
        container.appendChild(newElement);
    });
}