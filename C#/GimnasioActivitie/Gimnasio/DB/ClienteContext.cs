using System;
using System.Data;
using Oracle.ManagedDataAccess.Client;

namespace Gimnasio.DB
{
    class ClienteContext
    {

        public static string user = "<DEMODOTNET>";
        public static string pwd = "<PASSWORD>";

        public static string db = "localhost/XEPDB1";

        public void CrearUsuario(String Nombre,String password, int nPersonas)
        {
            string conStringUser = "User Id=" + user + ";Password=" + pwd + ";Data Source=" + db + ";";

            using (OracleConnection con = new OracleConnection(conStringUser))
            {
                using (OracleCommand cmd = con.CreateCommand())
                {
                    try
                    {
                        con.Open();
                        Console.WriteLine("Successfully connected to Oracle Database as " + user);
                        Console.WriteLine();

                        //Create the sample table. Checks if table already exists

                        cmd.CommandText = "IINSERT INTO clientes(Nombre,nPersonas,contrasena) VALUES(:Nombre,:nPersonas,:contrasena)";
                        

                        OracleParameter Nombreparam = new OracleParameter("Nombre", OracleDbType.Varchar2);
                        Nombreparam.Direction = ParameterDirection.Input;
                        Nombreparam.Value = Nombre;
                        cmd.Parameters.Add(Nombreparam);

                        OracleParameter nPersonasparam = new OracleParameter("nPersonas", OracleDbType.Int16);
                        nPersonasparam.Direction = ParameterDirection.Input;
                        nPersonasparam.Value = nPersonas;
                        cmd.Parameters.Add(nPersonasparam);

                        OracleParameter contrasenaparam = new OracleParameter("contrasena", OracleDbType.Varchar2);
                        contrasenaparam.Direction = ParameterDirection.Input;
                        contrasenaparam.Value = Nombre;
                        cmd.Parameters.Add(contrasenaparam);

                        

                        cmd.ExecuteNonQuery();
                    

                        //Retrieve sample data

                        Nombreparam.Dispose();
                        nPersonasparam.Dispose();
                        contrasenaparam.Dispose();
                       
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex.Message);
                    }
                }
            }
        }
    }
}