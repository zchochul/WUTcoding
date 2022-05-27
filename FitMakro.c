void FitMakro() 
{
	cout<<"Podaj nazwe pliku wejsciowego (bez .txt)"<<endl;

	string wejsciowy;

	cin>>wejsciowy;

	string file = wejsciowy + ".txt";

	ifstream ifile;
	ifile.open(file.c_str());
	
	TF1 *fitfunc = new TF1("fitfunc","gaus",0,254);
	double x[255];// x
	double ex[255]={0};//niepewnosci x
	double y[255];//y
	double ey[255]={0};//niepewnosci y

	int Ox;

	for(int i=0; i<255; i++)
	{
		ifile>>Ox;
		x[i] = Ox;
	}

	int Oy;	

	for(int i=0; i<255; i++)
	{
		ifile>>Oy;
		y[i] = Oy;
	}
	

	ifile.close();

	TGraphErrors *h = new TGraphErrors(255,x,y,ex,ey);

	h->Fit("fitfunc","rob");


	double max = fitfunc->GetMaximum();
	double x_maximum = fitfunc->GetMaximumX();
	double fwhm_left = fitfunc->GetX(max/2,0, x_maximum);
	double fwhm_right = fitfunc->GetX(max/2, x_maximum, 255);
	cout<<"FWHM = " << fwhm_right - fwhm_left<<endl;


	h->SetTitle(wejsciowy.c_str());
	h->GetXaxis()->SetTitle("numer kanalu");
	h->GetYaxis()->SetTitle("liczba zliczen");

	TCanvas *canva = new TCanvas();	

	gStyle->SetOptFit(0111);
	h->Draw();

	string wyjsciowy = wejsciowy + ".png";

	canva->Print(wyjsciowy.c_str());



}