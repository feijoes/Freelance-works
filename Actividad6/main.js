
const Center = () => {
    return `<div><button onclick="center()">Main</button><div id="Center" class='container main'>
                    ${Lugar("Roque Nublo, lugar de culto",
                    `Es la roca volcánica más identificable de Gran Canaria.
                    Con sus 80 metros de alto, esta mole se eleva a 1.813 metros sobre el nivel del mar.
                    Su origen se debe a una de las erupciones volcánicas que forjaron el archipiélago hace millones de años.
                    Lo más curioso del Roque Nublo es su vinculación con un lugar sagrado, un espacio de culto de los antiguos aborígenes.
                    Este es uno de los sitios que hay que visitar sí o sí en la isla.`,
                    "monte.jpg",1)}
                    ${Lugar("Dunas de Maspalomas, el pequeño desierto",
                    `Si no tienes una foto en las Dunas de Maspalomas, no has ido a Gran Canaria. 
                    Este desierto de Sahara en miniatura es uno de los paisajes más impactantes que tienes que visitar en la isla.
                    Recorre sus dunas, disfruta de las panorámicas y termina dándote un baño en las azules aguas del Atlántico.`,
                    "dunas.jpg",2)}      
                </div>`
};
const Lugar = (titulo,content,image,num) => {
  if (num == 1) {return `<div class="row">
  <div class="col padding">
      <h2>${titulo}</h2>
      <p>${content}</p>
  </div>
  <img class="image" src="images/${image}"></img>
  </div>`}
  return `<div class="row">
  <img class="image" src="images/${image}"></img>
  <div class="col padding">
      <h2>${titulo}</h2>
      <p>${content}</p>
  </div>
  </div>`
  
}
const Footer = () => {
    return `<div><button onclick="footer()">Footer</button>
    <footer id="Footer">
    <div class="container">
      <div class="row color">
        <div class="col-md-4 footer-col">
          <h3>Contacto</h3>
          <p>
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-person-fill" fill="currentColor"
              xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
            </svg>
            Aránzazu Afonso Santana
          </p>
          <p>
            <span>
              <i class="fa fa-phone">
              </i>
              Telefono
            </span>
            928 55 44 44
          </p>
          <p>
            <span>
              <i class="fa fa-envelope">
              </i>
              Email
            </span>
            <a href="">Yo@gmail.com</a>
          </p>
        </div>
        <div class="col-md-4 footer-col">
          <h3>Mis redes</h3>
          <ul class="list-inline">
            <li>
              <a target="_blank" href="https://www.facebook.com/" class="btn-social btn-outline"><i
                  class="fa fa-fw fa-facebook"></i></a>
            </li>
            <li>
              <a target="_blank" href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-google-plus"></i></a>
            </li>
            <li>
              <a target="_blank" href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-twitter"></i></a>
            </li>
            <li>
              <a target="_blank" href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-linkedin"></i></a>
            </li>

          </ul>
        </div>
        <div class="col-md-4 footer-col">
          <h3>Curso</h3>
          <p>I.E.S. El Rincon 2º DAW </p>
        </div>
      </div>
    </div>
  </footer></div>`;
}


const Header = () => {
  return `<div><button onclick="header()">Header</button>
  <div id="Header"><div id="cabecera">
  <h1>Lugares para visitar en Gran Canaria</h1>
  <div id="logo">

  <img src="images/gran-canaria-logo.png">
  </div>

</div>
<!-- barra de navegacion -->

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active ">
        <a class="nav-link" href="#">Início</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#">Contacto</a>
      </li>
      
      </li>
    </ul>
</nav></div>`;
}
document.querySelector('#app').insertAdjacentHTML("beforebegin",  `${Header()}${Center()}${Footer()}`
);
function footer() {
  var x = document.getElementById("Footer");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}function header() {
  var x = document.getElementById("Header");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}function center() {
  var x = document.getElementById("Center");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}