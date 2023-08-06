namespace ArraySettings
{
	partial class FormArraySettings
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.TitleLabel = new System.Windows.Forms.Label();
			this.lblType = new System.Windows.Forms.Label();
			this.gbxTyp = new System.Windows.Forms.GroupBox();
			this.lblSize = new System.Windows.Forms.Label();
			this.txtSize = new System.Windows.Forms.TextBox();
			this.rbtnDynamic = new System.Windows.Forms.RadioButton();
			this.rbtnStatic = new System.Windows.Forms.RadioButton();
			this.btnApply = new System.Windows.Forms.Button();
			this.btnCancel = new System.Windows.Forms.Button();
			this.gbxSortingAlg = new System.Windows.Forms.GroupBox();
			this.rbtnInsertion = new System.Windows.Forms.RadioButton();
			this.rbtnSelection = new System.Windows.Forms.RadioButton();
			this.rbtnBubble = new System.Windows.Forms.RadioButton();
			this.gbxTyp.SuspendLayout();
			this.gbxSortingAlg.SuspendLayout();
			this.SuspendLayout();
			// 
			// TitleLabel
			// 
			this.TitleLabel.AutoSize = true;
			this.TitleLabel.Font = new System.Drawing.Font("Comic Sans MS", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.TitleLabel.Location = new System.Drawing.Point(70, 9);
			this.TitleLabel.Name = "TitleLabel";
			this.TitleLabel.Size = new System.Drawing.Size(141, 26);
			this.TitleLabel.TabIndex = 0;
			this.TitleLabel.Text = "Array Settings";
			// 
			// lblType
			// 
			this.lblType.AutoSize = true;
			this.lblType.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblType.Location = new System.Drawing.Point(22, 16);
			this.lblType.Name = "lblType";
			this.lblType.Size = new System.Drawing.Size(42, 18);
			this.lblType.TabIndex = 1;
			this.lblType.Text = "Type:";
			// 
			// gbxTyp
			// 
			this.gbxTyp.Controls.Add(this.lblSize);
			this.gbxTyp.Controls.Add(this.txtSize);
			this.gbxTyp.Controls.Add(this.rbtnDynamic);
			this.gbxTyp.Controls.Add(this.rbtnStatic);
			this.gbxTyp.Controls.Add(this.lblType);
			this.gbxTyp.Location = new System.Drawing.Point(12, 38);
			this.gbxTyp.Name = "gbxTyp";
			this.gbxTyp.Size = new System.Drawing.Size(275, 76);
			this.gbxTyp.TabIndex = 2;
			this.gbxTyp.TabStop = false;
			// 
			// lblSize
			// 
			this.lblSize.AutoSize = true;
			this.lblSize.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblSize.Location = new System.Drawing.Point(25, 41);
			this.lblSize.Name = "lblSize";
			this.lblSize.Size = new System.Drawing.Size(39, 18);
			this.lblSize.TabIndex = 6;
			this.lblSize.Text = "Size:";
			// 
			// txtSize
			// 
			this.txtSize.Font = new System.Drawing.Font("Comic Sans MS", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.txtSize.Location = new System.Drawing.Point(89, 39);
			this.txtSize.MaxLength = 2;
			this.txtSize.Name = "txtSize";
			this.txtSize.Size = new System.Drawing.Size(39, 23);
			this.txtSize.TabIndex = 5;
			this.txtSize.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.txtSize_KeyPress);
			this.txtSize.Leave += new System.EventHandler(this.txtSize_Leave);
			// 
			// rbtnDynamic
			// 
			this.rbtnDynamic.AutoSize = true;
			this.rbtnDynamic.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.rbtnDynamic.Location = new System.Drawing.Point(193, 14);
			this.rbtnDynamic.Name = "rbtnDynamic";
			this.rbtnDynamic.Size = new System.Drawing.Size(76, 22);
			this.rbtnDynamic.TabIndex = 4;
			this.rbtnDynamic.TabStop = true;
			this.rbtnDynamic.Text = "Dynamic";
			this.rbtnDynamic.UseVisualStyleBackColor = true;
			this.rbtnDynamic.CheckedChanged += new System.EventHandler(this.rbtnType_CheckedChanged);
			// 
			// rbtnStatic
			// 
			this.rbtnStatic.AutoSize = true;
			this.rbtnStatic.Checked = true;
			this.rbtnStatic.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.rbtnStatic.Location = new System.Drawing.Point(89, 14);
			this.rbtnStatic.Name = "rbtnStatic";
			this.rbtnStatic.Size = new System.Drawing.Size(63, 22);
			this.rbtnStatic.TabIndex = 3;
			this.rbtnStatic.TabStop = true;
			this.rbtnStatic.Text = "Static";
			this.rbtnStatic.UseVisualStyleBackColor = true;
			this.rbtnStatic.CheckedChanged += new System.EventHandler(this.rbtnType_CheckedChanged);
			// 
			// btnApply
			// 
			this.btnApply.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.btnApply.Location = new System.Drawing.Point(37, 266);
			this.btnApply.Name = "btnApply";
			this.btnApply.Size = new System.Drawing.Size(88, 31);
			this.btnApply.TabIndex = 3;
			this.btnApply.Text = "Apply";
			this.btnApply.UseVisualStyleBackColor = true;
			this.btnApply.Click += new System.EventHandler(this.btnApply_Click);
			// 
			// btnCancel
			// 
			this.btnCancel.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.btnCancel.Location = new System.Drawing.Point(144, 266);
			this.btnCancel.Name = "btnCancel";
			this.btnCancel.Size = new System.Drawing.Size(88, 31);
			this.btnCancel.TabIndex = 4;
			this.btnCancel.Text = "Cancel";
			this.btnCancel.UseVisualStyleBackColor = true;
			this.btnCancel.Click += new System.EventHandler(this.btnCancel_Click);
			// 
			// gbxSortingAlg
			// 
			this.gbxSortingAlg.Controls.Add(this.rbtnInsertion);
			this.gbxSortingAlg.Controls.Add(this.rbtnSelection);
			this.gbxSortingAlg.Controls.Add(this.rbtnBubble);
			this.gbxSortingAlg.Font = new System.Drawing.Font("Comic Sans MS", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.gbxSortingAlg.Location = new System.Drawing.Point(12, 129);
			this.gbxSortingAlg.Name = "gbxSortingAlg";
			this.gbxSortingAlg.Size = new System.Drawing.Size(275, 111);
			this.gbxSortingAlg.TabIndex = 5;
			this.gbxSortingAlg.TabStop = false;
			this.gbxSortingAlg.Text = "Sorting algorithm";
			// 
			// rbtnInsertion
			// 
			this.rbtnInsertion.AutoSize = true;
			this.rbtnInsertion.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.rbtnInsertion.Location = new System.Drawing.Point(12, 78);
			this.rbtnInsertion.Name = "rbtnInsertion";
			this.rbtnInsertion.Size = new System.Drawing.Size(110, 22);
			this.rbtnInsertion.TabIndex = 6;
			this.rbtnInsertion.TabStop = true;
			this.rbtnInsertion.Text = "Insertion sort";
			this.rbtnInsertion.UseVisualStyleBackColor = true;
			// 
			// rbtnSelection
			// 
			this.rbtnSelection.AutoSize = true;
			this.rbtnSelection.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.rbtnSelection.Location = new System.Drawing.Point(12, 50);
			this.rbtnSelection.Name = "rbtnSelection";
			this.rbtnSelection.Size = new System.Drawing.Size(111, 22);
			this.rbtnSelection.TabIndex = 5;
			this.rbtnSelection.TabStop = true;
			this.rbtnSelection.Text = "Selection sort";
			this.rbtnSelection.UseVisualStyleBackColor = true;
			// 
			// rbtnBubble
			// 
			this.rbtnBubble.AutoSize = true;
			this.rbtnBubble.Checked = true;
			this.rbtnBubble.Font = new System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.rbtnBubble.Location = new System.Drawing.Point(12, 22);
			this.rbtnBubble.Name = "rbtnBubble";
			this.rbtnBubble.Size = new System.Drawing.Size(96, 22);
			this.rbtnBubble.TabIndex = 4;
			this.rbtnBubble.TabStop = true;
			this.rbtnBubble.Text = "Bubble sort";
			this.rbtnBubble.UseVisualStyleBackColor = true;
			this.rbtnBubble.CheckedChanged += new System.EventHandler(this.rbtnSortAlg_CheckedChanged);
			// 
			// FormArraySettings
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(299, 309);
			this.Controls.Add(this.gbxSortingAlg);
			this.Controls.Add(this.btnCancel);
			this.Controls.Add(this.btnApply);
			this.Controls.Add(this.gbxTyp);
			this.Controls.Add(this.TitleLabel);
			this.MaximizeBox = false;
			this.MaximumSize = new System.Drawing.Size(315, 348);
			this.MinimizeBox = false;
			this.MinimumSize = new System.Drawing.Size(315, 348);
			this.Name = "FormArraySettings";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "ArraySettings";
			this.gbxTyp.ResumeLayout(false);
			this.gbxTyp.PerformLayout();
			this.gbxSortingAlg.ResumeLayout(false);
			this.gbxSortingAlg.PerformLayout();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label TitleLabel;
		private System.Windows.Forms.Label lblType;
		private System.Windows.Forms.GroupBox gbxTyp;
		private System.Windows.Forms.RadioButton rbtnDynamic;
		private System.Windows.Forms.RadioButton rbtnStatic;
		private System.Windows.Forms.Button btnApply;
		private System.Windows.Forms.TextBox txtSize;
		private System.Windows.Forms.Button btnCancel;
		private System.Windows.Forms.Label lblSize;
		private System.Windows.Forms.GroupBox gbxSortingAlg;
		private System.Windows.Forms.RadioButton rbtnInsertion;
		private System.Windows.Forms.RadioButton rbtnSelection;
		private System.Windows.Forms.RadioButton rbtnBubble;
	}
}

