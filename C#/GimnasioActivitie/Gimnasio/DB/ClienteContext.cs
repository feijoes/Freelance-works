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

    
  }
}