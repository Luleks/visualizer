using Settings;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ArraySettings
{
	public partial class FormArraySettings : Form
	{
		private Settings.ArraySettings array_settings = null;

		public FormArraySettings()
		{
			InitializeComponent();
			
			array_settings = Settings.ArraySettings.LoadFromXml("ArraySettings.xml");
			Init();
		}

		private void Init()
		{
			txtSize.Text = array_settings.array_size.ToString();

			if (array_settings.sorting_alg == Settings.ArraySettings.SortingAlg.Bubble)
				rbtnBubble.Checked = true;
			else if (array_settings.sorting_alg == Settings.ArraySettings.SortingAlg.Insertion)
				rbtnInsertion.Checked = true;
			else if (array_settings.sorting_alg == Settings.ArraySettings.SortingAlg.Selection)
				rbtnSelection.Checked = true;

			if (array_settings.array_type == Settings.ArraySettings.ArrayType.Static)
				rbtnStatic.Checked = true;
			else if (array_settings.array_type == Settings.ArraySettings.ArrayType.Dynamic)
				rbtnDynamic.Checked = true;
		}

		private void txtSize_KeyPress(object sender, KeyPressEventArgs e)
		{
			if (!char.IsDigit(e.KeyChar) && !char.IsControl(e.KeyChar))
				e.Handled = true;
		}

		private void txtSize_Leave(object sender, EventArgs e)
		{
			if (txtSize.Text == string.Empty)
				txtSize.Text = 5.ToString();
		}

		private void btnApply_Click(object sender, EventArgs e)
		{
			array_settings.array_size = Int32.Parse(txtSize.Text);
			array_settings.SaveAsXML("ArraySettings.xml");
			Close();
		}

		private void btnCancel_Click(object sender, EventArgs e)
		{
			Close();
		}

		private void rbtnType_CheckedChanged(object sender, EventArgs e)
		{
			if (rbtnStatic.Checked)
				array_settings.array_type = Settings.ArraySettings.ArrayType.Static;
			else if (rbtnDynamic.Checked)
				array_settings.array_type = Settings.ArraySettings.ArrayType.Dynamic;
		}

		private void rbtnSortAlg_CheckedChanged(object sender, EventArgs e)
		{
			if (rbtnBubble.Checked)
				array_settings.sorting_alg = Settings.ArraySettings.SortingAlg.Bubble;
			else if (rbtnInsertion.Checked)
				array_settings.sorting_alg = Settings.ArraySettings.SortingAlg.Insertion;
			else if (rbtnSelection.Checked)
				array_settings.sorting_alg = Settings.ArraySettings.SortingAlg.Selection;
		}
	}
}
