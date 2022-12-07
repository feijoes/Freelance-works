using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GUI
{
    public partial class Form1 : Form
    {

        String mes;
        String dia;
        String ano;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime date = DateTime.Parse(dia + "/" + mes + "/" +ano);
            TimeSpan myAge = DateTime.Now.Subtract(date);
            MessageBox.Show("You are " + ((int)myAge.TotalDays) + " days old!");
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            this.dia= textBox2.Text;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            this.ano = textBox1.Text;
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            this.mes = textBox3.Text;
        }
    }
}
