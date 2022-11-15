using Business_Layer;
using Entity_Layer;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Facturas.Controllers
{
    public class PagoController : Controller
    {
        // GET: Pago
    [HttpPost]
        public ActionResult Insert(PagoBO dto)
        {
            NegPago obj = new NegPago();
            obj.Insert(dto);
            return RedirectToAction("Listar");

        }
        [HttpPost]
        public ActionResult InsertP(DetalleBO dto)
        {
            NegDetalle obj = new NegDetalle();
            obj.Insertar(dto);
            return RedirectToAction("Listar");

        }
        public ActionResult Update(PagoBO dto)
        {
            return View(); NegPago obj = new NegPago();
            obj.Actualizar(dto);
            return RedirectToAction("Listar");
        }
        [HttpGet]
        public ActionResult Delete(int NUM_PAGO)
        {

            NegPago obj = new NegPago();
            obj.Eliminar(NUM_PAGO);
            return RedirectToAction("Listar");
        }
        public ActionResult Listar()
        {
            NegPago obj = new NegPago();
            return View(obj.Listar());
        }
        public ActionResult Listar2()
        {
            NegFactura obj = new NegFactura();
            return View(obj.Listar());
        }
        public ActionResult Listar3()
        {
            NegDetalle obj = new NegDetalle();
            return View(obj.Listar());
        }
        [HttpGet]
        public ActionResult EditarPago(int NUM_PAGO)
        {
            NegPago obj = new NegPago();
            PagoBO dto = obj.Listar().FirstOrDefault(a=> a.NUM_PAGO == NUM_PAGO);
            return View("Update",dto);
        }
        public ActionResult Insert()
        {
            return RedirectToAction("Insert", new PagoBO());
        }
        public ActionResult InsertP()
        {
            return RedirectToAction("InsertP", new DetalleBO());

        }
        public ActionResult Pedidos()
        {

            return RedirectToAction("PedidoInsertar");

        }
    }
}