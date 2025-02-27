using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace дфиф2
{
    public partial class Form1: Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
        void MyFunc()
        {
            string s = textBox1.Text.ToString();
            int a = Convert.ToInt32(s);
            int c;
            c = a * 2;
            MessageBox.Show(c.ToString());
        }
        private void button1_Click(object sender, EventArgs e)
        {
            Thread t = new Thread(MyFunc);
            t.Start();
        }
    }
}
