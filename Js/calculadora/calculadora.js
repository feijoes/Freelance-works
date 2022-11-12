class Window {
    constructor(options = {}) {
        this.width = options.width || 200;
        this.height = options.height || 200;
        this.posX = options.posX || 200;
        this.posY = options.posY || 1100;

        this.el = document.createElement('div');
        this.el.style.width = this.width + 'px';
        this.el.style.height = this.height + 'px';
        this.el.style.top = this.posX + 'px';
        this.el.style.left = this.posY + 'px';
        this.el.style.position = 'absolute';
        document.body.appendChild(this.el);
    }
    setTitle(title) {
        this.el.innerText = title;
    }
   setContent(ele,elementos){
     var elemento = document.createElement(ele);
     elemento.innerHTML = elementos
     this.el.appendChild(elemento);
     return elemento;
   }
}

class Calculator extends Window {
    constructor(options = {}) {
        super();
        var elementos = '<div class="container">\
       <div id="display"></div>\
            <div class="buttons">\
                <div class="button">C</div>\
                <div class="button">/</div>\
                <div class="button">*</div>\
                <div class="button">&larr;</div>\
                <div class="button">7</div>\
                <div class="button">8</div>\
                <div class="button">9</div>\
                <div class="button">-</div>\
                <div class="button">4</div>\
                <div class="button">5</div>\
                <div class="button">6</div>\
                <div class="button">+</div>\
                <div class="button">1</div>\
                <div class="button">2</div>\
                <div class="button">3</div>\
                <div class="button">.</div>\
                <div class="button">(</div>\
                <div class="button">0</div>\
                <div class="button">)</div>\
                <div id="equal" class="button">=</div>\
            </div></div>';
      console.log(12)
       const contenido = this.setContent("section",elementos);
       
        let display = document.getElementById('display');

let buttons = Array.from(document.getElementsByClassName('button'));

buttons.map( button => {
    button.addEventListener('click', (e) => {
        switch(e.target.innerText){
            case 'C':
                display.innerText = '';
                break;
            case '=':
                try{
                    display.innerText = eval(display.innerText);
                } catch {
                    display.innerText = "Error"
                }
                break;
            case '←':
                if (display.innerText){
                   display.innerText = display.innerText.slice(0, -1);
                }
                break;
            default:
                display.innerText += e.target.innerText;
        }
    });
});}}

var c = new Calculator();