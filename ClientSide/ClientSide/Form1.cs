using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Sockets;
using System.IO;
using System.Runtime.Serialization.Json;

namespace ClientSide
{
    public partial class Form1 : Form
    {
        TcpClient client = null;
        public Form1()
        {
            InitializeComponent();
            client = new TcpClient("127.0.0.1", 8888);
            NetworkStream ns = client.GetStream();
            StreamReader sr = new StreamReader(ns);

            //txtServerMessage.Text = "Server >> " + sr.ReadLine();

            DataTable dt = ReadToObject(sr.ReadLine());

        }

        // Deserialize a JSON stream to a User object.  
        public static DataTable ReadToObject(string json)
        {
            DataTable dt = new DataTable();
            MemoryStream ms = new MemoryStream(Encoding.UTF8.GetBytes(json));
            DataContractJsonSerializer ser = new DataContractJsonSerializer(dt.GetType());
            dt = ser.ReadObject(ms) as DataTable;
            ms.Close();
            return dt;
        }

        private void btnSend_Click(object sender, EventArgs e)
        {
            if (txtMessage.Text != "")
            {
                NetworkStream ns = client.GetStream();
                StreamWriter sw = new StreamWriter(ns);
                sw.WriteLine(txtMessage.Text);

                sw.Flush();

                sw.Close();
                ns.Close();
            }
        }
    }
}
