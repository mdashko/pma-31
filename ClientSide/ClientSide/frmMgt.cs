using DAL.Entities;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net.Sockets;
using System.Runtime.Serialization.Json;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ClientSide
{
    public partial class frmMgt : Form
    {
        TcpClient client = null;
        NetworkStream ns = null;
        StreamReader sr;// = new StreamReader(ns);
        StreamWriter sw;// = new StreamWriter(ns);
        public frmMgt()
        {
            InitializeComponent();
            
            client = new TcpClient("127.0.0.1", 8888);
            ns = client.GetStream();
            sr = new StreamReader(ns);
            sw = new StreamWriter(ns);
            sw.AutoFlush = true;

            //txtServerMessage.Text = "Server >> " + sr.ReadLine();

            DataTable dt = DeserializeJson(sr.ReadLine());
            dataGridView1.DataSource = dt;
        }

        private DataTable DeserializeJson(string json)
        {
            DataTable dt = new DataTable();
            MemoryStream ms = new MemoryStream(Encoding.UTF8.GetBytes(json));
            DataContractJsonSerializer ser = new DataContractJsonSerializer(dt.GetType());
            dt = ser.ReadObject(ms) as DataTable;

            return dt;
        }

        private string SerializeObject(EEmployee emp)
        {
            MemoryStream ms = new MemoryStream();

            DataContractJsonSerializer ser = new DataContractJsonSerializer(typeof(EEmployee));

            ser.WriteObject(ms, emp);

            byte[] json = ms.ToArray();

            return Encoding.UTF8.GetString(json, 0, json.Length);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            EEmployee emp = new EEmployee();

            emp.Name = txtName.Text;
            emp.Email = txtEmail.Text;
            emp.opt = "2";

            string str = SerializeObject(emp);
            sw.WriteLine(str);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            NetworkStream ns = client.GetStream();
            EEmployee emp = new EEmployee();
            emp.opt = "1";
            sw.WriteLine(SerializeObject(emp));

            ns = client.GetStream();
            DataTable dt = DeserializeJson(sr.ReadLine());
            dataGridView1.DataSource = dt;
        }
    }
}
