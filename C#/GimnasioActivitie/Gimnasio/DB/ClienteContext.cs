using System.Runtime.InteropServices;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Extensions.DependencyInjection;
using Gimnasio.Models;
namespace Gimnasio.DB
{
  public class ClienteContext
  {
    public string ConnectionString { get; set; }

    public ClienteContext(string connectionString)
    {
      this.ConnectionString = connectionString;
    }

    private MySqlConnection GetConnection()
    {
      return new MySqlConnection(ConnectionString);
    }

    public void CrearUsuario(string Nombre,string contrasena, int nPersonas)
    {

      using (MySqlConnection conn = GetConnection())
      {
        conn.Open();
        MySqlCommand cmd = new MySqlCommand();
        cmd.Connection = conn;
        cmd.CommandText = "INSERT INTO clientes(Nombre,nPersonas,contrasena) VALUES(?Nombre,?nPersonas,?contrasena)";
        cmd.Parameters.Add("?Nombre", MySqlDbType.VarChar).Value = Nombre;
        cmd.Parameters.Add("?nPersonas", MySqlDbType.Int32).Value = nPersonas;
        cmd.Parameters.Add("?contrasena", MySqlDbType.VarChar).Value = contrasena;
        cmd.ExecuteNonQuery();
      }
    }
  }
}