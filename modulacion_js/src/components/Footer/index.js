
const Footer = () => {
    return `<footer class="">
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
            TU NOMBRE
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
  </footer>`;
}
export default Footer