
const Lugar = (titulo,content,image,num) => {
    if (num == 1) {return `<div class="row">
    <div class="col padding">
        <h2>${titulo}</h2>
        <p>${content}</p>
    </div>
    <img class="image" src="src/images/${image}"></img>
    </div>`}
    return `<div class="row">
    <img class="image" src="src/images/${image}"></img>
    <div class="col padding">
        <h2>${titulo}</h2>
        <p>${content}</p>
    </div>
    </div>`
    
}
export default Lugar