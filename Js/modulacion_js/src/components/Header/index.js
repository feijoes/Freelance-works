

const Header = () => {
    return `<div id="cabezera">
    <h1>Lugares para visitar en Gran Canaria</h1>
    <div id="logo">

    <img src="src/images/gran-canaria-logo.png">
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
  </nav>`;
}
export default Header