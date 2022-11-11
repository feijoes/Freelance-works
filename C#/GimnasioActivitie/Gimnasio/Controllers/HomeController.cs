using Gimnasio.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using Gimnasio.DB;
namespace Gimnasio.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index() => View();

    [HttpPost]
    public ActionResult Index(string Nombre,string contasena,int nPersonas)
    {
        Console.WriteLine(Nombre);
        Console.WriteLine(nPersonas);
        ClienteContext context = HttpContext.RequestServices.GetService(typeof(Gimnasio.DB.ClienteContext)) as ClienteContext;
        if (!String.IsNullOrEmpty(Nombre))
        {
            context.CrearUsuario(Nombre,contasena,nPersonas);
        }
        string mystring = "";
        if (nPersonas.Equals(1))
        {
            mystring = "50%";
        }
        if (nPersonas.Equals(2))
        {
            mystring = "75%";
        }
        if (nPersonas.Equals(3))
        {
            mystring = "100%";
        }
        return View((object)mystring);

    }   

        public IActionResult Privacy() => View();

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}