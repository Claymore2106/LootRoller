#pragma once

namespace LootRoller {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for MainForm
	/// </summary>
	public ref class MainForm : public System::Windows::Forms::Form
	{
	public:
		MainForm(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~MainForm()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::TabControl^  tabControl1;
	protected:
	private: System::Windows::Forms::TabPage^  tabPage1;
	private: System::Windows::Forms::ListBox^  listItems;

	private: System::Windows::Forms::TabPage^  tabPage2;
	private: System::Windows::Forms::Button^  button1;
	private: System::Windows::Forms::MenuStrip^  menuStrip1;
	private: System::Windows::Forms::ToolStripMenuItem^  fileToolStripMenuItem;
	private: System::Windows::Forms::Label^  lFlavor_Text;

	private: System::Windows::Forms::Label^  lItem_Name;
	private: System::Windows::Forms::PictureBox^  picItem;


	private: System::Windows::Forms::Button^  button3;
	private: System::Windows::Forms::Button^  button2;
	private: System::Windows::Forms::GroupBox^  groupBox1;
	private: System::Windows::Forms::Label^  lDetail0;

	private: System::Windows::Forms::Label^  lAttribute0;


	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			this->tabControl1 = (gcnew System::Windows::Forms::TabControl());
			this->tabPage1 = (gcnew System::Windows::Forms::TabPage());
			this->tabPage2 = (gcnew System::Windows::Forms::TabPage());
			this->listItems = (gcnew System::Windows::Forms::ListBox());
			this->button1 = (gcnew System::Windows::Forms::Button());
			this->menuStrip1 = (gcnew System::Windows::Forms::MenuStrip());
			this->fileToolStripMenuItem = (gcnew System::Windows::Forms::ToolStripMenuItem());
			this->picItem = (gcnew System::Windows::Forms::PictureBox());
			this->lItem_Name = (gcnew System::Windows::Forms::Label());
			this->lFlavor_Text = (gcnew System::Windows::Forms::Label());
			this->groupBox1 = (gcnew System::Windows::Forms::GroupBox());
			this->button2 = (gcnew System::Windows::Forms::Button());
			this->button3 = (gcnew System::Windows::Forms::Button());
			this->lAttribute0 = (gcnew System::Windows::Forms::Label());
			this->lDetail0 = (gcnew System::Windows::Forms::Label());
			this->tabControl1->SuspendLayout();
			this->tabPage1->SuspendLayout();
			this->menuStrip1->SuspendLayout();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->picItem))->BeginInit();
			this->groupBox1->SuspendLayout();
			this->SuspendLayout();
			// 
			// tabControl1
			// 
			this->tabControl1->Controls->Add(this->tabPage1);
			this->tabControl1->Controls->Add(this->tabPage2);
			this->tabControl1->Location = System::Drawing::Point(12, 27);
			this->tabControl1->Name = L"tabControl1";
			this->tabControl1->SelectedIndex = 0;
			this->tabControl1->Size = System::Drawing::Size(571, 374);
			this->tabControl1->TabIndex = 0;
			// 
			// tabPage1
			// 
			this->tabPage1->Controls->Add(this->button3);
			this->tabPage1->Controls->Add(this->button2);
			this->tabPage1->Controls->Add(this->groupBox1);
			this->tabPage1->Controls->Add(this->lFlavor_Text);
			this->tabPage1->Controls->Add(this->lItem_Name);
			this->tabPage1->Controls->Add(this->picItem);
			this->tabPage1->Controls->Add(this->button1);
			this->tabPage1->Controls->Add(this->listItems);
			this->tabPage1->Location = System::Drawing::Point(4, 22);
			this->tabPage1->Name = L"tabPage1";
			this->tabPage1->Padding = System::Windows::Forms::Padding(3);
			this->tabPage1->Size = System::Drawing::Size(563, 348);
			this->tabPage1->TabIndex = 0;
			this->tabPage1->Text = L"tabPage1";
			this->tabPage1->UseVisualStyleBackColor = true;
			this->tabPage1->Click += gcnew System::EventHandler(this, &MainForm::tabPage1_Click);
			// 
			// tabPage2
			// 
			this->tabPage2->Location = System::Drawing::Point(4, 22);
			this->tabPage2->Name = L"tabPage2";
			this->tabPage2->Padding = System::Windows::Forms::Padding(3);
			this->tabPage2->Size = System::Drawing::Size(556, 290);
			this->tabPage2->TabIndex = 1;
			this->tabPage2->Text = L"tabPage2";
			this->tabPage2->UseVisualStyleBackColor = true;
			// 
			// listItems
			// 
			this->listItems->FormattingEnabled = true;
			this->listItems->Location = System::Drawing::Point(-2, 0);
			this->listItems->Name = L"listItems";
			this->listItems->Size = System::Drawing::Size(120, 316);
			this->listItems->TabIndex = 0;
			// 
			// button1
			// 
			this->button1->Location = System::Drawing::Point(6, 319);
			this->button1->Name = L"button1";
			this->button1->Size = System::Drawing::Size(75, 23);
			this->button1->TabIndex = 1;
			this->button1->Text = L"Create New";
			this->button1->UseVisualStyleBackColor = true;
			// 
			// menuStrip1
			// 
			this->menuStrip1->Items->AddRange(gcnew cli::array< System::Windows::Forms::ToolStripItem^  >(1) { this->fileToolStripMenuItem });
			this->menuStrip1->Location = System::Drawing::Point(0, 0);
			this->menuStrip1->Name = L"menuStrip1";
			this->menuStrip1->Size = System::Drawing::Size(595, 24);
			this->menuStrip1->TabIndex = 1;
			this->menuStrip1->Text = L"menuStrip1";
			// 
			// fileToolStripMenuItem
			// 
			this->fileToolStripMenuItem->Name = L"fileToolStripMenuItem";
			this->fileToolStripMenuItem->Size = System::Drawing::Size(37, 20);
			this->fileToolStripMenuItem->Text = L"File";
			// 
			// picItem
			// 
			this->picItem->Location = System::Drawing::Point(124, 6);
			this->picItem->Name = L"picItem";
			this->picItem->Size = System::Drawing::Size(50, 50);
			this->picItem->TabIndex = 2;
			this->picItem->TabStop = false;
			// 
			// lItem_Name
			// 
			this->lItem_Name->AutoSize = true;
			this->lItem_Name->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 15, System::Drawing::FontStyle::Underline, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->lItem_Name->Location = System::Drawing::Point(180, 6);
			this->lItem_Name->Name = L"lItem_Name";
			this->lItem_Name->Size = System::Drawing::Size(112, 25);
			this->lItem_Name->TabIndex = 3;
			this->lItem_Name->Text = L"Item_Name";
			// 
			// lFlavor_Text
			// 
			this->lFlavor_Text->AutoSize = true;
			this->lFlavor_Text->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 8.25F, System::Drawing::FontStyle::Italic, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->lFlavor_Text->Location = System::Drawing::Point(180, 43);
			this->lFlavor_Text->Name = L"lFlavor_Text";
			this->lFlavor_Text->Size = System::Drawing::Size(63, 13);
			this->lFlavor_Text->TabIndex = 4;
			this->lFlavor_Text->Text = L"Flavor_Text";
			this->lFlavor_Text->Click += gcnew System::EventHandler(this, &MainForm::label2_Click);
			// 
			// groupBox1
			// 
			this->groupBox1->Controls->Add(this->lDetail0);
			this->groupBox1->Controls->Add(this->lAttribute0);
			this->groupBox1->Location = System::Drawing::Point(124, 81);
			this->groupBox1->Name = L"groupBox1";
			this->groupBox1->Size = System::Drawing::Size(426, 215);
			this->groupBox1->TabIndex = 5;
			this->groupBox1->TabStop = false;
			this->groupBox1->Text = L"groupBox1";
			// 
			// button2
			// 
			this->button2->Location = System::Drawing::Point(98, 319);
			this->button2->Name = L"button2";
			this->button2->Size = System::Drawing::Size(76, 23);
			this->button2->TabIndex = 6;
			this->button2->Text = L"Add Attribute";
			this->button2->UseVisualStyleBackColor = true;
			// 
			// button3
			// 
			this->button3->Location = System::Drawing::Point(474, 319);
			this->button3->Name = L"button3";
			this->button3->Size = System::Drawing::Size(75, 23);
			this->button3->TabIndex = 7;
			this->button3->Text = L"Save";
			this->button3->UseVisualStyleBackColor = true;
			// 
			// lAttribute0
			// 
			this->lAttribute0->AutoSize = true;
			this->lAttribute0->Location = System::Drawing::Point(7, 20);
			this->lAttribute0->Name = L"lAttribute0";
			this->lAttribute0->Size = System::Drawing::Size(46, 13);
			this->lAttribute0->TabIndex = 0;
			this->lAttribute0->Text = L"Attribute";
			// 
			// lDetail0
			// 
			this->lDetail0->AutoSize = true;
			this->lDetail0->Location = System::Drawing::Point(298, 20);
			this->lDetail0->Name = L"lDetail0";
			this->lDetail0->Size = System::Drawing::Size(34, 13);
			this->lDetail0->TabIndex = 1;
			this->lDetail0->Text = L"Detail";
			// 
			// MainForm
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 13);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->ClientSize = System::Drawing::Size(595, 413);
			this->Controls->Add(this->tabControl1);
			this->Controls->Add(this->menuStrip1);
			this->Name = L"MainForm";
			this->Text = L"Loot Roller [Alpha] v0.1";
			this->Load += gcnew System::EventHandler(this, &MainForm::MainForm_Load);
			this->tabControl1->ResumeLayout(false);
			this->tabPage1->ResumeLayout(false);
			this->tabPage1->PerformLayout();
			this->menuStrip1->ResumeLayout(false);
			this->menuStrip1->PerformLayout();
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->picItem))->EndInit();
			this->groupBox1->ResumeLayout(false);
			this->groupBox1->PerformLayout();
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	private: System::Void tabPage1_Click(System::Object^  sender, System::EventArgs^  e) {
	}
	private: System::Void MainForm_Load(System::Object^  sender, System::EventArgs^  e) {
	}
private: System::Void label2_Click(System::Object^  sender, System::EventArgs^  e) {
}
};
}
