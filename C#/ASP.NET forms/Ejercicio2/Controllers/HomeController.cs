using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }
        [HttpPost]
        public ActionResult Index(string NombreFormulario,string Key, string Label, bool Requerido, string Orden, string ControlType, string Type)
        {
            Console.WriteLine(NombreFormulario);
            Console.WriteLine(Key);
            Console.WriteLine(Label);
            Console.WriteLine(Requerido);
            Console.WriteLine(Orden);
            Console.WriteLine(ControlType);
            Console.WriteLine(Type);
            return View(new List<string>() {"Nombre del formulario: "+ NombreFormulario,"Key: "+Key,"Label: "+ Label, "Requerido: "+Requerido.ToString(),"Orden: "+ Orden, "Control Type: "+ControlType, "Type: "+ Type });
        }
        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}