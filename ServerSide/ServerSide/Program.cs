//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Net.Sockets;
//using System.Text;
//using System.Threading.Tasks;
//using System.IO;
//using System.Data;
//using System.Data.SqlClient;
//using System.Runtime.Serialization.Json;
//using DAL.Entities;
//using DAL.Operations;

//namespace ServerSide
//{
//    class Program
//    {
//        static void Main(string[] args)
//        {
//            try
//            {
//                TcpListener server = new TcpListener(8888);
//                server.Start();
//                Console.WriteLine("Server Started and waiting for clients.");
//                Socket socketForClients = server.AcceptSocket();

//                if (socketForClients.Connected)
//                {
//                    string opt = "";
//                    EEmployee emp = new EEmployee();
//                    OEmployee empOps = new OEmployee();
//                    NetworkStream ns = new NetworkStream(socketForClients);
//                    StreamWriter sw = new StreamWriter(ns);
//                    StreamReader sr = new StreamReader(ns);
//                    sw.AutoFlush = true;
//                    Console.WriteLine("Server>> Welcome Client.");
//                    string str = SerializeObject();
//                    sw.WriteLine(str);

//                    while (true)
//                    {
//                        // send message to client
//                        string json = sr.ReadLine();
//                        if (json != null)
//                        {
//                            emp = DeserializeObject(json);
//                            opt = emp.opt;
//                        }

//                        switch (opt)
//                        {
//                            case "1":
//                                str = SerializeObject();
//                                sw.WriteLine(str);
//                                break;
//                            case "2":
//                                empOps.Insert(emp);
//                                break;
//                        }


//                        if (opt == null)
//                            break;
//                    }

//                    sr.Close();
//                    if (sw != null)
//                    {
//                        sw.Close();
//                    }
//                    ns.Close();
//                }

//                socketForClients.Close();
//            }
//            catch (Exception ex)
//            {
//            }
//        }

//        private static string SerializeObject()
//        {
//            OEmployee empOps = new OEmployee();
//            //Create a stream to serialize the object to.  
//            MemoryStream ms = new MemoryStream();
//            // Serializer the User object to the stream.  
//            DataContractJsonSerializer ser = new DataContractJsonSerializer(typeof(DataTable));
//            DataTable dt = empOps.SelectAll();
//            dt.TableName = "Employee";
//            ser.WriteObject(ms, dt);
//            byte[] json = ms.ToArray();
//            ms.Close();
//            return Encoding.UTF8.GetString(json, 0, json.Length);
//        }

//        private static EEmployee DeserializeObject(string json)
//        {
//            EEmployee emp = new EEmployee();

//            if (json != null)
//            {
//                MemoryStream ms = new MemoryStream(Encoding.UTF8.GetBytes(json));
//                DataContractJsonSerializer ser = new DataContractJsonSerializer(emp.GetType());

//                emp = ser.ReadObject(ms) as EEmployee;
//            }
//            return emp;
//        }

//        //private static DataTable GetAll()
//        //{
//        //    SqlConnection conn = new SqlConnection(@"Data Source=LAPTOP-DBVPT6QU\SQLEXPRESS;Initial Catalog=EmployeeDb;Integrated Security=True");
//        //    string query = "Select * from Employee";
//        //    SqlDataAdapter da = new SqlDataAdapter(query, conn);
//        //    DataTable dt = new DataTable();
//        //    da.Fill(dt);

//        //    return dt;
//        //}
//    }
//}
