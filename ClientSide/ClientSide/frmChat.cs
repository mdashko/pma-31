using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ClientSide
{
    public partial class frmChat : Form
    {
        TcpClient client;
        NetworkStream ns;
        StreamReader sr;
        StreamWriter sw;
        string username;

        public frmChat()
        {
            InitializeComponent();

            client = new TcpClient("127.0.0.1", 8888);
            ns = client.GetStream();
            sr = new StreamReader(ns);
            sw = new StreamWriter(ns);
            sw.AutoFlush = true;

            username = GetUserName();
            RegisterWithServer();

            //GetMessages();
        }



        private void RegisterWithServer()
        {
            //sw.WriteLine("Registered: " + username);
        }

        private string GetUserName()
        {
            string input = "Imran";//Microsoft.VisualBasic.Interaction.InputBox("Prompt",
            //            "Enter username",
            //            "",
            //            0,
            //            0);

            return input;
        }

        private void btnSend_Click(object sender, EventArgs e)
        {
            string msg = rtbMsg.Text.Trim();
            sw.WriteLine(username + ">> " + msg);
            rtbMsg.Clear();
            GetMessages();
        }

        private void GetMessages()
        {
            string msg = sr.ReadLine();
            //if (!msg.Contains("Registered"))
            //{
            //    rtbAllMsgs.AppendText(msg + "\n");
            //}
            rtbAllMsgs.AppendText(msg + "\n");
        }
    }
}
