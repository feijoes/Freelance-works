using Microsoft.AspNetCore.Mvc;
using System;
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
        public ActionResult Index(string NIT)
        {
            string mystring = "";
            int total = 0;
            int multiplicacion = 2;
            char[] charArray = NIT.ToCharArray();
            
            for (int i = charArray.Length - 1; i > -1; i--)
            {
                total += charArray[i] * multiplicacion;
                multiplicacion++;
            }
            int valor = total % 11;
            valor -= 11 ;
            Console.WriteLine(valor);
            if (valor == 11 || valor ==10)
            {
                mystring = "NIT es valido";
            }
            else
            {
                mystring = "NIT no es valido";
            }

                return View((object)mystring);
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